from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            server_email = os.getenv('EMAIL')
            server_pass = os.getenv('PASSWORD')
            admin_email = os.getenv('ADMIN_EMAIL')
            connection.login(server_email, server_pass)
            connection.sendmail(from_addr=server_email,
                                to_addrs=admin_email,
                                msg="Subject: New Message From Portfolio Website\n\n"
                                    f"Name: {data['name']}\n"
                                    f"Email: {data['email']}\n"
                                    f"Subject: {data['subject']}\n"
                                    f"Message: {data['message']}\n")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

