from flask import Flask, request, render_template, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/festivals')
def festivals():
    return render_template('festivals.html')


@app.route('/cuisine')
def cuisine():
    return render_template('cuisine.html')


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Email to yourself
    msg_to_me = Message(
        subject=f"Feedback from {name}",
        sender=email,
        recipients=['bhavya.khatri@gmail.com'],
        body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
    )
    mail.send(msg_to_me)

    # Email copy to the user
    msg_to_user = Message(
        subject="Copy of Your Feedback - Indian Culture & Heritage",
        sender='india.heritage657@gmail.com',
        recipients=[email],
        body=f"Thank you, {name}, for your feedback!\n\nYour message:\n{message}"
    )
    mail.send(msg_to_user)

    return redirect(url_for('feedback'))


if __name__ == '__main__':
    app.run(debug=True)
