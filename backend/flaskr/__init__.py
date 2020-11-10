# 1: Step up application factory
import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/helloworld')
    def hello():
        total = str(eggs())
        return total


    def eggs():
        number = 12
        boxes = 6
        return number * boxes

# 5.1 Registering db with our app, initilize the db in terminal: new tab, activate environment: . venv/bin/activate, run: export FLASK_APP=flaskr, then: export FLASK_ENV=development, then: flask init-db. Should see our message appear.
    from . import db
    db.init_app(app)

# 6.1 Register blueprint with our app
    from . import authbp
    app.register_blueprint(authbp.bp)



# 1: Part of step 1
    return app