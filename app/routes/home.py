# Imports functions Blueprint and render_template from flask
from flask import Blueprint, render_template, session, redirect
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

    return render_template(
        'homepage.html', 
        posts=posts, 
        loggedIn = session.get('loggedIn')
    )

@bp.route('/login')
def login():
    # not login in
    if session.get('loggedIn') is None:
        return render_template('login.html')
        
    return redirect('/dashboard')

# <id> represents a parameter which is why we include a single parameter function
@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render single post template
    return render_template(
        'single-post.html',
        post=post,
        loggedIn = session.get('loggedIn')
    )