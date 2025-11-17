# 🎓 University Study Register System

A comprehensive command-line application for managing university student records, course completions, and academic data efficiently.
<!-- 
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Active-success.svg) -->

## 📋 Overview

The University Study Register System is a lightweight, file-based database management application designed to handle student information, course catalogs, and grade records. Built entirely in Python, this system provides an intuitive menu-driven interface for educational institutions to track student progress and maintain academic records.

## ✨ Features

### Core Functionality
- **👤 Student Management**
  - Add new students with validation
  - Search students by ID or name
  - View complete student profiles
  
- **📚 Course Operations**
  - Search courses by code or name
  - Display course details and instructors
  - View credit information

- **📝 Grade Tracking**
  - Record course completions
  - Automatic grade improvement tracking
  - Date-stamped completion records

- **📊 Academic Records**
  - Display student transcripts
  - Calculate total credits earned
  - Show complete academic history

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Text editor or IDE
- Git (for version control)

### Installation

1. Clone the repository
```bash
git clone https://github.com/navinxqz/Study-Register-LUT.git
```

2. Ensure data files are present
```
courses.txt
students.txt
passed.txt
```

3. Run the application
```bash
python RegisterSys.py
```

## 📁 File Structure

```
university-register-system/
│
├── study_register.py      # Main application file
├── courses.txt             # Course catalog database
├── students.txt            # Student information database
├── passed.txt              # Grade records database
└── README.md              # Project documentation
```

## 💾 Data Format

### courses.txt
```
CourseCode,CourseName,Credits,Teacher1,Teacher2,...
A0100,Introduction to Computer Science,3,Emily Johnson
```

### students.txt
```
StudentID,LastName,FirstName,SecondName,Email,StartYear,Program
69545,Sharp,Tom,,tom.sharp@lut.fi,2022,CE
```

### passed.txt
```
CourseCode,StudentID,Date,Grade
A0370,81274,2025-11-14,3
```

## 🎯 Usage Guide

### Main Menu Options

1. **Add Student** - Register new students in the system
2. **Search Student** - Find students by ID or name
3. **Search Course** - Locate courses by code or title
4. **Add Course Completion** - Record grades and completion dates
5. **Show Student's Record** - Display full academic transcript
6. **Exit** - Close the application

### Sample Workflow

```python
# Adding a new student
Enter your choice (1-6): 1
Enter student ID: 99999
Enter last name: Doe
Enter first name: John
...

# Recording course completion
Enter your choice (1-6): 4
Enter course code: A0100
Enter student ID: 99999
Enter completion date (YYYY-MM-DD): 2025-11-17
Enter grade (1-5): 4
```

## 🔧 Technical Details

### Key Features
- **List comprehensions** for efficient data processing
- **File I/O operations** for persistent storage
- **Input validation** to ensure data integrity
- **Automatic grade updates** when students retake courses
- **Date validation** using datetime module

### Program Flow
```
Start → Display Menu → User Input → Process Request → Update Files → Loop
```

## 🎓 Supported Programs

- **CE** - Computational Engineering
- **EE** - Electrical Engineering
- **ET** - Energy Technology
- **ME** - Mechanical Engineering
- **SE** - Software Engineering

## 🛠️ Tools & Technologies

- **Python 3.x** - Primary programming language
- **VS Code** - Code editor
- **Git Bash** - Version control
- **File-based storage** - CSV format for data persistence

## 📝 Code Highlights

- Clean, modular function design
- Efficient use of Python's built-in functions
- Readable variable naming conventions
- Comprehensive error handling
- User-friendly interface with clear prompts

## 🔐 Data Integrity

The system ensures:
- ✅ No duplicate student IDs
- ✅ Valid course codes verification
- ✅ Proper date format validation
- ✅ Grade range enforcement (1-5)
- ✅ Automatic best grade retention

## 🤝 Contributing

This is an academic project. Feel free to fork and experiment!

## 📄 License

This project is available under the MIT License.

## 👨‍💻 Author

Developed as part of university coursework focusing on file handling, data structures, and command-line applications in Python.

## 🙏 Acknowledgments

Special thanks to LUT University for providing the project specifications and test data files.

---

## 📌 Declaration

This project was completed independently without the use of AI assistance tools. All code was written manually using:
- Visual Studio Code (IDE)
- Git Bash (Version Control)
- Python Documentation (Reference)
- Personal problem-solving and debugging skills

**Date:** November 17, 2025

---

⭐ **If you find this project useful, please consider giving it a star!**

📧 **Questions or suggestions?** Feel free to open an issue or reach out!

---

*Made with ❤️ and lots of ☕*