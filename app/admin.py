from django.contrib import admin

from app.models import Jaatelokioski, Tuote

@admin.register(Tuote)
class TuoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Jaatelokioski)
class JaatelokioskiAdmin(admin.ModelAdmin):
    pass