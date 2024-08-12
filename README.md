# Microservices with Django: Authentication and Notification Services

## Overview

This project demonstrates a simple microservices architecture using Django. It consists of two services:

1. **Authentication Service**: Handles user registration and login, and issues authentication tokens.
2. **Notification Service**: Sends OTPs to users' phone numbers, verifying their authentication tokens with the Authentication Service.

## Prerequisites

- Docker and Docker Compose
- Git

## Setup Instructions

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

Build and run the Docker containers using Docker Compose:

```bash
docker-compose up --build
```

This command will build the necessary Docker images and start the following services:

- **auth_service**: Authentication service running on `http://localhost:8001`.
- **notification_service**: Notification service running on `http://localhost:8002`.
- **celery_worker**: Celery worker for handling asynchronous tasks.
- **redis**: Redis server used by Celery for task queuing.
- **postgres_db**: PostgreSQL database for storing user data.

## API Endpoints

### Authentication Service

- **Signup**
  - **URL**: `POST /auth/signup/`
  - **Body**:
    ```json
    {
      "username": "your_username",
      "email": "your_email@example.com",
      "password": "your_password"
    }
    ```
  - **Response**:
    ```json
    {
      "token": "your_auth_token"
    }
    ```

- **Login**
  - **URL**: `POST /auth/login/`
  - **Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - **Response**:
    ```json
    {
      "token": "your_auth_token"
    }
    ```

### Notification Service

- **Request OTP**
  - **URL**: `POST /notify/send-otp/`
  - **Headers**:
    ```
    Authorization: Token your_auth_token
    ```
  - **Body**:
    ```json
    {
      "phone_number": "+1234567890"
    }
    ```
  - **Response**:
    ```json
    {
      "message": "OTP is being sent to your phone number"
    }
    ```

## Running Migrations

After the services are up, you need to run migrations for the Django apps:

```bash
docker-compose exec auth_service python manage.py migrate
docker-compose exec notification_service python manage.py migrate
```

## Running Tests

To run the test cases, use the following command:

```bash
docker-compose exec auth_service python manage.py test
docker-compose exec notification_service python manage.py test
```

## Stopping the Services

To stop the services, use:

```bash
docker-compose down
```