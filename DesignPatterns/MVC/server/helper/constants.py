# Define socket host and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000

# File paths
VIEW_PATH = "server/views"

# Statuses
STATUS_OK = "200 OK"
STATUS_SERVER_ERROR = "500 Internal Server Error"
STATUS_NOT_FOUND = "404 Not Found"
STATUS_METHOD_ERROR = "405 Method Not Allowed"

# DB commands
INSERT_USER = "INSERT INTO mvc.users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)"
SELECT_USER = "SELECT * from mvc.users"

# Error messages
INVALID_VALUE_ERROR = "'{}' is an invalid value for '{}' field."
EASY_PASSWORD_ERROR = """Password needs to be complex.
Please use upper letters and special symbols."""
