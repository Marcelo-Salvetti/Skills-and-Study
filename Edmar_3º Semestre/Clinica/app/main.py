from flask import Flask, request, jsonify
from services.paciente_service import adicionar_paciente

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem":"Bem vindo ao Sistema de Consultas"})
@app.route('/pacientes', methods=['POST'])
def novo_paciente():
    dados = request.get_json()
    adicionar_paciente(dados['nome'], dados['idade'], dados['cpf'])
    return jsonify({"mensagem":"Paciente cadastrado com sucesso"})
if __name__ == '__main__':
    app.run(debug=True)