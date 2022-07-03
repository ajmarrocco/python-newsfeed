# imports Flask() function from flask module
from flask import Flask
# imports home module from app.routes
# Can do this because the __init__.py file imported and renamed blueprint object
from app.routes import home, dashboard
# imports init_db from app/db
from app.db import init_db

def create_app(test_config=None):
  # set up app config, don't need to declare using const or var
  # App should serve any static resources from the root directory 
  # and not from default /static directory
  app = Flask(__name__, static_url_path='/')
  # Make trailing slash optional. Eg: /dashboard vs /dashboard/
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    # used when creating a server-side session
    SECRET_KEY='super_secret_key'
  )
  # turns function into a route
  @app.route('/hello')
  # adds inner function
  def hello():
    return 'hello world'

  # register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  # initializes database
  init_db(app)

  return app