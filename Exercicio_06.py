    # Autor: EDSON JÚNIOR FROTA SILVA
    # DATA: 16/02/2025

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__)

# Configuração do Flask-Limiter para prevenir ataques de força bruta
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]  # Limita a 5 tentativas de login por minuto
)

SENHA_ADMIN_HASH = generate_password_hash('1234')  # Gera um hash da senha

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")  # Aplica o limite de taxa à rota /login
def login():

    if not request.form.get('username') or not request.form.get('password'):
        return jsonify({"erro": "Usuário e senha são obrigatórios"}), 400

    username = request.form['username']
    password = request.form['password']


    if username == 'admin' and check_password_hash(SENHA_ADMIN_HASH, password):
        return jsonify({"mensagem": "Acesso concedido"}), 200
    else:
        return jsonify({"mensagem": "Credenciais inválidas"}), 401

if __name__ == '__main__':
    # Desativa o modo de depuração em produção
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)