import os
import sys

# Define the base directory of your Django project (where manage.py securely lives)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Add this path to the Python system path so the app imports work properly
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Set Django settings module configuration naturally
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourhobe.settings')

# Phusion Passenger loads the 'application' variable by default
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
