from flask import Flask, request
import smtplib

app = Flask(__name__)


@app.route("/form", methods=["POST", "GET"])
def submitting():

    if request.method == "POST":
        # this is how you access the input fields in form, the part you want to extract (["name"]) should be the value of the name attribute of the in put in html
        json_data = request.get_json(force=True)
        user = json_data["name"]
        mail = json_data["email"]
        ms = json_data["message"]
        # your mail template
        content = f"<h1>    This is from your website form:  </h1> \n<h1> Name: {user} </h1>\n<h1> Email: {mail} </h1> \n <p>Message: {ms}</p>"


    #each email provider has a different smtp protocol you may need to change the code below
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("YOUR_EMAIL@gmail.com", "YOUR_EMAIL_PASSWORD")
        server.sendmail("YOUR_EMAIL@gmail.com", "RECIVE_THE_MAIL_HERE@gmail.com", content)
        return ""
    else:
        user = request.args.get("name")
        return f"<h1>you're not conected/ {request.args}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
