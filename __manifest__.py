# __manifest__.py
{
    "name": "Monthly Attendance Report",
    "version": "16.0.0.1",
    "category": "Human Resources",
    "summary": "Generate Monthly Attendance Reports",
    "description": """
        Generate detailed monthly attendance reports in Excel format
        Features:
        - Daily attendance records
        - Check-in/Check-out times
        - Weekend handling
    """,
    "author": "ELvice Ouma",
    "website": "https://github.com/elvoceouma",
    "depends": ["hr_attendance", "hr", "report_xlsx"],
    "data": [
        "security/ir.model.access.csv",
        "views/attendance_report_views.xml",
        "reports/attendance_report_template.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
