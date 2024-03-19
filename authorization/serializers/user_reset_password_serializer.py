from rest_framework import serializers
from authorization.models.users import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError


class UserResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=255, style={'input_type': 'password'})
    confirm_password = serializers.CharField(max_length=255, style={'input_type': 'password'})

    class Meta:
        fields = ('new_password', 'confirm_password')

    def validate(self, attrs):
        try:
            # Fetching all the required field details from serializer and its context.
            new_password = attrs.get('new_password')
            confirm_password = attrs.get('confirm_password')
            uid = self.context.get('uid')
            token = self.context.get('token')

            # Checking if both new password and confirm password is same or not.
            if new_password != confirm_password:
                raise serializers.ValidationError('Passwords do not match')

            # Decoding user id from reset URI
            user_id = smart_str(urlsafe_base64_decode(uid))
            # Fetching user details from the database.
            user = User.objects.get(id=user_id)

            # Checking if passed token in the URI is whether valid or not.
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError('Expired or Invalid token')

            # Setting up the new password for the user.
            user.set_password(new_password)
            user.save()

            return attrs

        # Handling exception if some error occurs during encoding or decoding.
        except DjangoUnicodeDecodeError:
            raise serializers.ValidationError('Expired or Invalid token')

        # Handling exception if encountered with an error.
        except Exception as e:
            raise serializers.ValidationError(str(e))
