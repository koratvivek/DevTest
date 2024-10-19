# DevTest - Django File Upload and Email Summary Report

## Project Overview
This Django-based web application allows users to upload Excel or CSV files and generates a summary report of the data. The report is then emailed to a specified recipient, with details such as total records, DPD statistics, and a state-wise breakdown of the data.

## Features
- File upload functionality for Excel/CSV files.
- Summary report generation for uploaded data, including:
  - Total records.
  - Sum, average, median, maximum, and minimum DPD values.
  - Count of zero DPD records.
  - State-wise DPD summary.
- Automated email sending of the report to the recipient.
- Deployed on Heroku for easy access.

## Technologies Used
- Python
- Django
- Pandas (for data processing)
- Openpyxl (for reading Excel files)
- SMTP (for sending email)
- HTML/CSS (for frontend templates)

## Installation and Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/DevTest.git
    cd DevTest
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup environment variables:**
    Create a `.env` file in the root directory and add the following:
    ```plaintext
    EMAIL_HOST=smtp.your-email-host.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=your-email@example.com
    EMAIL_HOST_PASSWORD=your-email-password
    ```

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Run the server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000` to access the web interface.

## Usage

1. **Upload a file:** 
   Go to the file upload page, and choose an Excel/CSV file with columns `Cust State`, `Cust Pin`, and `DPD`. Submit the form.
   
2. **Generate a report:**
   After the file is uploaded, the summary report will be generated automatically and displayed on the success page.

3. **Email the report:**
   The report is automatically sent to the specified email (`vkorat50@gmail.com` or as per your code).

## Deployment

The project is deployed on Heroku and can be accessed via the following URL:

- **[DevTest on Heroku](https://your-heroku-app-url.herokuapp.com/)**

## Folder Structure

```plaintext
DevTest/
│
├── fileupload/               # Django app for file upload and report generation
│   ├── migrations/           # Database migrations
│   ├── static/               # Static files (CSS, JS, etc.)
│   ├── templates/            # HTML templates for views
│   ├── forms.py              # Django forms for file upload
│   ├── models.py             # Models for file handling
│   ├── urls.py               # URL routing for the app
│   └── views.py              # Views to handle file uploads, generate reports, and send email
│
├── DevTest/                  # Project configuration files
│   ├── settings.py           # Django settings (modify email credentials here)
│   ├── urls.py               # Project-wide URL configuration
│   └── wsgi.py               # WSGI configuration for deployment
│
├── media/                    # Directory for storing uploaded files
├── .env                      # Environment variables for email credentials
├── .gitignore                # Files to be ignored by Git
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── manage.py                 # Django management commands
