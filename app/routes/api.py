import sys
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
    try:
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
    except:
        # insert failed, so send error message
        print(sys.exe_info()[0])

        # insert failed, so rollback and send error to front end
        db.rollback()
        return jsonify(message = 'Signup failed'), 500
    
    # returns new User wtih ID number
    return jsonify(id = newUser.id)
