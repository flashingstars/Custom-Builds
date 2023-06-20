from app import app
import os
from flask import render_template, request, redirect, session, flash, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from .models import Base, User, Admin, Photo, AdminPhoto
from flask_login import login_required, LoginManager, current_user, login_user

# Set a secret key for session management
app.secret_key = 'my_secret_key'

# Create SQLite database engine and bind it to the session using a connection pool
engine = create_engine('sqlite:///custom_builds.db')
Session = scoped_session(sessionmaker(bind=engine))
db_session = Session
Base.metadata.create_all(bind=engine)

# Flask-Login initialization
login_manager = LoginManager()
login_manager.init_app(app)

# Configuration for  the login view
login_manager.login_view = 'login'

#Define the user_loader function and register it with Flask-Login
@login_manager.user_loader
def load_user(user_id):
    #Load the user object based on the user ID
    return User.query.get(int(user_id))

@login_manager.user_loader
def load_admin(admin_id):
	# Load the Admin object based on the admin ID
	return Admin.query.get(int(admin_id))

# Define the request_loader function and register it with Flask-Login
@login_manager.request_loader
def load_user_from_request(request):
    # Load the user object based on the request data
    user_id = request.headers.get("Authorization")
    if user_id:
        return User.query.get(int(user_id))
    return None

@login_manager.request_loader
def load_admin_from_request(request):
	# Load the admin object based on the request data
	admin_id = request.headers.get("Authorization")
	if admin_id:
		return Admin.query.get(int(admin_id))
	return None

# Defining route handlers
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# Handle login form submission
		email = request.form['email']
		password = request.form['password']

		# Authenticating if the credentials belong to a user
		user = db_session.query(User).filter_by(email=email).first()
		if user and check_password_hash(user.password, password):
			flash('Login Successful')
			login_user(user) # Log in the user
			return redirect('/whatweoffer.html')
		
		flash('Invalid email or password')
		return redirect('/login.html')

		# Authenticating if the credentials belong to admin
		admin = db_session.query(Admin).filter_by(email=email).first()
		if admin and check_password_hash(admin.password, password):
			flash('Admin login succesful')
			login_user(admin) # Log in admin 
			return redirect('/whatweoffer.html')
		flash('Invalid email or password')
		return redirect('/login.html')
	
	# If request is 'GET'
	return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')
		role = Role.query.filter_by(name='user').first() # Get the user role

		# Creating a new User object with the form data
		new_user = User(username=username, email=email,password=password)

		# Hash the password before storing it in the database
		new_user.set_password = generate_password_hash(password)

		# Assign the role to the user
		new_user.roles.append(role)

		# Add the user to the database session
		db_session.add(new_user)
		db_session.commit()

		flash('Signup successful')

		return redirect('/whatweoffer.html')
	
	# Render the login form for GET request
	return render_template('signup.html')

@app.route('/whatweoffer')
@login_required
def whatweoffer():
    return render_template('whatweoffer.html')

# folder where photos will be saved
UPLOAD_FOLDER = '/app/static/images/admin_photos'

@app.route('/add_photo', methods=['POST'])
@login_required
def add_photo():
	if current_user.is_admin:
		section = request.form.get('section')
		photo_file = request.files['photo']
		heading = request.form.get('heading')
		description = request.form.get('description')
		price = float(request.form.get('price'))

		# Save the photo file to the upload folder
		filename = secure_filename(photo_file.filename)
		photo_file.save(os.path.join(UPLOAD_FOLDER, filename))

		# Create a new Photo object and save it to the database
		photo = Photo(name=filename, description=description, price=price)
		session.add(photo)
		session.commit()

		# Associate the photo with the corresponding section
		if section == 'On_offer':
			On_offer_photo = AdminPhoto(photo_id=photo.id, email=current_user.email)
			session.add(On_offer_photo)
		elif section == 'livingroom':
			livingroom_photo = AdminPhoto(photo_id=photo.id, email=current_user.email)
			session.add(livingroom_photo)
		elif section == 'dining':
			dining_photo = AdminPhoto(photo_id=photo.id, email=current_user.email)
			session.add(dining_photo)
		elif section == 'bedroom':
			bedroom_photo = AdminPhoto(photo_id=photo.id, email=current_user.email)
			session.add(bedroom_photo)
		elif section == 'outdoors':
			outdoors_photo = AdminPhoto(photo_id=photo.id, email=current_user.email)
			session.add(outdoors_photo)
		session.commit()

		flash('Photo added successfully')

		# Redirecting to the section page
		if section == 'On_offer':
			return redirect('/On_offer.html')
		elif section == "livingroom":
			return redirect('/livingroom.html')
		elif section == "dining":
			return redirect('/dining.html')
		elif section == "bedroom":
			return redirect('bedroom.html')
		elif section == "outdoors":
			return redirect('/outdoors.html')
	else:
		flash('You are not authorized to perform this action')
		return redirect('/whatweoffer.html')
	
@app.route('/On_offer')
def On_offer():
	photos = AdminPhoto.query.join(Photo).filter_by(id=AdminPhoto.photo_id).all()
	return render_template('On_offer.html', photos=photos)

@app.route('/livingroom')
def livingroom():
	photos = AdminPhoto.query.join(Photo).filter_by(id=AdminPhoto.photo_id).all()
	return render_template('livingroom.html', photos=photos)

@app.route('/dining')
def dining():
	photos = AdminPhoto.query.join(Photo).filter_by(id=AdminPhoto.photo_id).all()
	return render_template('dining.html', photos=photos)

@app.route('/bedroom')
def bedroom():
	photos = AdminPhoto.query.join(Photo).filter_by(id=AdminPhoto.photo_id).all()
	return render_template('bedroom.html', photos=photos)

@app.route('/outdoors')
def outdoors():
	photos = AdminPhoto.query.join(Photo).filter_by(id=AdminPhoto.photo_id).all()
	return render_template('outdoors.html', photos=photos)

@app.route('/contact_us')
@login_required
def contact_us():
	return render_template('whatweoffer.html')

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
	conn = sqlite.connect(custom_builds.db)
	c = conn.cursor()
	c.execute("INSERT INTO review Values (?, ?, ?)", (name, email, comment))
	conn.commit()
	conn.close()

	#redirect to customer stories page
	return redirect('/customer_stories.html')

@app.route('/customer_stories')
def customer_stories():
	# Fetching the submitted review from the database
	conn = sqlite.connect(custom_builds.db)
	c = conn.cursor()
	c.execute("SELECT * FROM reviews")
	reviews = c.fetchall()
	conn.close()

	return render_template('customer_stories.html', reviews=reviews)
