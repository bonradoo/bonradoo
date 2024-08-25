from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__, static_folder="static", template_folder="templates")

PROJECTS = [
        {
            "title": "CARGO-PRO",
            "details": "Project Details: A logistics management system.",
            "image_url": "static/cargo-pro.png",
            "url": "https://cargo-pro.pl"
        },
        {
            "title": "Konrad Bik",
            "details": "Portfolio: Cybersecurity specialist and sport enthusiast.",
            "image_url": "static/konrad-bik.jpg",
            "logo": "static/logo_yellow.png",
            "url": "https://konradbik.com"
        },
        {
            "title": "DEEPFAKEDETECTOR",
            "details": "Project Details: AI-powered deepfake detection tool.",
            "image_url": "static/deepfakedetector.png",
            "url": "https://image.deepfakedetector.pl",
            "hero_image": "static/deepfakedetector.png"
        }
    ]

@home_bp.route('/')
def homepage():
    return render_template('home.html', projects=PROJECTS)
