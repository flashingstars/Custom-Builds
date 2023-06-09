from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlqlchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __table__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    orders = relationship("Order", back_populates="user")
    user_stories = relationship("UserStory", back_populates="user")
    likes = relationship("Like", back_populates="user")

class Photo(Base):
    __tablename__ = 'photos'

    id = Column(integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    price = Column(Float, nullable=False)

    user_stories = relationship("UserStory", back_populates="photo")
    likes = relationship("Like", back_populates="photo")
    orders = relationsip("Order", back_populates="photo")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, Foreign_key('users.id'), nullable=False)
    product_id = Column(Integer, Foreign_key('photos.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_poulates="orders")
    photos = relationship("Photo", back_populates="orders")

class UserStory(Base):
    __tablename__ = 'user_stories'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    photo_id = Column(Integer, ForeignKey('photos.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(500))

    user = relationship("User", back_populates="user_stories")
    photos = relationship("Photo", back_populates="user_stories")

class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, Primary_Key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    photo_id = Column(Integer, ForeignKey('photos.id'), nullable=False)

    user = relationship("User", back_populates="likes")
    photos = relationship("Photo", back_populates="likes")

class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integr, primary_Key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(150), )

class AdminPhoto(Base):
    __tablename__ = 'admin_photos'

    id = Column(Integer, primary_Key=True)
    photo_id = Column(Integer, ForeignKey('photos.id'), nullable=False)
    email = Column(String(150), unique=True, nullable=False)

    admin = relationship("Admin")
    photo = relationship("Photo")