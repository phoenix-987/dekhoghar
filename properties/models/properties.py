from django.db import models
from authorization.models import User

TENANT_CHOICES = (
    ('Any', 'Any'),
    ('Bachelor', 'Bachelor'),
    ('Family', 'Family'),
)

FURNISHING_CHOICES = (
    ('Unfurnished', 'Unfurnished'),
    ('Semi Furnished', 'Semi Furnished'),
    ('Fully Furnished', 'Fully Furnished'),
)

AVAILABILITY_CHOICES = (
    ('Immediately', 'Immediately'),
    ('Within 15 days', 'Within 15 days'),
    ('Within 30 days', 'Within 30 days'),
    ('After a month', 'After a month'),
)


class Properties(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=False,
                                   blank=False,
                                   default='Describe your property. It increases the chances to be shortlisted'
                                   )

    rental_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.00)
    brokerage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False, default=0.00)

    maintenance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False, default=0.00)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False, default=0.00)

    furnishing_type = models.CharField(max_length=256, null=False, blank=False,
                                       choices=FURNISHING_CHOICES, default='Unfurnished'
                                       )
    carpet_area = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    property_location = models.CharField(max_length=256, null=False, blank=False)
    availability = models.CharField(max_length=256, null=False, blank=False,
                                    choices=AVAILABILITY_CHOICES, default='Immediately'
                                    )

    tenant_type = models.CharField(max_length=256, null=False, blank=False,
                                   choices=TENANT_CHOICES, default='Any'
                                   )
    property_age = models.CharField(max_length=5, null=False, blank=False, default='New')
