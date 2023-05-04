from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import ForeignKey, Identity
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import Numeric, String


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = 'customer'
    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    orders: Mapped[List['Order']] = relationship('Order', back_populates='customer')

    def __repr__(self):
        return f'Customer(id={self.id}, name={self.name})'

class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    details: Mapped[List['OrderDetails']] = relationship('OrderDetails', back_populates='product')
    def __repr__(self):
        return f'Product(id={self.id}, name={self.name})'

class Order(Base):
    __tablename__ = 'order'
    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customer.id'))
    number: Mapped[str] = mapped_column(String(10))
    time: Mapped[datetime] = mapped_column()
    customer: Mapped['Customer'] = relationship('Customer', back_populates='orders')
    details: Mapped[List['OrderDetails']] = relationship('OrderDetails', back_populates='order')
    def __repr__(self):
        return f'<Order: id={self.id}, number={self.number}>'


class OrderDetails(Base):
    __tablename__ = 'order_details'
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), primary_key=True)
    quantity: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    order: Mapped['Order'] = relationship("Order", back_populates="details")
    product: Mapped['Product'] = relationship("Product", back_populates="details")

    def __repr__(self):
        return f'<Details: order={self.order_id}, product={self.product_id}, qty={self.quantity}>'



if __name__ == '__main__':
    from sqlalchemy.dialects import postgresql, sqlite
    from sqlalchemy.schema import CreateTable
    print(CreateTable(Product.__table__).compile(dialect=sqlite.dialect()))
