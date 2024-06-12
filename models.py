from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class UserRole(PyEnum):
    USER = "User"
    ADMIN = "Admin"

class OrderStatus(PyEnum):
    PENDING = "Pending"
    PROCESSED = "Processed"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"

class User(Base):
    __tablename__ = 'users'  # Specify the table name for User model
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)

    # Relationships
    cart_items = relationship('CartItem', back_populates='user')
    orders = relationship('Order', back_populates='user')

class Product(Base):
    __tablename__ = 'products'  # Specify the table name for Product model
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    # Relationships
    cart_items = relationship('CartItem', back_populates='product')

class CartItem(Base):
    __tablename__ = 'cart_items'  # Specify the table name for CartItem model
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    # Relationships
    user = relationship('User', back_populates='cart_items')
    product = relationship('Product', back_populates='cart_items')

class Order(Base):
    __tablename__ = 'orders'  # Specify the table name for Order model
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship('User', back_populates='orders')
    order_items = relationship('OrderItem', back_populates='order')

class OrderItem(Base):
    __tablename__ = 'order_items'  # Specify the table name for OrderItem model
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

    # Relationships
    order = relationship('Order', back_populates='order_items')
    product = relationship('Product')

# No need to create engine and sessionmaker here; handle these in your main script
