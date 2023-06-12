from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False) # Added role attribute

    orders = relationship("Order", back_populates="user")
    user_stories = relationship("CustomerStory", back_populates="user")
    likes = relationship("Like", back_populates="user")

class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    price = Column(Float, nullable=False)

    likes = relationship("Like", back_populates="photo")
    orders = relationship("Order", back_populates="photo")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('photos.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    order_date = Column(datetime, default=datetime.utcnow)

    users = relationship("User", back_poulates="orders")
    photos = relationship("Photo", back_populates="orders")

class CustomerStory(Base):
    __tablename__ = 'Customer_stories'

    id = Column(Integer, primary_key=True)
    reviews_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    username = Column(String(150), uniue=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    comment = Column(String(10,000), nullable=False)

    user = relationship("User", back_populates="customer_stories")
    reviews = relationship("Review", back_populates="customer_stories")

class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, Primary_Key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    photo_id = Column(Integer, ForeignKey('photos.id'), nullable=False)

    user = relationship("User", back_populates="likes")
    photos = relationship("Photo", back_populates="likes")

class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_Key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    role = Column(String(20), nullable=False, default="admin")

class AdminPhoto(Base):
    __tablename__ = 'admin_photos'

    id = Column(Integer, primary_Key=True)
    photo_id = Column(Integer, ForeignKey('photos.id'), nullable=False)
    email = Column(String(150), unique=True, nullable=False)

    admin = relationship("Admin", back_populates="admin_photos")
    photo = relationship("Photo", back_populates="admin_photos")

class AdminOrder(Base):
    __tablename__ = 'admin_orders'

    id = Column(Integer, primary_Key=True)
    photo_id = Column(Integer, ForeignKey('photos.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    email = Column(String(150), unique=True, nullable=False)

    admin = relationship("Admin", back_populates="admin_orders")
    order = relationship("Order", back_populates="admin_orders")




class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_Key=True)
    username = Column(String(150), uniue=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    comment = Column(String(10000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    users = relationship("User", back_populates="reviews")

