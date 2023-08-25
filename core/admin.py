from django.contrib import admin

from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'email')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
        ('Разрешения', {'fields': ('is_staff', 'is_active', 'is_superuser')})
    )
    list_display = ('username', 'first_name', 'last_name', 'email',)
    readonly_fields = ('last_login', 'date_joined')
