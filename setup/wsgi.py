import os
from whitenoise import WhiteNoise
from .settings import STATIC_ROOT, MEDIA_ROOT, MEDIA_URL
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
