from flask import Blueprint, render_template

contact_bp = Blueprint('contact', __name__, static_folder="static", template_folder="templates")

@contact_bp.route('/contact')
def contact_page():
    return render_template('contact.html')
