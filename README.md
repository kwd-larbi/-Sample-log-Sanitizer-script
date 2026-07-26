# 🚀 Python Log Processing Pipeline

> **Transforming raw IT ticket logs into structured CSV and Excel reports using Python, Regular Expressions, and OpenPyXL.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Regex](https://img.shields.io/badge/Regex-Log%20Parsing-green)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel%20Automation-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

IT systems generate large volumes of log data that often exist as unstructured text. While these logs contain valuable information, manually reviewing and organizing them can be repetitive and time-consuming.

This project automates the process of parsing raw IT ticket logs into structured reports. Using Python and Regular Expressions, it extracts key information, validates log entries, identifies malformed records, and exports the results into CSV and formatted Excel reports for easier analysis and reporting.

---

# ✨ Features

- 📂 Reads raw IT ticket log files
- 🔍 Parses log entries using Regular Expressions
- 📋 Extracts:
  - Ticket ID
  - Priority Level
  - System Message
  - Employee ID
- ⚠️ Identifies malformed log entries
- 📄 Generates structured CSV reports
- 📊 Automatically creates formatted Excel dashboards
- 📏 Auto-adjusts Excel column widths
- 📈 Displays processing statistics

---

# 🛠 Technologies Used

- Python 3
- Regular Expressions (`re`)
- CSV
- OpenPyXL
- OS Module
- File Handling

---

# 📂 Project Structure

```text
python-log-processing-pipeline/
│
├── formatted_ticket_router.py
├── ticket_router.py
├── regexpatterntest.py
│
├── unprocessed_tickets/
│   └── incoming_tickets.log
│
├── structured_it_dashboard.csv
├── structured_it_dashboard.xlsx
│
├── LICENSE
└── README.md
```

---

# ⚙️ How It Works

```text
Raw IT Ticket Logs
        │
        ▼
Directory Scanner
        │
        ▼
Regular Expression Parser
        │
 ┌───────────────┐
 │               │
 ▼               ▼
Valid Logs   Malformed Logs
 │
 ▼
Structured Data
 │
 ▼
CSV Report
 │
 ▼
Formatted Excel Dashboard
```

---

# 📄 Sample Input

```text
ERROR [pid:1458] Database connection failed - User:EMP1024

WARNING [pid:3189] Disk usage exceeded threshold - User:EMP1102

INFO [pid:2231] User successfully authenticated - User:EMP1056
```

---

# 📊 Output

The application automatically generates:

- **structured_it_dashboard.csv**
- **structured_it_dashboard.xlsx**

These reports organize extracted ticket information into a clean, structured format that is easier to review, analyze, and share.

---

# 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/kwd-larbi/python-log-processing-pipeline.git
```

### Navigate into the project

```bash
cd python-log-processing-pipeline
```

### Install dependencies

```bash
pip install openpyxl
```

### Run the project

```bash
python formatted_ticket_router.py
```

---

# 💡 Skills Demonstrated

This project showcases practical software engineering skills, including:

- Python Programming
- Automation
- Regular Expressions (Regex)
- File Handling
- Directory Traversal
- CSV Processing
- Excel Automation
- Data Validation
- Data Parsing
- Report Generation
- Problem Solving

---

# 📚 What I Learned

Building this project strengthened my understanding of:

- Parsing structured text using Regular Expressions
- Automating repetitive workflows with Python
- Reading and writing files
- Working with CSV datasets
- Creating Excel reports using OpenPyXL
- Organizing Python code into reusable functions
- Building an end-to-end data processing workflow

---


---

# 🎓 Inspiration

This project was inspired by the Python automation concepts I learned while completing the **Google IT Automation with Python Professional Certificate**. It allowed me to apply those concepts by building a practical automation tool for processing IT ticket logs and generating structured reports.

---

# 👨‍💻 Author

**Kwadwo Larbi**

Aspiring Software Engineer | Python Developer | Automation Enthusiast

I'm passionate about building Python applications that automate repetitive tasks, organize data, and solve practical problems. I'm continuously expanding my software engineering skills by creating hands-on projects and preparing for internship opportunities.

---

# ⭐ Support

If you found this project interesting or useful, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.
