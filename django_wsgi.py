import os,sys

# Add the virtual Python environment site-packages directory to the path
import site
site.addsitedir('/var/www/liftiumenv/lib/python2.6/site-packages')

# Add the current directory to the path
sys.path.append(os.path.dirname(__file__))
# And the parent directory
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(parent_path)


import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
