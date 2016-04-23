#!.venv/bin/python

activate_this = "/var/www/flask-headlines/.venv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, "/var/www/flask-headlines")
sys.path.insert(0, ".venv/bin/python")
from headlines import app as application
