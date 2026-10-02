import asyncio
from datetime import datetime
from pathlib import Path
from random import choice, randint, sample

from piccolo.table import create_db_tables, drop_db_tables

from tables import Customer, Order, OrderDetails, Product, ProductTag, Tag

TABLES = (Customer, Product, Tag, ProductTag, Order, OrderDetails)


def read_csv(filename):
    path = Path(__file__).parent.parent / "static_data" / f"{filename}.csv"
    with open(path, encoding="utf-8") as f:
        result = [line.strip() for line in f if line.strip()]
    return [r.split(";") for r in result]


async def create_database():
    await drop_db_tables(*TABLES)
    await create_db_tables(*TABLES)


async def fill_db():
    customers = [Customer(name=c[0], address=c[1]) for c in read_csv("customers")]
    await Customer.insert(*customers)

    products = [Product(name=p[0], price=p[1]) for p in read_csv("products")]
    await Product.insert(*products)

    tags = [Tag(name=t[0]) for t in read_csv("tags")]
    await Tag.insert(*tags)

    # joining table rows are inserted directly: add_m2m() can't be used because
    # the foreign keys of ProductTag are NOT NULL
    product_ids = [p.id for p in await Product.objects()]
    product_tags = []
    for tag in await Tag.objects():
        for pid in sample(product_ids, randint(1, 10)):
            product_tags.append(ProductTag(product=pid, tag=tag.id))
    await ProductTag.insert(*product_tags)

    customer_ids = [c.id for c in await Customer.objects()]
    orders = [
        Order(
            customer=choice(customer_ids),
            number=str(i),
            time=datetime.fromtimestamp(1681655478 - randint(0, 10000000)),
        )
        for i in range(100)
    ]
    await Order.insert(*orders)

    details = []
    for order in await Order.objects():
        for pid in sample(product_ids, randint(1, 20)):
            details.append(
                OrderDetails(order=order.id, product=pid, quantity=randint(1, 10))
            )
    await OrderDetails.insert(*details)


async def main():
    print("connecting...")
    await create_database()
    print("db created!")
    await fill_db()
    print("db filled with data")


if __name__ == "__main__":
    asyncio.run(main())
