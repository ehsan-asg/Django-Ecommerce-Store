from django.contrib import admin
from .models import User,OtpCode
from .forms import UserCreationForm,UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ['phone_number','code','created_at']
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('full_name','phone_number','role')
    list_filter = ('role','created_at')
    readonly_fields = ('last_login',)

    fieldsets = (
		('Main', {'fields':( 'phone_number', 'email','full_name','role','image_profile','password')}),
		('Permissions', {'fields':('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')}),
	)

    add_fieldsets = (
		("Add User", {'fields':('phone_number', 'email','full_name','role','image_profile','password')}),
	)

    search_fields = ('email', 'phone_number','full_name')
    ordering = ('created_at',)
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(User, UserAdmin)