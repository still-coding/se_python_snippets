from datetime import UTC, datetime
from pathlib import Path
from random import choice, randint, sample

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from config import DATABASE_URI
from models import Customer, Order, OrderDetails, Product, Tag
from tools import create_database

STATIC_DATA = Path(__file__).parent.parent / "static_data"


def read_csv(filename: str) -> list[list[str]]:
    with open(STATIC_DATA / f"{filename}.csv", encoding="utf-8") as f:
        return [line.strip().split(";") for line in f if line.strip()]


def fill_db(session_factory: sessionmaker[Session]) -> None:
    # `sessionmaker.begin()` opens a session and a transaction: commit on exit, rollback on error
    with session_factory.begin() as session:
        session.add_all(
            Customer(name=name, address=address) for name, address in read_csv("customers")
        )
        products = [Product(name=name, price=price) for name, price in read_csv("products")]
        session.add_all(products)
        session.add_all(
            Tag(name=name, products=sample(products, randint(1, 10)))
            for (name,) in read_csv("tags")
        )

    with session_factory.begin() as session:
        customer_ids = session.scalars(select(Customer.id)).all()
        session.add_all(
            Order(
                customer_id=choice(customer_ids),
                number=str(i),
                time=datetime.fromtimestamp(1681655478 - randint(0, 10000000), tz=UTC),
            )
            for i in range(100)
        )

    with session_factory.begin() as session:
        order_ids = session.scalars(select(Order.id)).all()
        product_ids = session.scalars(select(Product.id)).all()
        for order_id in order_ids:
            session.add_all(
                OrderDetails(order_id=order_id, product_id=product_id, quantity=randint(1, 10))
                for product_id in sample(product_ids, randint(1, 20))
            )


if __name__ == "__main__":
    print("connecting...")
    session_factory = create_database(DATABASE_URI)
    print("db created!")

    fill_db(session_factory)
    print("db filled with data")
