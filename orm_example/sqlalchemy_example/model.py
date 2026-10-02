from sqlalchemy import ForeignKey, Identity, Table, Column
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy.types import DateTime, Integer, Numeric, String


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = 'customer'
    id = mapped_column(Integer, Identity(), primary_key=True)
    name = mapped_column(String(50), nullable=False)
    address = mapped_column(String, nullable=False)
    orders = relationship('Order', back_populates='customer')

    def __repr__(self):
        return f'Customer(id={self.id}, name={self.name})'

products_tags = Table(
    "products_tags",
    Base.metadata,
    Column("product_id", ForeignKey("product.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True)
)

class Product(Base):
    __tablename__ = 'product'
    id = mapped_column(Integer, Identity(), primary_key=True)
    name = mapped_column(String, nullable=False)
    price = mapped_column(Numeric(8, 2), nullable=False)
    details = relationship('OrderDetails', back_populates='product')
    tags = relationship('Tag', back_populates='products', secondary=products_tags)
    def __repr__(self):
        return f'Product(id={self.id}, name={self.name})'


class Tag(Base):
    __tablename__ = 'tag'
    id = mapped_column(Integer, Identity(), primary_key=True)
    name = mapped_column(String, nullable=False)
    products = relationship('Product', back_populates='tags', secondary=products_tags)
    def __repr__(self):
        return f'Tag(id={self.id}, name={self.name})'


class Order(Base):
    __tablename__ = 'order'
    id = mapped_column(Integer, Identity(), primary_key=True)
    customer_id = mapped_column(Integer, ForeignKey('customer.id'), nullable=False)
    number = mapped_column(String, nullable=False)
    time = mapped_column(DateTime, nullable=False)
    customer = relationship('Customer', back_populates='orders')
    details = relationship('OrderDetails', back_populates='order')
    
    def __repr__(self):
        return f'<Order: id={self.id}, number={self.number}>'


class OrderDetails(Base):
    __tablename__ = 'order_details'
    order_id = mapped_column(Integer, ForeignKey("order.id"), primary_key=True)
    product_id = mapped_column(Integer, ForeignKey("product.id"), primary_key=True)
    quantity = mapped_column(Numeric(8, 2), nullable=False)
    order = relationship("Order", back_populates="details")
    product = relationship("Product", back_populates="details")

    def __repr__(self):
        return f'<Details: order={self.order_id}, product={self.product_id}, qty={self.quantity}>'



if __name__ == '__main__':
    from sqlalchemy.schema import CreateTable
    print(CreateTable(Customer.__table__))
