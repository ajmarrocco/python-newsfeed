# Imports functions Blueprint and render_template from flask
from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

# consolidates routes into a single bp object that parent app can register later
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    # get all posts
    # get_db() functions returns a session connection that's tied to route's context
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()

    return render_template('homepage.html', posts=posts)

@bp.route('/login')
def login():
    return render_template('login.html')

# <id> represents a parameter which is why we include a single parameter function
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')