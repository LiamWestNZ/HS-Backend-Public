from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Accounts

admin.site.site_header = 'Harry and Sam Database Dashboard'

class AccountAdmin(UserAdmin):
    pass
    list_display = ('username','first_name', 'last_name', 'number','email','date_joined','last_login','is_admin','is_staff')
    search_fields = ('first_name', 'last_name','email')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ('date_joined',)
    fieldsets = ()

admin.site.register(Accounts, AccountAdmin)
