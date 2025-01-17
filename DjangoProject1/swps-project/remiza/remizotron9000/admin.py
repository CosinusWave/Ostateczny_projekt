from django.contrib import admin

from .models import FireFighter, FireTruck, FirefighterInSquad, Squad

admin.site.register(FireFighter)
admin.site.register(FireTruck)
admin.site.register(FirefighterInSquad)
admin.site.register(Squad)