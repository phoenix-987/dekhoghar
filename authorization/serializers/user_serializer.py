from rest_framework import serializers
from authorization.models.users import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'name', 'is_owner', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match!')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
