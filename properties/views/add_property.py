from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from properties.serializers import PropertySerializer
from properties.renderers import PropertiesJSONRenderer
from authorization.authentication import OwnerIsAuthenticated


class AddPropertyView(APIView):

    # Renders the output in the Json format.
    renderer_classes = [PropertiesJSONRenderer]
    # Authenticates whether the user is authorized or not to perform the action.
    permission_classes = [OwnerIsAuthenticated]

    def post(self, request):
        serializer = PropertySerializer(data=request.data)

        # Saving the new property object in the database if data is valid with appropriate response.
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {'message': 'Property added successfully'},
                    status=status.HTTP_201_CREATED
                )

        # Sending the response if something goes wrong with the respective error while validating data.
        except serializers.ValidationError:
            return Response(
                {'message': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Sending the response if something goes wrong with the respective error at any point.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
