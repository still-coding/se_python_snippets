import asyncio

from tables import Customer, Order, OrderDetails, Product, Tag


def show(title, rows):
    print(title)
    for row in rows:
        print(row)
    print("\n")


async def main():
    show("customers:", await Customer.select())

    # join through a foreign key: Order.customer.name
    show("orders with customers:", await Order.select(Order.all_columns(), Order.customer.name))

    show(
        "order details:",
        await OrderDetails.select(
            OrderDetails.order.number,
            OrderDetails.product.name,
            OrderDetails.quantity,
        ),
    )

    # Piccolo can't multiply two columns inside Sum(), so this one is raw SQL
    orders_total = await OrderDetails.raw(
        """
        SELECT o.number, SUM(p.price * d.quantity) AS total
        FROM order_details d
        JOIN "order" o ON d.order = o.id
        JOIN product p ON d.product = p.id
        GROUP BY o.id ORDER BY o.id
        """
    )
    show("orders totals:", orders_total)

    # the same with objects
    first_order = await Order.objects().order_by(Order.id).first()
    details = await OrderDetails.objects(OrderDetails.product).where(
        OrderDetails.order == first_order.id
    )
    check_total = sum(d.product.price * d.quantity for d in details)
    print("First order total queried:", orders_total[0]["total"])
    print("First order total checked:", check_total)

    # M2M: every product with the list of its tag names
    show(
        "products and tags:",
        await Product.select(Product.name, Product.tags(Tag.name, as_list=True)),
    )


if __name__ == "__main__":
    asyncio.run(main())
