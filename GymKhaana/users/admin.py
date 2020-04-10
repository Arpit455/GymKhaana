from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import CustomUser, CustomerProfile


class CustomUserAdmin(UserAdmin):
    model = CustomUser 
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm 
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_customer', 'is_manager','is_trainer', 'role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomerProfile)