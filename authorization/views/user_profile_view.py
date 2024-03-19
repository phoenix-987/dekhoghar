from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from authorization.renderers import AuthJSONRenderer
from rest_framework.permissions import IsAuthenticated
from authorization.serializers import UserProfileSerializer


class UserProfileView(APIView):
    renderer_classes = [AuthJSONRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            serializer = UserProfileSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
