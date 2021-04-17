from .base_controller import BaseController
from ..helper.utils import render_template
from ..helper.constants import STATUS_OK
from ..models.user import UserModel


class RegistrationController(BaseController):
    def __init__(self, client_address):
        self.user_ip = client_address[0]
        self.user_port = str(client_address[1])
        self.title = "Registration"

    def get(self):
        return STATUS_OK, render_template(
            "registration.html",
            title=self.title,
            success_visibility="hidden",
            error_visibility="hidden",
            name="",
            error="",
        )

    def post(self, body):
        user_data = {el.split("=")[0]: el.split("=")[1] for el in body.split("&")}
        error = self.register_user(**user_data)
        name = user_data["firstname"]
        success_visibility = "visible" if not error else "hidden"
        error_visibility = "visible" if error else "hidden"
        return STATUS_OK, render_template(
            "registration.html",
            title=self.title,
            success_visibility=success_visibility,
            error_visibility=error_visibility,
            name=name,
            error=str(error) or "",
        )

    def register_user(self, firstname, lastname, email, password):
        model = UserModel()
        error = model.insert_user(firstname, lastname, email, password)
        return error
