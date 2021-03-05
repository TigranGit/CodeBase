## FlaskMVC


Install environment for flask app.

    pip install Flask

    pip install virtualenv


To run the application use following commands:

    virtualenv venv
    source venv/Scripts/activate

    pip install -e .

    export FLASK_APP=app/__init__.py
    export FLASK_ENV=development
    export FLASK_DEBUG=1

    flask run


To change database connection open app/config.py and configure

    config['MONGO_DBNAME'] = 'flaskmvc'
    config['MONGO_URI'] = 'mongodb://localhost:27017/flaskmvc'
