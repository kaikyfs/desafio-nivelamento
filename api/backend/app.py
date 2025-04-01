from flask import Flask
import config
from flask_cors import CORS
import os

def create_app():
     # Caminho absoluto para a pasta 'frontend'
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/teste-intuitive'))

    app = Flask(__name__, template_folder=template_dir)
    CORS(app)

    # Configuração da aplicação
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL

    # Importar e registrar rotas localmente
    from routes import register_routes
    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)