from os import environ
from rest_framework import serializers
from authorization.models.users import User
from django.utils.encoding import force_bytes
from authorization.bin.send_email import SendMail
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class SendResetPwdMailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')

        # Checking if user exists then send the mail with enclosed reset link URI
        if User.objects.filter(email=email).exists():
            # Creating user object ofr the required mail id
            user = User.objects.get(email=email)
            # Encoding User ID so that it is invisible in the reset password URI
            uid = urlsafe_base64_encode(force_bytes(user.id))
            # Generating Reset Password Token
            token = PasswordResetTokenGenerator().make_token(user)
            # Combining and creating required Rest Password URI
            reset_uri = f"{environ.get('RESET_URI')}/{uid}/{token}/"

            # Sending Mail to the user
            response = SendMail().send_email(user.name, user.email, reset_uri)

            # In any case mail is not sent then it will raise an exception.
            if not response.get('status'):
                raise Exception(response.get('message'))

            return attrs

        # If mail is not found in the database, then raising exception to enter correct mail address.
        else:
            raise serializers.ValidationError('Given email address is not registered.')
