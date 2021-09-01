
from flask import Blueprint, render_template
views  = Blueprint('views', __name__)
from .data import TOTALRESULT


posts = None 
@views.route('/')
def home():
    return render_template("news.html", data = TOTALRESULT)
