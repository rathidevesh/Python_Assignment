from fastapi import APIRouter
from app.models.employee import Employee
from app.crud.emp_crud import (
    create_employee,
    get_employees,
    update_employee,
    delete_employee
)
from app.database import get_db_connection

router = APIRouter()



@router.post("/employees")
def add_employee(emp: Employee):
    create_employee(emp)
    return {"message": "Employee added"}

@router.get("/employees")
def fetch_employees():
    return get_employees()

@router.put("/employees/{emp_id}")
def update_employee_api(emp_id: int, emp: Employee):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE employees
        SET name=%s, email=%s, department=%s, salary=%s
        WHERE id=%s
        """,
        (emp.name, emp.email, emp.department, emp.salary, emp_id)
    )
    conn.commit()
    conn.close()
    return {"message": "Employee updated successfully"}



@router.delete("/employees/{id}")
def remove_employee(id: int):
    delete_employee(id)
    return {"message": "Employee deleted"}
