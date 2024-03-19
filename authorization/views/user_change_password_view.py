from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from authorization.renderers import AuthJSONRenderer
from rest_framework.permissions import IsAuthenticated
from authorization.serializers.user_change_password_serializer import UserChangePasswordSerializer


class UserChangePasswordView(APIView):
    renderer_classes = [AuthJSONRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})

        try:
            # Checking if the serializer is valid or not and if not it will raise an exception.
            if serializer.is_valid(raise_exception=True):
                return Response(
                    {'message': 'Password changed successfully'},
                    status=status.HTTP_200_OK
                )

        # Handling exception if serializer is not valid.
        except serializers.ValidationError:
            return Response(
                {'message': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Handling error if something else goes wrong.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
