from flask import Flask, jsonify, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# should move a lot of this into a settings file to protect the password
app.config['MAIL_SERVER']='mail.privateemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'trevor@rememberthee.com'
app.config['MAIL_PASSWORD'] = 'PASSWORD'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/sign-up", methods=['POST'])
def sign_up():
	try:
		data = request.get_json()
		subject = "User Sign Up: " + data['name']
		message = Message(subject, sender="trevor@rememberthee.com", recipients=["trevor@rememberthee.com"])
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

