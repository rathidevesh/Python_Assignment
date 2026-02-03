# Employee Management System 🚀

A full-stack **Employee Management System** built using **FastAPI**, **MySQL**, and a simple **Bootstrap-based frontend**.  
This application provides complete **CRUD operations** (Create, Read, Update, Delete) for managing employee records.

---

## ✨ Features

- ➕ Add new employees  
- 📋 View all employees in a tabular format  
- ✏️ Edit existing employee details  
- 🗑️ Delete employees  
- ⚡ RESTful APIs using FastAPI  
- 🗄️ MySQL database integration  
- 🎨 Simple and responsive UI using Bootstrap  
- 🐳 Docker & Docker Compose support (multi-container)

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- MySQL

### Frontend
- HTML
- Bootstrap 5
- JavaScript (Fetch API)

### DevOps
- Docker
- Docker Compose
- Virtual Environment

---

## 📂 Project Structure

```text
employee_management/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   └── employee.py
│   ├── crud/
│   │   └── employee_crud.py
│   ├── routers/
│   │   └── employee_routes.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd employee_management

Create and Activate Virtual Environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

Install All Dependancies

pip install -r requirements.txt

Database Setup
CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(50),
    salary FLOAT
);

Update MySQL credentials in app/database.py:
Run the Application
uvicorn app.main:app --reload

Access:

Backend API:
👉 http://127.0.0.1:8000

Swagger API Docs:
👉 http://127.0.0.1:8000/docs

Frontend:
👉 Open index.html in browser
