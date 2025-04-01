from .operadora import operadoras_bp
from .home import home_bp

def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(operadoras_bp)