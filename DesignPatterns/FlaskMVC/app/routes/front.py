from flask import Blueprint
from app.controllers.HomeController import homecontroller

front = Blueprint("front", __name__)


@front.route("/", methods=["GET"])
def home():
    return homecontroller.index()


@front.route("/registration", methods=["GET"])
def register():
    return homecontroller.register()


@front.route("/registration", methods=["POST"])
def registeruser():
    return homecontroller.registeruser()
