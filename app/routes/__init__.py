# .home syntax finds module named home, api, and dashboard and then imports bp object and renames it home, api and dashboard
from .home import bp as home
from .dashboard import bp as dashboard
from .api import bp as api