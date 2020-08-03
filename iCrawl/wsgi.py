
from django.core.wsgi import get_wsgi_application

from iCrawl.settings.conf import setDefaultEnv

setDefaultEnv()


application = get_wsgi_application()
