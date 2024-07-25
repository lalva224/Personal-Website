from flask import Flask, render_template, request, redirect, url_for
from mailersend import emails
app = Flask(__name__)

@app.route('/send-email')
def send_email(name,email):
    
    # assigning NewEmail() without params defaults to MAILERSEND_API_KEY env var
    mailer = emails.NewEmail()

    # define an empty dict to populate with mail values
    mail_body = {}

    mail_from = {
        "name": name,
        "email": email,
    }

    recipients = [
        {
            "name": "Leandro Alvarez",
            "email": "alvarezleandro720@gmail.com",
        }
    ]

    reply_to = {
        "name": "Name",
        "email": "reply@domain.com",
    }

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("Hello!", mail_body)
    mailer.set_html_content("This is the HTML content", mail_body)
    mailer.set_plaintext_content("This is the text content", mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    # using print() will also return status code and data
    mailer.send(mail_body)

if __name__ == '__main__':
    app.run(debug=True)