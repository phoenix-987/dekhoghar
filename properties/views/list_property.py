from rest_framework import status
from properties.models import Properties
from rest_framework.views import APIView
from rest_framework.response import Response
from properties.serializers import PropertySerializer
from properties.renderers import PropertiesJSONRenderer
from authorization.authentication import OwnerIsAuthenticated
from authorization.authentication import TenantIsAuthenticated


class TenantListPropertyView(APIView):
    """
    Class for fetching all the properties from the database and returning them to tenants.
    """

    # Renders the output in the Json format.
    renderer_classes = [PropertiesJSONRenderer]
    # Authenticates whether the user is authorized or not to perform the action.
    permission_classes = [TenantIsAuthenticated]

    def get(self, request):
        try:
            # Fetching all the properties.
            properties = Properties.objects.all().order_by('id')
            serializer = PropertySerializer(properties, many=True)

            # Returning all the properties as response.
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        # Sending the response if property not found.
        except Properties.DoesNotExist:
            return Response(
                {'message': 'Property does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Sending the response if something goes wrong with the respective error in the process.
        except Exception as e:
            print(e)
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetTenantPropertyView(APIView):
    """
    Class for fetching the requested property details from the database and returning them.
    """

    # Renders the output in the Json format.
    renderer_classes = [PropertiesJSONRenderer]
    # Authenticates whether the user is authorized or not to perform the action.
    permission_classes = [TenantIsAuthenticated]

    def get(self, request, pk):
        try:
            # Fetching the requested property object.
            property_obj = Properties.objects.get(pk=pk)
            serializer = PropertySerializer(property_obj)

            # Sending the details as a response.
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        # Sending the response if property not found.
        except Properties.DoesNotExist:
            return Response(
                {'message': 'Property does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Sending the response if something goes wrong with the respective error during the process.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class OwnerListPropertyView(APIView):
    """
    Class for fetching all the properties from the database and returning them to tenants.
    """

    # Renders the output in the Json format.
    renderer_classes = [PropertiesJSONRenderer]
    # Authenticates whether the user is authorized or not to perform the action.
    permission_classes = [OwnerIsAuthenticated]

    def get(self, request):
        try:
            # Fetching all the properties owned by owner.
            properties = Properties.objects.filter(user=request.user.id).order_by('id')
            serializer = PropertySerializer(properties, many=True)

            # Returning the properties as response.
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        # Sending the response if property not found.
        except Properties.DoesNotExist:
            print('Property does not exist.')
            return Response(
                {'message': 'Property does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Sending the response if something goes wrong with the respective error in the process.
        except Exception as e:
            print(e)
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetOwnerPropertyView(APIView):
    """
    Class for fetching the requested property details of owner from the database and returning them.
    """

    renderer_classes = [PropertiesJSONRenderer]
    permission_classes = [OwnerIsAuthenticated]

    def get(self, request, pk):
        try:
            # Fetching the requested property object.
            property_obj = Properties.objects.get(pk=pk, user=request.user.id)

            # if property not found then we will raise a 404 error.
            if not property_obj:
                raise Properties.DoesNotExist

            serializer = PropertySerializer(property_obj)

            # Sending the details as a response.
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        # Sending the response if property not found.
        except Properties.DoesNotExist:
            return Response(
                {'message': 'Property does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Sending the response if something goes wrong with the respective error during the process.
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
