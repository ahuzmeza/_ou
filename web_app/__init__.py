from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import sqlalchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

# mysql connection config
# mysql:///[username]:[password]@[hostname]/[database]
con_username = 'root'
con_password = ''
con_host = 'localhost'
con_db_name = 'database'
# -------------------------------------------------
con_db = f'mysql:///{con_username}:{con_password}@{con_host}/{con_db_name}'.format()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY']='hjshjhdjah kjshkjdhjs'
    app.config[ 'SQLALCHEMY_DATABASE_URI']= con_db
    db.init_app(app)
    
    app.config['SECRET_KEY'] = 'secret'
    
    app.static_folder = 'static'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app