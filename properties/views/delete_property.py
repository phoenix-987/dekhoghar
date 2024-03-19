from rest_framework import status
from properties.models import Properties
from rest_framework.views import APIView
from rest_framework.response import Response
from properties.renderers import PropertiesJSONRenderer
from authorization.authentication import OwnerIsAuthenticated


class DeletePropertyView(APIView):

    # Renders the output in the Json format.
    renderer_classes = [PropertiesJSONRenderer]
    # Authenticates whether the user is authorized or not to perform the action.
    permission_classes = [OwnerIsAuthenticated]

    def delete(self, request, pk):
        try:
            # Fetching the required property object from database.
            property_obj = Properties.objects.get(pk=pk)

            if property_obj.user.id != request.user.id:
                return Response(
                    {"message": "You do not have permission to perform this action."},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Deleting the fetched property.
            response = property_obj.delete()

            # Checking if property is deleted or not with appropriate response respectively.
            if response[0] == 1:
                return Response(
                    {'message': 'Property removed successfully.'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'message': 'Property not found.'},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Sending the response if something goes wrong during the deletion process.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
