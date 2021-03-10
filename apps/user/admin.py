from django.contrib import admin
from .models import User
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
class UserAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):

    list_display = ('id', 'type', 'username', 'full_name', 'email', 'is_active')
    search_fields = ('id', 'email')

admin.site.register(User, UserAdmin)