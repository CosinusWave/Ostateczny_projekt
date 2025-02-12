from django.contrib import admin
from .models import Shelf, User, Book, DVD

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['name', 'nazwisko']
    readonly_fields = ['data_dodania']

admin.site.register(User)
admin.site.register(Book)
admin.site.register(DVD)
admin.site.register(Shelf)

# Register your models here.
