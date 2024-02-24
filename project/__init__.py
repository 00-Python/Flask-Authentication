from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

#init SQLAlchemy so we can use it later in our model
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    csrf = CSRFProtect(app)
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    with app.app_context():
        from .models import User, UserRole
        from .auth import auth as auth_blueprint
        from .main import main as main_blueprint

        app.register_blueprint(auth_blueprint)
        app.register_blueprint(main_blueprint)

        db.create_all()

        @login_manager.user_loader
        def load_user(user_id):
            # since the user_id is just the primary key of our user table, use it in the query for the user
            return User.query.get(int(user_id))

        # create admin role if not exists
        if UserRole.query.filter_by(name='admin').first() is None:
            admin_role = UserRole(name='admin')
            db.session.add(admin_role)

        # create user role if not exists
        if UserRole.query.filter_by(name='user').first() is None:
            user_role = UserRole(name='user')
            db.session.add(user_role)

        db.session.commit()

    return app