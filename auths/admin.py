from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from auths.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    search_fields = ['email', 'username', 'is_active', 'is_admin']
    readonly_fields = ['id', 'uuid', 'created_at', 'last_updated']
    list_display = ['email', 'username', 'is_active', 'is_admin', 'created_at']
    list_filter = ['is_active', 'is_admin', 'created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    filter_horizontal = []
