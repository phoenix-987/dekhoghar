from rest_framework import serializers
from django.contrib.auth import authenticate


class UserChangePasswordSerializer(serializers.Serializer):
    # Serializer fields
    old_password = serializers.CharField(max_length=255, style={'input_type': 'new_password'}, write_only=True)
    new_password = serializers.CharField(max_length=255, style={'input_type': 'new_password'}, write_only=True)
    confirm_password = serializers.CharField(max_length=255, style={'input_type': 'new_password'}, write_only=True)

    class Meta:
        fields = ('new_password', 'confirm_password')

    def validate(self, attrs):
        # Getting values from the serialized data
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        # Object for user passed as context from view
        user = self.context.get('user')

        # Checking if the old password is correct or not
        if not authenticate(email=user.email, password=old_password):
            raise serializers.ValidationError('Old password is incorrect.')

        # Checking if the new password matches or not
        if new_password != confirm_password:
            raise serializers.ValidationError('Passwords do not match!')

        # Saving New Password in the database.
        try:
            user.set_password(new_password)
            user.save()
        except Exception as e:
            raise serializers.ValidationError(str(e))

        return attrs
