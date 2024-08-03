# Online Ticketing Application

This repository contains an online ticketing application designed to manage and resolve hardware, software, and login access issues systematically in large organizations.

## Features

- User-friendly interface for submitting and tracking tickets
- Admin dashboard for managing and resolving tickets
- Static files for styling and scripts
- Template files for rendering web pages
- Pre-trained model for life expectancy prediction included as an example

## Prerequisites

- Python 3.10 or higher
- Django 3.2 or higher
- Required Python packages listed in `requirements.txt`

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/online-ticketing-application.git
    cd online-ticketing-application
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.
