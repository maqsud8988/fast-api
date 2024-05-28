from sqlalchemy import Column, INTEGER, Integer, String, Text, ForeignKey,Boolean, Float, Numeric, NUMERIC
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import Choice
from database import Base
from sqlalchemy import Column, Integer, String, Boolean
from database import Base




class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=True)
    last_name = Column(String(20), nullable=True)
    username = Column(String(10), nullable=True)
    email = Column(Text, nullable=True)
    password = Column(String(20), nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    order = relationship("Order", back_populates="user")

    def __repr__(self):
        return self.first_name


class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    product = relationship('Product', back_populates='category')


class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='product')
    order = relationship("Order", back_populates="product")

class Order(Base):

    __tablename__ ='orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    user = relationship("User", back_populates="orders")
    product = relationship('Product', back_populates='orders')