# CRM App

[![Go Live](https://img.shields.io/badge/Go%20Live%20🚀-green?style=for-the-badge)](https://guibrandt.pythonanywhere.com)

## Description

The CRM App is a web application designed to securely manage customer data. It allows you to add, update, and remove customer records, with form validations and automatic address filling based on ZIP code.

## Features

- **Customer Registration:** Add new customers securely.
- **Update and Delete:** Update or remove existing customer records as needed.
- **Form Validations:** Ensures that entered data is accurate and complete.
- **ZIP Code Automation:** Automatically fills in address fields based on the provided ZIP code.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django, Python
- **Database:** MySQL

## Quickstart

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/crm-app.git
    ```
2. **Create and activate virtual enviroment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create the database:**
   - run the db.py script to create the database and its tables:
   ```bash
    python mybd.py
   ```
5. **Apply database migrations:**
  ```bash
    python manage.py migrate
  ```
6. **Start the development server:**
  ```bash
    python manage.py runserver
  ```

## Contact
For questions or suggestions, contact Guilherme Brandt at glbfaria42@gmail.com
