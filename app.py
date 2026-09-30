from flask import Flask, jsonify  
from flask_jwt_extended import JWTManager 
from database.db import init_db  
from routes.user_routes import user_bp  
from routes.formulario_routes import formulario_bp

app = Flask(__name__)

app.config.from_pyfile('config.py')

jwt = JWTManager(app)

# Padronização das respostas de erro do JWT em formato JSON e idioma português
@jwt.unauthorized_loader
def unauthorized_callback(reason):
    return jsonify({"error": "Token de autenticação não fornecido"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(reason):
    return jsonify({"error": "Token de autenticação inválido"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token de autenticação expirado"}), 401

init_db()

app.register_blueprint(user_bp, url_prefix='/users')

app.register_blueprint(formulario_bp, url_prefix='/formularios')

if __name__ == '__main__':
    app.run(debug=True)
