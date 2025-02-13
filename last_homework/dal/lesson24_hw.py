import psycopg as pg
import product_dao
import employee_dao

class NorthwindRepository:
    def __init__(self, conn_info: str):
        self.conn = pg.connect(conninfo=conn_info)
        self.product_dao = product_dao.ProductDAO(self.conn)
        self.employee_dao = employee_dao.EmployeeDAO(self.conn)

    # def close_conn...
    #     self.conn.close()
       

    def update_price_for_product(self, id: int, price: float):
        self.product_dao.update_price_for_product(id, price)
        # self.product_dao.update_company_books(??)

repo = NorthwindRepository(conn_info="dbname=northwind user=postgres password=postgres")
# repo.update_price_for_product(1, 20)
repo.update_price_for_product(2, 20)