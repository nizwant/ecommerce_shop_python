# Django Learning Project

This is my first time building a web application. I'm using this learning project to familiarize myself with various technologies including Django, Docker, HTML, CSS, and JavaScript.

## Project Overview

This project is a simple e-commerce website where users can view products, add them to their cart, and checkout. The website also includes user registration and login functionality.

## Technologies Used

- Django: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- Docker: A platform to develop, ship, and run applications inside containers.
- HTML: The standard markup language for documents designed to be displayed in a web browser.
- CSS: A style sheet language used for describing the look and formatting of a document written in HTML.
- JavaScript: Used sparingly to add interactivity to the web pages.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and learning purposes.

### Prerequisites

- Docker installed on your machine.

### Installation

1. Clone the repository
2. Build the Docker image:

    ```bash
    docker build -t your-image-name .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 8000:8000 your-image-name
    ```

The application will be available at `http://localhost:8000`.

## Project Structure

- `Dockerfile`: This file contains the Docker instructions to build the Docker image for the project. It specifies the base Python image, installs the requirements, runs Django migrations, and starts the Django server.

- `requirements.txt`: This file lists the Python dependencies that your project needs to run. When building the Docker image, these dependencies are installed using pip.

- `manage.py`: This is Django's command-line utility for administrative tasks. It's used in the Dockerfile to run migrations and start the Django server.


## Learning Points

This project is a great opportunity to learn about:

- Developing web applications with Django.
- Using Docker for development and deployment.
- Working with databases and Django's ORM.
- User authentication in Django.
- Basic HTML for structuring web pages.
- CSS for styling the web pages.
- Using JavaScript to add interactivity to the web pages.
