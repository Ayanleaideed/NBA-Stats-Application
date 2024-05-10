
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_stats_app.settings')
application = get_wsgi_application()

app = application  # Ensure this alias is created