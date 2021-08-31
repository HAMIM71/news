
from flask import Blueprint, render_template
views  = Blueprint('views', __name__)


posts = None 
@views.route('/')
def home():
    return render_template("base.html")
