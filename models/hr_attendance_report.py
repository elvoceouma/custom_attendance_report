from odoo import models, fields, api
from datetime import datetime


class HRAttendanceMonthlyReport(models.Model):
    _name = "hr.attendance.monthly.report"
    _description = "Monthly Attendance Report"
    _rec_name = "employee_id"
    _order = "year desc, month desc"

    employee_id = fields.Many2one("hr.employee", string="Employee", required=True)
    department_id = fields.Many2one(
        related="employee_id.department_id", string="Department", store=True
    )
    month = fields.Selection(
        [
            ("01", "January"),
            ("02", "February"),
            ("03", "March"),
            ("04", "April"),
            ("05", "May"),
            ("06", "June"),
            ("07", "July"),
            ("08", "August"),
            ("09", "September"),
            ("10", "October"),
            ("11", "November"),
            ("12", "December"),
        ],
        string="Month",
        required=True,
    )
    year = fields.Integer(string="Year", required=True)
    total_working_days = fields.Integer(
        string="Working Days", compute="_compute_attendance_stats"
    )
    total_present_days = fields.Integer(
        string="Present Days", compute="_compute_attendance_stats"
    )
    total_absent_days = fields.Integer(
        string="Absent Days", compute="_compute_attendance_stats"
    )
    total_hours = fields.Float(
        string="Total Hours", compute="_compute_attendance_stats"
    )

    @api.depends("employee_id", "month", "year")
    def _compute_attendance_stats(self):
        for record in self:
            start_date = f"{record.year}-{record.month}-01"
            if record.month == "12":
                end_date = f"{record.year + 1}-01-01"
            else:
                next_month = str(int(record.month) + 1).zfill(2)
                end_date = f"{record.year}-{next_month}-01"

            attendances = self.env["hr.attendance"].search(
                [
                    ("employee_id", "=", record.employee_id.id),
                    ("check_in", ">=", start_date),
                    ("check_in", "<", end_date),
                ]
            )

            record.total_present_days = len(
                set(att.check_in.date() for att in attendances)
            )
            record.total_working_days = self._get_working_days(
                record.year, int(record.month)
            )
            record.total_absent_days = (
                record.total_working_days - record.total_present_days
            )
            record.total_hours = sum(att.worked_hours for att in attendances)

    def _get_working_days(self, year, month):
        from calendar import monthrange
        from datetime import date

        num_days = monthrange(year, month)[1]
        working_days = 0
        for day in range(1, num_days + 1):
            if date(year, month, day).weekday() not in (
                4,
                5,
            ):  # 4 is Friday and  5 is Saturday
                working_days += 1
        return working_days
