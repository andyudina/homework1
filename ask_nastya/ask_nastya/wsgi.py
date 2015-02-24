"""
WSGI config for ask_nastya project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os, sys
sys.path.append("home/nastya/ask_nastya")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask_nastya.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
