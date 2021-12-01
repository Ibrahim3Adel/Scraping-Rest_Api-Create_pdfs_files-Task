from django.contrib import admin
from .models import novel_auth
from import_export.admin import ImportExportActionModelAdmin

admin.site.register(novel_auth)
class ViewAdmin(ImportExportActionModelAdmin):
    pass