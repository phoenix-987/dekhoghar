from authorization.renderers import AuthJSONRenderer
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from authorization.serializers import SendResetPwdMailSerializer


class SendResetPwdView(APIView):
    # Customised Preview of requested data in the form of JSON.
    renderer_classes = [AuthJSONRenderer]

    def post(self, request):
        serializer = SendResetPwdMailSerializer(data=request.data)

        # Sending mail with the appropriate response if all things are working fine
        try:
            if serializer.is_valid(raise_exception=True):
                return Response(
                    {'message': 'Password Reset link has been sent. Please check your email inbox or spam folder.'},
                    status=status.HTTP_200_OK
                )

        # Handling exceptions if serializers are not valid by any chance and returning response for the same.
        except serializers.ValidationError:
            return Response(
                {'message': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Handling exceptions if something goes wrong and returning response for the same.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
