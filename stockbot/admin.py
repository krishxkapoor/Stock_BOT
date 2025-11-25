from django.contrib import admin
from .models import Watchlist, Alert, Signal

admin.site.register(Watchlist)
admin.site.register(Alert)
admin.site.register(Signal)
