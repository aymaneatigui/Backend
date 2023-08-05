from django.contrib import admin
from account.models import MyUser
from django.contrib.auth.admin import UserAdmin

class SuperUser(UserAdmin):
    list_display = ['username','email','is_staff']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username','first_name', 'last_name')}),
        ('Token', {'fields': ['refresh_token']}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

admin.site.register(MyUser, SuperUser)