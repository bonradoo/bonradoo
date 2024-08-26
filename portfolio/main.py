from flask import Flask, render_template, redirect, request, jsonify, url_for
from blueprints.home.home import home_bp
from blueprints.portfolio.portfolio import portfolio_bp
from blueprints.dfd.dfd import dfd_bp
from blueprints.cargopro.cargopro import cargopro_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(cargopro_bp, url_prefix='/cargo-pro')
app.register_blueprint(dfd_bp, url_prefix='/deepfake-detector')
app.register_blueprint(portfolio_bp, url_prefix='/portfolio')

@app.route("/")
def index():
    return redirect(url_for("home.homepage"))

if __name__ == '__main__':
    app.run(debug=True)
