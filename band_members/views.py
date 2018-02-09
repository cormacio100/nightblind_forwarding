# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from band_members.serializers import BandMemberSerializer
from band_members.models import Band_Member

"""
USER AUTHENTICATION HAS NOT BEEN USED IN THIS PROJECT YET
"""


class BandMemberView(APIView):
    """
        BandMemberView used to handle the incoming requests relating to
        groups and individual `band_member` items
    """
    def get(self,request,pk=None):
        """
        Retrieve a list of Band_Member items from the Band_Member items
        :param request:
        :return:
        """
        if pk is None:
            band_member_items = Band_Member.objects.all()
            # Serialize the data retrieved from the DB and serialize
            # them using the `BandMemberSerializer`
            serializer = BandMemberSerializer(band_member_items,many=True)
            # Store the serialized data `serialized_data`
            serialized_data = serializer.data
            return Response(serialized_data)
        else:
            band_member = Band_Member.objects.get(id=pk)
            # Serialize the data retrieved from the DB and serialize
            # them using the `BandMemberSerializer`
            serializer = BandMemberSerializer(band_member)
            # Store the serialized data `serialized_data`
            serialized_data = serializer.data
            return Response(serialized_data)

    """
        Used to handle the incoming POST requests relating to
        CREATING `band_member` items
    """
    def post(self,request):
        """
        Handle POST requests for the 'band_members/' endpoint

        This view will take the data property from the 'request' object, desrialize it into a Band_Member object,
        and store it in the DB

        Returns a 201 (successfully created) if the item is successfully created, otherwise returns a 400 (bad request)

        :param request:
        :return:
        """
        serializer = BandMemberSerializer(data=request.data)

        #   Check to see if the data in the 'request' is valid
        #   If not:
        #   -   a bad request response is returns
        #   Else:
        #   -   save the data and return the data and a success response
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
    """
        Used to handle the incoming PUT requests relating to
        UPDATINGS individual `band_member` items
    """
    def put(self,request,pk):
        """
        Handle PUT request for the 'band_members/' endpoint

        Retrieves a 'band_member/' instance based on the primary key contained in the URL
        Then takes the data property from the 'request' object to update the relevant 'band_member' instance

        Returns the updated object if the update was successful,
        otherwise
        400 (bad request) is returned
        :param request:
        :param pk:
        :return:
        """
        todo = Band_Member.objects.get(id=pk)
        serializer = BandMemberSerializer(todo,data=request.data)

        #   Check to see if the 'request' data is valid
        #   If it cannot be deserialized into a Band_Member object then a bad request response will be returned containing the error
        #   Else, save and return the data
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data)

    """
        Used to handle the incoming DELETE requests relating to
        individual `band_member` items
    """
    def delete(self,request,pk):
        """
        Handle DELETE request for the 'band_member' endpoint

        Retrieves a 'band_member' instance based on the pk contained in the URL and then deletes the relevant instance

        Returns a 204 (no content) status to indicate that the item was deleted
        :param request:
        :param pk:
        :return:
        """
        band_member = Band_Member.objects.get(id=pk)
        band_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

