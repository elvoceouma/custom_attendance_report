from odoo import models
import calendar
from datetime import datetime, timedelta


class AttendanceXlsxReport(models.AbstractModel):
    _name = "report.monthly_attendance_report.attendance_report_xlsx"
    _inherit = "report.report_xlsx.abstract"
    _description = "Attendance XLSX Report"

    def generate_xlsx_report(self, workbook, data, wizard):
        month = int(data.get("month"))
        year = int(data.get("year"))

        sheet = workbook.add_worksheet("Attendance Report")

        formats = {
            "header": workbook.add_format(
                {
                    "bold": True,
                    "align": "center",
                    "bg_color": "#D3D3D3",
                    "border": 1,
                    "text_wrap": True,
                }
            ),
            "date": workbook.add_format({"align": "center", "border": 1}),
            "time": workbook.add_format(
                {"num_format": "hh:mm", "align": "center", "border": 1}
            ),
            "weekend": workbook.add_format(
                {"bg_color": "#F2F2F2", "align": "center", "border": 1}
            ),
            "present": workbook.add_format(
                {"bg_color": "#90EE90", "align": "center", "border": 1}  # Light green
            ),
            "absent": workbook.add_format(
                {"bg_color": "#FFB6C1", "align": "center", "border": 1}  # Light red
            ),
        }

        self._write_headers(sheet, month, year, formats)

        domain = []
        if data.get("employee_ids"):
            domain = [("id", "in", data["employee_ids"])]
        employees = self.env["hr.employee"].search(domain)

        self._write_attendance_data(sheet, employees, month, year, formats)

        self._adjust_column_widths(sheet, month, year)

    def _write_headers(self, sheet, month, year, formats):
        month_name = calendar.month_name[month]
        _, num_days = calendar.monthrange(year, month)

        sheet.merge_range(
            0, 0, 0, num_days + 2, f"{month_name} {year}", formats["header"]
        )

        sheet.write(1, 0, "Employee", formats["header"])
        sheet.write(1, 1, "Department", formats["header"])

        for day in range(1, num_days + 1):
            date = datetime(year, month, day)
            col_format = (
                formats["weekend"] if date.weekday() in (4, 5) else formats["header"]
            )
            sheet.write(1, day + 1, day, col_format)

    def _write_attendance_data(self, sheet, employees, month, year, formats):
        row = 2
        for employee in employees:
            sheet.write(row, 0, employee.name, formats["date"])
            sheet.write(row, 1, employee.department_id.name or "", formats["date"])

            start_date = datetime(year, month, 1)
            end_date = (
                datetime(year + 1, 1, 1)
                if month == 12
                else datetime(year, month + 1, 1)
            )

            attendances = self.env["hr.attendance"].search(
                [
                    ("employee_id", "=", employee.id),
                    ("check_in", ">=", start_date),
                    ("check_in", "<", end_date),
                ]
            )

            attendance_by_date = {
                attendance.check_in.date(): attendance for attendance in attendances
            }

            _, num_days = calendar.monthrange(year, month)
            for day in range(1, num_days + 1):
                date = datetime(year, month, day).date()
                col = day + 1

                if date in attendance_by_date:
                    sheet.write(row, col, "P", formats["present"])
                else:
                    if datetime(year, month, day).weekday() in (4, 5):
                        sheet.write(row, col, "W", formats["weekend"])
                    else:
                        sheet.write(row, col, "A", formats["absent"])

            row += 1

    def _adjust_column_widths(self, sheet, month, year):
        sheet.set_column(0, 0, 30)  # employee_name
        sheet.set_column(1, 1, 20)  # department
        _, num_days = calendar.monthrange(year, month)
        sheet.set_column(2, num_days + 1, 5)
