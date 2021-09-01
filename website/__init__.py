from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9x4x4x10xfjfs!@#0864'
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix ='/') 
    app.register_blueprint(auth, url_prefix ='/') 
    
    return app