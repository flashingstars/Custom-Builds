from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    permissions = relationship("Permission", back_populates="role")

class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)

    role = relationship('Role', back_populates="permissions")

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False) # Added role attribute

    role = relationship("Role", back_populates="users")
    orders = relationship("Order", back_populates="user")
    customer_stories = relationship("CustomerStory", back_populates="user")
    likes = relationship("Like", back_populates="user")

class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    price = Column(Float, nullable=False)

    like = relationship("Like", back_populates="photo")
    order = relationship("Order", back_populates="photo")
    admin_photo = relationship("AdminPhoto", back_populates="photo")

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    photo_id = Column(Integer, ForeignKey('photo.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="orders")
    photo = relationship("Photo", back_populates="order")
    admin_order = relationship = relationship("AdminOrder", back_populates="order")

class CustomerStory(Base):
    __tablename__ = 'Customer_story'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    comment = Column(String(10000), nullable=False)

    user = relationship("User", back_populates="customer_story")
    review = relationship("Review", back_populates="customer_story")

class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    photo_id = Column(Integer, ForeignKey('photo.id'), nullable=False)

    user = relationship("User", back_populates="likes")
    photo = relationship("Photo", back_populates="likes")

class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)

    role = relationship("Role", back_populates="admin")
    admin_photos = relationship("AdminPhoto", back_populates="admin")
    admin_orders = relationship("AdminOrder", back_populates="admin")

class AdminPhoto(Base):
    __tablename__ = 'admin_photo'

    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer, ForeignKey('photo.id'), nullable=False)
    admin_id = Column(Integer, ForeignKey('admin.id'), nullable=False)
    email = Column(String(150), unique=True, nullable=False)

    admin = relationship("Admin", back_populates="admin_photos")
    photo = relationship("Photo", back_populates="admin_photos")

class AdminOrder(Base):
    __tablename__ = 'admin_order'

    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer, ForeignKey('photo.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    admin_id = Column(Integer, ForeignKey('admin.id'), nullable=False)
    email = Column(String(150), unique=True, nullable=False)

    admin = relationship("Admin", back_populates="admin_orders")
    order = relationship("Order", back_populates="admin_orders")

class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    comment = Column(String(10000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship("User", back_populates="reviews")
