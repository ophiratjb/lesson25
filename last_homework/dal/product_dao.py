import psycopg as pg
import models.product

class ProductDAO:
    def __init__(self, conn: pg.Connection):
        self.db_conn = conn

    def update_price_for_product(self, id: int, price: float):
        with self.db_conn.cursor() as cursor:
            cursor.execute("UPDATE products SET unit_price = %s WHERE product_id = %s", (price, id))
            self.db_conn.commit()

    def get_product_by_id(self, id: int):
        ...
        p1 = models.product.Product(id=id)
        p2 = models.product.Product(id=id)
        p3 = models.product.Product(id=id)

        return models.product.Product(id=id)