from flask import request
from flask import render_template
from app.models.AuthModel import authmodel
from app.helpers.utils import send_response


class HomeController:
    def __init__(self):
        pass

    def index(self):
        user = {"nickname": "Tigran"}
        return render_template("index.html", title="Home", user=user)

    def register(self):
        return render_template("registration.html", title="Registration")

    def registeruser(self):
        _firstname = request.form.get("firstname", "")
        _lastname = request.form.get("lastname", "")
        _email = request.form.get("email", "")
        _password = request.form.get("password", "")
        return send_response(
            authmodel.registerUser(_firstname, _lastname, _email, _password)
        )


homecontroller = HomeController()
