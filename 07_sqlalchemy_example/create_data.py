from datetime import datetime
from random import choice, randint, sample

from tools import create_database
from sqlalchemy import select

from config import DATABASE_URI
from model import Customer, Order, OrderDetails, Product



def fill_db(sess):
    def read_csv(filename):
        with open(f"./static_data/{filename}.csv", "r") as f:
            result = [line.strip() for line in f]
        return [r.split(";") for r in result]

    customers = read_csv("customers")
    products = read_csv("products")

    with sess() as session, session.begin():
        for c in customers:
            cust = Customer(name=c[0], address=c[1])
            session.add(cust)

        for p in products:
            prod = Product(name=p[0], price=p[1])
            session.add(prod)

    with sess() as session, session.begin():
        cust_ids = [c.id for c in session.scalars(select(Customer)).all()]
        for i in range(100):
            order = Order(
                customer_id=choice(cust_ids),
                number=str(i),
                time=datetime.fromtimestamp(1681655478 - randint(0, 10000000)),
            )
            session.add(order)

    with sess() as session, session.begin():
        order_ids = [o.id for o in session.scalars(select(Order)).all()]
        product_ids = [p.id for p in session.scalars(select(Product)).all()]
        for oid in order_ids:
            order_pids = sample(product_ids, randint(1, 20))
            for pid in order_pids:
                det = OrderDetails(
                    order_id=oid, product_id=pid, quantity=randint(1, 10)
                )
                session.add(det)


if __name__ == "__main__":
    print("connecting...")
    session = create_database(DATABASE_URI)
    print("connection established")
    print("db created!")

    fill_db(session)
    print("db filled with data")
    
    session().close()

    print("session closed")
