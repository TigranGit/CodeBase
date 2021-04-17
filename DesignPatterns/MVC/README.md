# MVC


Install a virtual environment package

    pip install virtualenv


To create a virtual environment (only once):

    virtualenv venv

    source venv/Scripts/activate

    pip install -r requirements.txt


To run the application use following commands:

    source venv/Scripts/activate

    python -m server.run

To kill the application use `Ctrl + C (^C)`

## Create DB

1. Install PostgreSQL

2. Create a schema 'mvc'

3. Create a table 'mvc.users' (use the following DDL)

    DDL:

        CREATE TABLE mvc.users (
            user_id serial UNIQUE PRIMARY KEY,
            firstname VARCHAR(20),
            lastname VARCHAR(20),
            email VARCHAR(50),
            password VARCHAR(20)
        );

4. Set the DB connection configs in the `server/configs.py`
