from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if SiteSettings.objects.exists() else True
    
    def has_delete_permission(self, request, obj=None):
        return False
