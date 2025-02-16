    # Autor: EDSON JÚNIOR FROTA SILVA
    # DATA: 16/02/2025
 
 #Endpoint GET /saudacao que recebe um parâmetro nome e retorna uma mensagem de saudação personalizada.
 
from flask import Flask, request, jsonify

# Inicializa o Flask
app = Flask(__name__)

# Endpoint 1: GET /saudacao
@app.route('/saudacao', methods=['GET'])
def saudacao():
    # Obtém o parâmetro 'nome' da query string
    nome = request.args.get('nome')
    
    if nome:
        mensagem = f"Olá, {nome}! Tudo bem?"
    else:
        mensagem = "Olá! Qual é o seu nome?"
    
    return jsonify({"mensagem": mensagem})

# Endpoint 2: POST /soma
@app.route('/soma', methods=['POST'])
def soma():
    
    dados = request.get_json()
    
    # Verifica se os campos 'numero1' e 'numero2' estão presentes no JSON
    if 'numero1' in dados and 'numero2' in dados:
        numero1 = dados['numero1']
        numero2 = dados['numero2']
        resultado = numero1 + numero2
        return jsonify({"resultado": resultado})
    else:
        
        return jsonify({"erro": "Por favor, forneça 'numero1' e 'numero2' no JSON."}), 400

if __name__ == '__main__':
    app.run(debug=True)