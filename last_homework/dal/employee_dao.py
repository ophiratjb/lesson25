import psycopg as pg

class EmployeeDAO:
    def __init__(self, conn: pg.Connection):
        self.db_conn = conn

    def delete_employee_by_id(self, id: int):
        with self.db_conn.cursor() as cursor:
            ...
            self.db_conn.commit()