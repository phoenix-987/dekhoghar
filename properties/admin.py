from django.contrib import admin
from properties.models import Properties


# Register your models here.
class PropertiesAdmin(admin.ModelAdmin):
    # Customise display of the properties instead of just showing the object name.
    list_display = ('id', 'title', 'user', 'property_location', 'availability', 'rental_price', 'property_age')
    # Filters that can be applied to filter out the properties.
    list_filter = ('user', 'property_location', 'availability')

    # Used to group the fields categorically.
    fieldsets = (
        ('Property owner', {'fields': ['user']}),
        ('Property Information', {'fields': ['title', 'description', 'furnishing_type', 'carpet_area', 'property_age']}),
        ('Costs to Tenant', {'fields': ['rental_price', 'brokerage', 'maintenance', 'security_deposit']}),
        ('Locality & Tenant', {'fields': ['property_location', 'tenant_type']}),
    )

    # Fields that can be used to search the property.
    search_fields = ('title', 'property_location', 'rental_price')
    # Fields that can be used for ordering the property.
    ordering = ('id', 'rental_price', 'property_location', 'property_age')

    # Added to avoid following errors: <class 'properties.admin.PropertiesAdmin'>: (admin.E019) The value of
    # 'filter_horizontal[0]' refers to 'groups', which is not a field of 'properties.Properties'. <class
    # 'properties.admin.PropertiesAdmin'>: (admin.E019) The value of 'filter_horizontal[1]' refers to
    # 'user_permissions', which is not a field of 'properties.Properties'.
    filter_horizontal = []


# Registering the Properties model and admin panel respectively.
admin.site.register(Properties, PropertiesAdmin)
