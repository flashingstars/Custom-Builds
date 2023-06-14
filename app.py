import os
import sqlite3
from flask import Flask, render_template, request, redirect, session, flash, url_for
from app.models import Base, User, Photo, Order, CustomerStory, Like, Admin, AdminPhoto, AdminOrder, Review
from sqlalchemy import sessionmaker, scoped_session
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, LoginManager, current_user, login_user

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods['GET', 'POST'])
def login():
	if request.method == 'POST':
		# Get the login information from the form
		email = request.form['email']
		password = request.form['password']

		# Authenticating if the credentials belong to admin
		admin = db_session.query(Admin).filter_by(email=email).first()
		if admin and check_password_hash(admin.password1, password):
			flash('Login succesful')
			login_user(admin) # Log in admin 
			return redirect('what_we_offer')

@app.route('/signup', methods=['POST'])
def signup():
	username = request.form.get('username')
	email = request.form.get('email')
	password = request.form.get('password')
	role = 'user' #Setting the role as user
@app.route('/whatweoffer')
@login_required
def whatweoffer():
    return render_template('/whatweoffer.html')

@app.route('/contact_us')
@login_required
def contact_us():
	return render_template('/whatweoffer.html')

@app.route('/custom_builds')
def custom_builds():
	return render_template('custom_builds.html')

@app.route('/review')
def review():
	return render_template('review.html')

@app.route('/submit', methods=['POST'])
def submit():
	# Retrieve form data
	name = request.form['username']
	email = request.form['email']
	comment = request.form['comment']

	# Store the comment in the database
	conn = sqlite3.connect()
	c = conn.cursor()
	c.execute("INSERT INTO review Values (?, ?, ?)", (name, email, comment))
	conn.commit()
	conn.close()

	#redirect to customer stories page
	return redirect('/customer_stories.html')

@app.route('/customer_stories')
def customer_stories():
	# Fetching the submitted review from the database
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	c.execute("SELECT * FROM reviews")
	reviews = c.fetchall()
	conn.close()

	return render_template('customer_stories.html', reviews=reviews)

# Run the app
if __name__ == '__main__':
	create_database()
	app.run(debug=True)
