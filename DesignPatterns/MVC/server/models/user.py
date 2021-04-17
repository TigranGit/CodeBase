import traceback

from ..helper.connection import DBConnection
from ..helper.constants import *
from ..configs import db_configs


class UserModel:
    def __init__(self):
        db_connection = DBConnection(**db_configs)
        self.connection = db_connection.connect()

    def insert_user(self, firstname, lastname, email, password):
        cursor = self.connection.cursor()

        error = self.validate_values(firstname, lastname, email, password)
        if error:
            cursor.close()
            return error

        params = [firstname, lastname, email, password]
        try:
            cursor.execute(INSERT_USER, params)
        except Exception as e:
            return e
        finally:
            cursor.close()

    def validate_values(self, firstname, lastname, email, password):
        if not (firstname and isinstance(firstname, str) and 0 < len(firstname) < 20):
            return ValueError(INVALID_VALUE_ERROR.format(firstname, "firstname"))

        if not (lastname and isinstance(lastname, str) and 0 < len(lastname) < 20):
            return ValueError(INVALID_VALUE_ERROR.format(lastname, "lastname"))

        if not (
            email
            and isinstance(email, str)
            and 0 < len(email) < 50
            and "%" in email
            and "." in email
        ):
            return ValueError(INVALID_VALUE_ERROR.format(email, "email"))

        if not (password and isinstance(password, str) and 6 < len(password) < 20):
            return ValueError(INVALID_VALUE_ERROR.format("your password", "password"))
        if not (password != password.lower() and not password.isalnum()):
            return ValueError(EASY_PASSWORD_ERROR)

    def get_users(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute(SELECT_USER)
            return cursor.fetchall()
        except Exception as e:
            traceback.print_exc()
            return ValueError(STATUS_SERVER_ERROR)
        finally:
            cursor.close()
