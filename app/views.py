from app import app
from flask import render_template, request, redirect, session, flash, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Base, User, Photo, Order, CustomerStory, Like, Admin, AdminPhoto, Review
from flask_login import login_required, LoginManager, current_user, login_user

# Secret key for session management
app.secret_key = 'secret_key'

# Flask login initialization
login_manager = LoginManager()
login_manager.init_app(app)

# Setting up the login page's configuration
login_manager.login_view = 'login'

# create SQLite database and bind it to the session using a connection pool
engine = create_engine('sqlite:///custom_builds.db')
Session = scoped_session(sessionmaker(bind=engine))
db_session = Session

# Creating a new user
new_user = User(username=username, email=email, password=password, role=role)
session.add(new_user)
session.commit()

return 'User created successfully' # For debugging purposes

session.close()

# User loader function
@login_manager.user_loader
def load_user(user_id):
    # Loading the user object from the database based on the given user id
    return db_session.query(User).get(user_id)

