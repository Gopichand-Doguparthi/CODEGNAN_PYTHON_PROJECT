# University Management System

A Python-based Streamlit application for managing colleges, students, and teachers in a simple university dashboard.

## Overview

This project helps users:

- Create and manage multiple colleges
- Add student details such as name, roll number, and branch
- Add teacher details such as name, branch, and subject
- View lists of students and teachers for each college
- Browse the list of colleges currently created in the system

## Tech Stack

- Python
- Streamlit

## Project Structure

- `main.py` - Streamlit application logic
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Features

### College Management

- Create new colleges
- Store college objects in session state
- Manage multiple colleges inside the same application

### Student Management

- Add a new student to a selected college
- Capture:
  - Student name
  - Roll number
  - Branch
- Display all students in a college

### Teacher Management

- Add a new teacher to a selected college
- Capture:
  - Teacher name
  - Branch
  - Subject
- Display all teachers in a college

## Setup Instructions

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required package:

   ```bash
   pip install streamlit
   ```

4. Run the application:

   ```bash
   streamlit run main.py
   ```

5. Open the local Streamlit URL shown in the terminal in your browser.

## How to Use

1. Choose the option from the sidebar:
   - Create College
   - Add Student
   - Add Teacher
   - Display Students
   - Display Teachers
   - List of Colleges
2. Create a college before adding students or teachers.
3. Use the form fields to enter the required information.
4. The app will display the relevant records in the interface.

## Example Workflow

- Create a college named "ABC College"
- Add students such as "Alice" and "Bob"
- Add teachers such as "Dr. Mehta" and "Prof. Rao"
- View the list of students and teachers under that college

## Notes

This project is designed mainly for learning Python OOP concepts and small application logic using Streamlit. The data is stored in the browser session during the app runtime and is not persisted to a database.

## License

This project is intended for educational purposes.
