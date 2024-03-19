from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from authorization.renderers import AuthJSONRenderer
from authorization.serializers import UserResetPasswordSerializer


class UserResetPasswordView(APIView):
    renderer_classes = [AuthJSONRenderer]

    def post(self, request, uid, token):
        # Serializing the object from requests' body
        serializer = UserResetPasswordSerializer(
            data=request.data,
            context={'uid': uid, 'token': token}
        )

        # Process of resetting password is initiated during the validation.
        try:
            if serializer.is_valid(raise_exception=True):
                return Response(
                    {'message': 'Password reset successfully.'},
                    status=status.HTTP_200_OK
                )

        # Handling the exceptions occurred during the validation process of serializers.
        except serializers.ValidationError:
            return Response(
                {'message': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Handling any unknown exceptions occurred during the process.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
