from flask import Flask, jsonify, render_template, request
from flask_mail import Mail, Message

import settings

app = Flask(__name__)

# should move a lot of this into a settings file to protect the password
app.config['MAIL_SERVER'] = settings.MAIL_SERVER
app.config['MAIL_PORT'] = settings.MAIL_PORT
app.config['MAIL_USERNAME'] = settings.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = settings.MAIL_PASSWORD
app.config['MAIL_USE_SSL'] = settings.MAIL_USE_SSL

mail = Mail(app)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/sign-up", methods=['POST'])
def sign_up():
	try:
		data = request.get_json()
		subject = "User Sign Up: " + data['name']
		message = Message(subject, sender="michael.yaacoub7@gmail.com", recipients=["michael.yaacoub7@gmail.com"])
		message.html = """
		<ul>
			<li>Name: {name}</li>
			<li>Email: {email}</li>
			<li>Message: {message}</li>
			<li>Browser: {browser}</li>
		</ul>
		""".format(**data)
		mail.send(message)
	except Exception as e:
		# would be great to have logs here
		pass
	finally:
		return jsonify(success=True)

