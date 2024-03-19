from .views import *
from django.urls import path


urlpatterns = [
    path('owner/<int:pk>/', GetOwnerPropertyView.as_view(), name='get_property'),
    path('tenant/<int:pk>/', GetTenantPropertyView.as_view(), name='get_property'),

    path('owner/', OwnerListPropertyView.as_view(), name='get_all_properties_owner'),
    path('tenant/', TenantListPropertyView.as_view(), name='get_all_properties_tenant'),

    path('add-property/', AddPropertyView.as_view(), name='add_new_property'),

    path('edit-property/<int:pk>/', EditPropertyView.as_view(), name='edit_property'),
    path('delete-property/<int:pk>/', DeletePropertyView.as_view(), name='delete_property'),
]
