
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)  # Crea el blueprint llamado 'main'

@bp.route('/')  # Define la ruta raíz ("/")
def home():
    return render_template("home.html")  # Renderiza el template 'home.html'

