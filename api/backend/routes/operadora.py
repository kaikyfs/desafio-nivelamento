from flask import Blueprint, jsonify, request
from src.controller.operadoras_controller import OperadorasController

operadoras_bp = Blueprint('operadoras', __name__)
controller = OperadorasController()

@operadoras_bp.route('/api/operadora/<nome>', methods=['GET'])
def get_operadora(nome):
    operadora = controller.get_operadora(nome)
    if operadora:
        return jsonify(operadora.to_dict()), 200
    return jsonify({"error": "Operadora não encontrada"}), 404

@operadoras_bp.route('/api/operadora', methods=['GET'])
def get_operadoras():
    operadoras = controller.get_operadoras()
    if operadoras:
        return jsonify([operadora.to_dict() for operadora in operadoras]), 200
    return jsonify({"error": "Nenhuma operadora encontrada"}), 404