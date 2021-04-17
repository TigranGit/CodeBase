from ..helper.constants import STATUS_METHOD_ERROR


class BaseController:
    def __init__(self, *args, **kwargs):
        pass

    def get(self):
        return STATUS_METHOD_ERROR, ""

    def post(self):
        return STATUS_METHOD_ERROR, ""

    def handle(self, method, body=""):
        if method == "GET":
            return self.get()
        elif method == "POST":
            return self.post(body)
