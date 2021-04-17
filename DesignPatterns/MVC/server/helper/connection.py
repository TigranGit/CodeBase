import psycopg2


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBConnection(metaclass=Singleton):
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        self.connection = psycopg2.connect(
            host="localhost", database="mvc", user="postgres", password="admin"
        )
        self.connection.autocommit = True
        return self.connection

    def cursor(self):
        return self.connection.cursor()
