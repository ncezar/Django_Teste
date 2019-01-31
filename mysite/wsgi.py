"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
<<<<<<< HEAD

from django.core.wsgi import get_wsgi_application
=======
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
>>>>>>> 702232158b50a7bce461d0541373c00e570ba281

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
<<<<<<< HEAD
=======
application = DjangoWhiteNoise(application)
>>>>>>> 702232158b50a7bce461d0541373c00e570ba281
