# from crypt import methods
# from traceback import print_tb
import email
from flask import Blueprint, request, jsonify
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

# POST routes receive data
@bp.route('/users', methods =['POST'])
def signup():
    # returns data as Python Dictionary
    data = request.get_json()
    db = get_db()
    # create a new user
    newUser = User(
        # bracket notation for Python dictionary
        username = data['username'],
        email = data['email'],
        password = data['password']
    )
    # save in database
    db.add(newUser)
    db.commit()
    
    # returns new User wtih ID number
    return jsonify(id = newUser.id)
