from .base_controller import BaseController
from ..helper.utils import render_template
from ..helper.constants import STATUS_OK


class IndexController(BaseController):
    def __init__(self, client_address):
        self.user_ip = client_address[0]
        self.user_port = str(client_address[1])
        self.title = "Home"

    def get(self):
        return STATUS_OK, render_template(
            "index.html",
            title=self.title,
            user_ip=self.user_ip,
            user_port=self.user_port,
        )
