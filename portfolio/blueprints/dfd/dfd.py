from flask import Blueprint, render_template

dfd_bp = Blueprint('dfd', __name__, static_folder="static", template_folder="templates")

@dfd_bp.route('/dfd')
def dfd_page():
    return render_template('dfd.html')
