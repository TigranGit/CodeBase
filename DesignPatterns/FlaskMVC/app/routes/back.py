from flask import Blueprint
from flask import render_template

back = Blueprint("back", __name__)


@back.route("/admin/", methods=["GET"])
def index():
    user = {"nickname": "Tigran"}
    return render_template("admin.html", title="Login", user=user)
