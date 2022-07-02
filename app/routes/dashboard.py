# Imports functions Blueprint and render_template from flask
from flask import Blueprint, render_template

# consolidates routes into a single bp object that parent app can register later
# url_prefix prefixes every route with /dashboard
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')