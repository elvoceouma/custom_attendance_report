from odoo import models, fields, api
from datetime import datetime


class AttendanceReportWizard(models.TransientModel):
    _name = "attendance.report.wizard"
    _description = "Attendance Report Wizard"

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
        default=lambda self: str(datetime.now().month).zfill(2),
    )
    year = fields.Integer(
        string="Year", required=True, default=lambda self: datetime.now().year
    )
    employee_ids = fields.Many2many("hr.employee", string="Employees")

    def action_generate_report(self):
        self.ensure_one()
        data = {
            "month": self.month,
            "year": self.year,
            "employee_ids": self.employee_ids.ids if self.employee_ids else False,
        }
        return self.env.ref(
            "custom_attendance_report.attendance_report_xlsx"
        ).report_action(self, data=data)
