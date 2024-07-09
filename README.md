# File Transformer

## Overview

This project is a standalone Django application designed to transform unstructured Excel files into a structured format using a predefined mapping file. The application allows users to upload input files, process them using a master mapping file, and generate a structured output file that can be downloaded. Additionally, a plot of a chosen parameter from the generated output file is displayed on the frontend.

## Features

- **File Upload**: Upload unstructured input Excel files (`input1.xlsx`, `input2.xlsx`) through the frontend.
- **Data Transformation**: Use `master.xlsx` (stored in the backend) for transforming the input files.
- **Output Generation**: Generate a structured output Excel file (`Output.xlsx`) that can be downloaded.
- **Data Visualization**: Display a plot of a chosen parameter from the generated output file.
- **Database Integration**: Use Django Models to create a data table in the default SQLite database.

## Requirements

- Python 3.x
- Django 3.x or higher
- Pandas
- Matplotlib

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/file_transformation.git
   cd file_transformation
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the Django Development Server**
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the Application**
   Open a web browser and navigate to `http://127.0.0.1:8000`.

2. **Upload Input Files**
   Use the provided interface to upload `input1.xlsx` and/or `input2.xlsx`.

3. **Generate Output File**
   Click the button to process the input files. The application will use `master.xlsx` to transform the data and generate `Output.xlsx`.

4. **Download Output File**
   The processed output file will be available for download.

5. **View Data Visualization**
   A plot of a chosen parameter from the output file will be displayed on the frontend.

## Project Structure

```
file_transformation/
│
├── manage.py
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── styles.css
│   └── migrations/
│       └── __init__.py
├── media/
│   ├── input1.xlsx
│   ├── input2.xlsx
│   └── master.xlsx
└── db.sqlite3
```
