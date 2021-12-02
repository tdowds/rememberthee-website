from flask import Flask, jsonify, render_template, request
from flask_mail import Mail, Message

import settings

app = Flask(__name__)

app.config['MAIL_SERVER'] = settings.MAIL_SERVER
app.config['MAIL_PORT'] = settings.MAIL_PORT
app.config['MAIL_USERNAME'] = settings.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = settings.MAIL_PASSWORD
app.config['MAIL_USE_SSL'] = settings.MAIL_USE_SSL

mail = Mail(app)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/get-remember-thee", methods=['POST'])
def get_remember_thee():
	return jsonify(success=True)

@app.route("/pray", methods=['POST'])
def pray():
	return jsonify(success=True)

@app.route("/sign-up", methods=['POST'])
def sign_up():
	data = request.get_json()
	subject = "User Sign Up: " + data['firstName'] + " " + data['lastName']
	message = Message(subject, sender="trevor@rememberthee.com", recipients=["trevor@rememberthee.com"])
	message.html = """
	<ul>
		<li>First Name: {firstName}</li>
		<li>Last Name: {lastName}</li>
		<li>Email: {email}</li>
		<li>Message: {message}</li>
		<li>Browser: {browser}</li>
	</ul>
	""".format(**data)
	mail.send(message)

	subject= "Thank you for signing up for Remember Thee"
	message = Message(subject, sender='trevor@rememberthee.com', recipients=[data['email']])
	message.html = render_template('welcome_email.html', firstName=data['firstName'])
	mail.send(message)

	return jsonify(success=True)

@app.route("/share", methods=['POST'])
def share():
	return jsonify(success=True)
