# Monthly Attendance Report Module

## 🎯 Overview
A comprehensive attendance reporting module for Odoo 16.0 that generates detailed monthly attendance reports in Excel format. Specifically designed for UAE calendar with Friday-Saturday weekends.

## ✨ Features

```python
features = {
    "report_types": [
        "Monthly Excel Reports",
        "Individual Employee Reports",
        "Department-wise Reports"
    ],
    "tracking": [
        "Daily Attendance Status",
        "Present/Absent Marking",
        "Weekend Handling",
        "Department Tracking"
    ],
    "formats": [
        "Excel Sheets",
        "Color-coded Status",
        "Customizable Date Ranges"
    ]
}
```

## 📋 Prerequisites

```python
requirements = {
    "odoo": "16.0",
    "python": ">=3.8",
    "dependencies": [
        "hr",
        "hr_attendance",
        "report_xlsx"
    ]
}
```

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/elvoceouma/custom_attendance_repor.git

# Move to custom addons directory
mv monthly_attendance_report /path/to/odoo/custom/addons/

# Restart Odoo server
service odoo restart  # Linux
# or
net stop odoo && net start odoo  # Windows
```

## 📝 Configuration

```python
# Enable Developer Mode in Odoo
{
    "steps": [
        "Settings → Developer Tools → Activate Developer Mode",
        "Apps → Update Apps List",
        "Search for 'Monthly Attendance Report'",
        "Install the module"
    ]
}
```

## 🚀 Usage

### Access Rights Setup
```python
user_access = {
    "HR Manager": [
        "Full access to reports",
        "Can configure report settings",
        "Can generate all types of reports"
    ],
    "HR Officer": [
        "Can generate reports",
        "Can view all employee reports"
    ],
    "Employee": [
        "Can view own attendance reports"
    ]
}
```

### Generate Monthly Report
```python
# Navigation Path
menu_path = [
    "Attendance",
    "Attendance Reports",
    "Generate Monthly Report"
]

# Report Generation Steps
report_wizard = {
    "fields": {
        "month": "Select target month",
        "year": "Select target year",
        "employees": ["Multiple selection allowed", "Optional"]
    },
    "actions": {
        "generate": "Click 'Generate Excel Report'",
        "download": "Save the generated Excel file"
    }
}
```

### Report Features
```python
report_content = {
    "header_info": [
        "Employee Name",
        "Department",
        "Daily Status"
    ],
    "status_codes": {
        "P": "Present",
        "A": "Absent",
        "W": "Weekend"
    },
    "color_coding": {
        "present": "Light Green",
        "absent": "Light Red",
        "weekend": "Light Gray"
    }
}
```

## 🎨 Customization

### Override Weekend Days
```python
# In attendance_report.py
class AttendanceXlsxReport(models.AbstractModel):
    def _is_weekend(self, date):
        # Default: Friday (4) and Saturday (5)
        return date.weekday() in (4, 5)  # Modify as needed
```

### Custom Report Styling
```python
# In attendance_report.py
formats = {
    'header': workbook.add_format({
        'bold': True,
        'align': 'center',
        'bg_color': '#YOUR_COLOR',
        'border': 1
    })
    # Add more custom formats
}
```

## 🛠 Troubleshooting

```python
common_issues = {
    "Report Not Generating": [
        "Check user access rights",
        "Verify report_xlsx module installation",
        "Confirm attendance records exist"
    ],
    "Missing Data": [
        "Verify employee records",
        "Check attendance check-in/out records",
        "Validate date range selection"
    ],
    "Excel Format Issues": [
        "Update xlsx writer library",
        "Check custom format definitions",
        "Verify Excel version compatibility"
    ]
}
```

## 📱 Support

```python
contact_info = {
    "github": "https://github.com/your-repo/issues",
    "email": "support@yourcompany.com",
    "docs": "https://yourcompany.com/docs/attendance-report"
}
```

## 🔄 Changelog

```python
versions = {
    "16.0.1.0.0": [
        "Initial release",
        "Basic attendance reporting",
        "UAE calendar support"
    ],
    "16.0.1.1.0": [
        "Added department filtering",
        "Improved color coding",
        "Performance optimizations"
    ]
}
```

## 📜 License

```python
license_info = {
    "type": "LGPL-3",
    "year": "2024",
    "author": "Your Company",
    "website": "https://www.yourcompany.com"
}
```
