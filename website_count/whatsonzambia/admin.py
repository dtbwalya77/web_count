from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, CustomUser, Client
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'fullname', 'is_staff', 'is_active',)
    list_filter = ('email', 'fullname', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'fullname', 'password')}),
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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(Client)
