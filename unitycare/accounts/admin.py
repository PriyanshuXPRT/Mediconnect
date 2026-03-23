from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class AdminUserCreationForm(UserCreationForm):
    """Admin add-user form that includes the custom 'role' field."""
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name", "role")


class AdminUserChangeForm(UserChangeForm):
    """Admin change-user form that includes the custom 'role' field."""
    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Use custom forms so 'role' appears in both add and change forms
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm

    # Show 'role' in the change page
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )

    # Show 'role' in the add page
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Role', {'fields': ('role',)}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = BaseUserAdmin.list_filter + ('role',)