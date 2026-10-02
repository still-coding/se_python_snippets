from collections.abc import Sequence
from typing import Any

from sqlalchemy import Row, func, select
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

from config import DATABASE_URI
from models import Customer, Order, OrderDetails, Product
from tools import get_session_engine


def execute_query(
    session: Session, query: Select[*tuple[Any, ...]], print_results: bool = False
) -> Sequence[Row[*tuple[Any, ...]]]:
    results = session.execute(query).all()
    if print_results:
        for result in results:
            print(result)
        print("\n")
    return results


if __name__ == "__main__":
    session_factory, _ = get_session_engine(DATABASE_URI)
    with session_factory() as session:
        execute_query(session, select(Customer), print_results=True)

        orders = select(Order, Customer).join(Order.customer)
        execute_query(session, orders, print_results=True)

        all_details = (
            select(Order, Product, OrderDetails.quantity)
            .join(OrderDetails, Order.id == OrderDetails.order_id)
            .join(Product, OrderDetails.product_id == Product.id)
        )
        execute_query(session, all_details, print_results=True)

        orders_total = (
            select(Order, func.sum(Product.price * OrderDetails.quantity))
            .join(OrderDetails, Order.id == OrderDetails.order_id)
            .join(Product, OrderDetails.product_id == Product.id)
            .group_by(Order.id)
            .order_by(Order.id)
        )
        results = execute_query(session, orders_total, print_results=True)
        _, first_total = results[0]
        print("First order total queried:", first_total)

        # the same with relationships: lazy loading issues extra queries
        first_order = session.scalars(select(Order).order_by(Order.id)).first()
        assert first_order is not None
        check_total = sum(d.product.price * d.quantity for d in first_order.details)
        print("First order total checked:", check_total)

        for product in session.scalars(select(Product)):
            print(product.name, product.tags)
