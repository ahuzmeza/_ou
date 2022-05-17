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
con_db_name = '_ou_db'
unix_socket = '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
# -------------------------------------------------
con_db = f'mysql+pymysql:///{con_username}:{con_password}@{con_host}/{con_db_name}??unix_sock={unix_socket}'.format()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY']='hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = con_db
    db.init_app(app)
    
    app.config['SECRET_KEY'] = 'secret'
    
    app.static_folder = 'static'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User    
    
    return app