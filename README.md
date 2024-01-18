# Django Learning Project

This is a learning project where I'm building a web application using Django and Docker.

## Project Overview

This project is a simple e-commerce website where users can view products, add them to their cart, and checkout. The website also includes user registration and login functionality.

## Technologies Used

- Django: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- Docker: A platform to develop, ship, and run applications inside containers.

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

- `Dockerfile`: Contains the Docker instructions to build the image.
- `requirements.txt`: Contains the Python dependencies for the project.
- `manage.py`: Django's command-line utility for administrative tasks.

## Learning Points

This project is a great opportunity to learn about:

- Developing web applications with Django.
- Using Docker for development and deployment.
- Working with databases and Django's ORM.
- User authentication in Django.
