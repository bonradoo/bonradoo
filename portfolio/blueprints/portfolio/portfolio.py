from flask import Blueprint, render_template

portfolio_bp = Blueprint('portfolio', __name__, static_folder="static", template_folder="templates")

@portfolio_bp.route('/portfolio')
def portfolio_page():
    return render_template('portfolio.html')
