from django.contrib import admin
from authorization.models.users import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModelAdmin(UserAdmin):
    # Customise display of the users instead of just showing the object name.
    list_display = ('id', 'email', 'name', 'is_owner', 'is_admin')
    # Filters that can be applied to filter out the users.
    list_filter = ('is_owner', 'is_admin')

    # Used to group the user fields categorically.
    fieldsets = [
        ('User Credentials', {'fields': ['email', 'password']}),
        ('Personal Info', {'fields': ['name']}),
        ('Roles', {'fields': ['is_owner', 'is_admin']}),
    ]

    # The fields to required while adding the new user.
    add_fieldsets = [
        ('User Details', {'fields': ('email', 'name', 'password')}),
    ]

    # The fields to required while adding the new data.
    search_fields = ['email']
    # Fields that can be used for ordering the property.
    ordering = ['email', 'name']

    # Added to avoid following errors: <class 'authorization.admin.UserModelAdmin'>: (admin.E019) The value of
    # 'filter_horizontal[0]' refers to 'groups', which is not a field of 'authorization.UserModelAdmin'.
    # <class 'authorization.admin.UserModelAdmin'>: (admin.E019) The value of 'filter_horizontal[1]' refers to
    # 'user_permissions', which is not a field of 'authorization.UserModelAdmin'.
    filter_horizontal = []


admin.site.register(User, UserModelAdmin)
