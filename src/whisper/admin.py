
from src.core.admin import admin_site
from src.whisper.models import HostInfo

admin_site.register(HostInfo)