from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from users.forms import FarmcareUserCreationForm, FarmcareUserChangeForm
from users.models import FarmcareUser


class FarmcareUserAdmin(UserAdmin):
    add_form = FarmcareUserCreationForm
    form = FarmcareUserChangeForm
    model = FarmcareUser
    list_display = ('email', 'is_staff', 'is_active',
                    'zipcode', 'date_joined',)
    list_filter = ('email', 'is_staff', 'is_active', 'zipcode', 'date_joined',)
    fieldsets = (
        (None, {'fields': ['first_name', 'last_name', 'email', 'zipcode', 'password', ]}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(FarmcareUser, FarmcareUserAdmin)