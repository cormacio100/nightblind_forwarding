# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from band_members.serializers import BandMemberSerializer
from band_members.models import Band_Member

class BandMemberView(APIView):
    """
        BandMemberView used to handle the incoming requests relating to
        `band_member` items
    """
    def get(self,request):
        """
        Retrieve a list of Band_Member items from the Band_Member items
        :param request:
        :return:
        """
        band_member_items = Band_Member.objects.all()
        # Serialize the data retrieved from the DB and serialize
        # them using the `BandMemberSerializer`
        serializer = BandMemberSerializer(band_member_items,many=True)
        # Store the serialized data `serialized_data`
        serialized_data = serializer.data
        return Response(serialized_data)
