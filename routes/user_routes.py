from flask import Blueprint, request, jsonify  
from flask_jwt_extended import jwt_required
from controllers.user_controller import UserController 

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True) or {}
    response, status = UserController.register_user(data)
    return jsonify(response), status

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    response, status = UserController.login_user(data)
    return jsonify(response), status

@user_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    response, status = UserController.get_user_by_id(id)
    return jsonify(response), status

@user_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    data = request.get_json(silent=True) or {}
    response, status = UserController.update_user(id, data)
    return jsonify(response), status

@user_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    response, status = UserController.delete_user(id)
    return jsonify(response), status
