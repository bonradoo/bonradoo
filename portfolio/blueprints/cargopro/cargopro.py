from flask import Blueprint, render_template

cargopro_bp = Blueprint('cargopro', __name__, static_folder="static", template_folder="templates")

@cargopro_bp.route('/cargopro')
def cargopro_page():
    return render_template('cargopro.html')
