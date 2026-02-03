from app.database import get_db_connection

def create_employee(emp):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, email, department, salary) VALUES (%s,%s,%s,%s)",
        (emp.name, emp.email, emp.department, emp.salary)
    )
    conn.commit()
    conn.close()

def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    conn.close()
    return result

def update_employee(emp_id, salary):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET salary=%s WHERE id=%s",
        (salary, emp_id)
    )
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    conn.commit()
    conn.close()
