from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, DateTime, ForeignKey, Identity, Integer, Numeric, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# association table for the many-to-many relation between products and tags
products_tags = Table(
    "products_tags",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("product.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
)


class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    address: Mapped[str]
    orders: Mapped[list["Order"]] = relationship(back_populates="customer")

    def __repr__(self) -> str:
        return f"Customer(id={self.id}, name={self.name})"


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str]
    price: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    details: Mapped[list["OrderDetails"]] = relationship(back_populates="product")
    tags: Mapped[list["Tag"]] = relationship(back_populates="products", secondary=products_tags)

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name={self.name})"


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str]
    products: Mapped[list[Product]] = relationship(back_populates="tags", secondary=products_tags)

    def __repr__(self) -> str:
        return f"Tag(id={self.id}, name={self.name})"


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    number: Mapped[str] = mapped_column(String(10))
    time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    customer: Mapped[Customer] = relationship(back_populates="orders")
    details: Mapped[list["OrderDetails"]] = relationship(back_populates="order")

    def __repr__(self) -> str:
        return f"Order(id={self.id}, number={self.number})"


class OrderDetails(Base):
    __tablename__ = "order_details"

    # composite primary key: both columns are marked with primary_key=True
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), primary_key=True)
    quantity: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    order: Mapped[Order] = relationship(back_populates="details")
    product: Mapped[Product] = relationship(back_populates="details")

    def __repr__(self) -> str:
        return (
            f"OrderDetails(order={self.order_id}, product={self.product_id}, qty={self.quantity})"
        )


if __name__ == "__main__":
    from typing import cast

    from sqlalchemy.dialects import postgresql
    from sqlalchemy.schema import CreateTable

    print(CreateTable(cast("Table", Product.__table__)).compile(dialect=postgresql.dialect()))
