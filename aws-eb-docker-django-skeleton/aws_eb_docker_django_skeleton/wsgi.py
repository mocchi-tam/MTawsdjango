import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aws_eb_docker_django_skeleton.settings")
application = get_wsgi_application()
