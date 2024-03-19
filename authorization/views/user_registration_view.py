from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from authorization.renderers import AuthJSONRenderer
from authorization.serializers.user_serializer import UserSerializer
from authorization.bin.generate_user_tokens import GenerateUserTokens


class UserRegistrationView(APIView):
    renderer_classes = [AuthJSONRenderer]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                token = GenerateUserTokens().generate_user_tokens(user)

                return Response(
                    {
                        'message': 'Registration successful!',
                        'token': token
                    },
                    status=status.HTTP_201_CREATED
                )

        except serializers.ValidationError:
            return Response(
                {'message': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
