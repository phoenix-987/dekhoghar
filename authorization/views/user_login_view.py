from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from authorization.renderers import AuthJSONRenderer
from authorization.serializers import UserLoginSerializer
from authorization.bin.generate_user_tokens import GenerateUserTokens


class UserLoginView(APIView):
    renderer_classes = [AuthJSONRenderer]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                user = authenticate(email=email, password=password)

                if user is not None:
                    token = GenerateUserTokens().generate_user_tokens(user)
                    return Response(
                        {'message': 'User logged in',
                         'token': token},
                        status=status.HTTP_200_OK
                    )

                return Response(
                    {'message': {'non_field_errors': ['Email or password is not valid']}},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception:
            return Response({'message': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
