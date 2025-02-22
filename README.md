# Project Management API

## Overview
This is a REST API built using Django REST Framework (DRF) to manage projects, tasks, and employees.

## Installation

1. **Clone the Repository**
```bash
$ git clone https://github.com/your-repo/project-management-api.git
$ cd project-management-api
```

2. **Create Virtual Environment & Install Dependencies**
```bash
$ python -m venv venv
$ source venv/bin/activate   # On Windows: venv\Scripts\activate
$ pip install -r requirements.txt
```

3. **Run Migrations**
```bash
$ python manage.py migrate
```

4. **Run the Server**
```bash
$ python manage.py runserver
```

## API Endpoints

### Employee Endpoints
- GET `/api/employees/` - Get all employees
- POST `/api/employees/` - Create a new employee
- GET `/api/employees/{id}/` - Get details of an employee
- PUT `/api/employees/{id}/` - Update an employee
- DELETE `/api/employees/{id}/` - Delete an employee

### Project Endpoints
- GET `/api/projects/` - Get all projects
- POST `/api/projects/` - Create a new project
- GET `/api/projects/{id}/` - Get project details with tasks
- PUT `/api/projects/{id}/` - Update a project
- DELETE `/api/projects/{id}/` - Delete a project

### Task Endpoints
- GET `/api/tasks/` - Get all tasks
- POST `/api/tasks/` - Create a new task
- GET `/api/tasks/{id}/` - Get details of a task
- PUT `/api/tasks/{id}/` - Update a task (e.g., assign employees)
- DELETE `/api/tasks/{id}/` - Delete a task

## Postman Testing Demo

### Importing the Postman Collection
1. **Download the Postman Collection JSON file** (provided below).
2. Open **Postman**.
3. Click **Import** → Select the JSON file → Click **Open**.
4. The collection will appear in **Postman** under "Collections."

### Sample API Requests Using Postman

#### 1. Create an Employee (POST)
- **Endpoint:** `POST http://localhost:8000/api/employees/`
- **Body (JSON):**
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "position": "Software Engineer"
  }
  ```

#### 2. Create a Project (POST)
- **Endpoint:** `POST http://localhost:8000/api/projects/`
- **Body (JSON):**
  ```json
  {
    "name": "EV Charging Station Management"
  }
  ```

#### 3. Create a Task (POST)
- **Endpoint:** `POST http://localhost:8000/api/tasks/`
- **Body (JSON):**
  ```json
  {
    "title": "Develop API for station data",
    "description": "Create REST APIs for fetching station details",
    "project": 1,
    "employee_ids": [1, 3]
  }
  ```

#### 4. Get All Employees (GET)
- **Endpoint:** `GET http://localhost:8000/api/employees/`

#### 5. Get All Projects (GET)
- **Endpoint:** `GET http://localhost:8000/api/projects/`

#### 6. Get All Tasks (GET)
- **Endpoint:** `GET http://localhost:8000/api/tasks/`

## Author
- **Sreejith S** - [GitHub](https://github.com/sreejith-0087)

