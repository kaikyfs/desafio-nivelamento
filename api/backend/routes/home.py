from flask import Blueprint, render_template
from src.controller.operadoras_controller import OperadorasController

home_bp = Blueprint('home', __name__)
controller = OperadorasController()

@home_bp.route('/')
def home():
    return render_template('index.html')