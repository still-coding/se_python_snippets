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
    product = ForeignKey(Product)
    tag = ForeignKey(Tag)


class Order(Table):
    customer = ForeignKey(Customer)
    number = Varchar(length=10)
    time = Timestamp()


# Piccolo has no composite primary keys: the table gets a surrogate `id`.
class OrderDetails(Table):
    order = ForeignKey(Order)
    product = ForeignKey(Product)
    quantity = Numeric(digits=(8, 2))
