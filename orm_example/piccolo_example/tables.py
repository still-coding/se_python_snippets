from piccolo.columns import (
    ForeignKey,
    Integer,
    LazyTableReference,
    Numeric,
    Text,
    Timestamp,
    Varchar,
)
from piccolo.columns.m2m import M2M
from piccolo.constraints import Check, Unique
from piccolo.table import Table


class Customer(Table):
    name = Varchar(length=50)
    address = Text()


class Product(Table):
    name = Text()
    price = Numeric(digits=(8, 2))
    tags = M2M(LazyTableReference("ProductTag", module_path=__name__))


class Tag(Table):
    name = Text()
    products = M2M(LazyTableReference("ProductTag", module_path=__name__))


# joining table for the many-to-many relation
class ProductTag(Table):
    product = ForeignKey(Product, null=False)
    tag = ForeignKey(Tag, null=False)

    unique_product_tag = Unique([product, tag])


class Order(Table):
    customer = ForeignKey(Customer, null=False)
    number = Varchar(length=10)
    time = Timestamp()


# Piccolo has no composite primary keys, so the table keeps a surrogate `id`
# and the (order, product) pair is protected with a composite UNIQUE constraint.
class OrderDetails(Table):
    order = ForeignKey(Order, null=False)
    product = ForeignKey(Product, null=False)
    quantity = Numeric(digits=(8, 2))

    unique_order_product = Unique([order, product])
    check_quantity_positive = Check(quantity > 0)
