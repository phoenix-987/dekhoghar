from rest_framework import serializers
from authorization.models.users import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'is_owner', 'is_admin')
