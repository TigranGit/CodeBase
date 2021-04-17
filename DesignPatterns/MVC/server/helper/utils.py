import os
import re

from .constants import *


def render_template(view_name, **kwargs):
    view_path = os.path.join(VIEW_PATH, view_name)
    with open(view_path, "r") as file:
        content = file.read()

    for key, value in kwargs.items():
        content = re.sub(r"{{\s*%s+\s*}}" % key, value, content)

    return content
