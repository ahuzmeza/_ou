from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = 'database.db'

# mysql connection config
# mysql:///[username]:[password]@[hostname]/[database]
con_username = 'guest'
con_password = 'password'
con_host = 'localhost'
con_db_name = '_ou_db'
# -------------------------------------------------
con_db = f'mysql+pymysql://{con_username}:{con_password}@{con_host}/{con_db_name}'.format()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = con_db
    app.config['SESSION_PERMANENT'] = True
    app.static_folder = 'static'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.auth_user'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, User_Relationship, User_Profile   
   
    db.create_all(app=app)

    return app
