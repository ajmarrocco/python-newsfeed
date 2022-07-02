# Imports functions Blueprint and render_template from flask
from flask import Blueprint, render_template

# consolidates routes into a single bp object that parent app can register later
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')

# <id> represents a parameter which is why we include a single parameter function
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')