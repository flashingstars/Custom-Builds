from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/signup/login')
def login():
	return render_template('login.html')

@app.route('/whatweoffer')
def whatweoffer():
        return render_template('/whatweoffer.html')

@app.route('/contact_us')
def contact_us():
	return render_template('/whatweoffer.html')

@app.route('/custom_builds')
def custom_builds():
	return render_template('custom_builds.html')

@app.route('customer_stories')
def customer_stories():
	return render_template('customer_stories.html')


# Run the app
if __name__ == '__main__':
	app.run()
