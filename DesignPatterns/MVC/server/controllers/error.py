from .base_controller import BaseController
from ..helper.constants import STATUS_SERVER_ERROR


class ErrorController(BaseController):
    def __init__(self, user_ip, status=STATUS_SERVER_ERROR):
        self.user_ip = user_ip
        self.status = status

    def get(self):
        return self.status, ""
