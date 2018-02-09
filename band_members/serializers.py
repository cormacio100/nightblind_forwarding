from rest_framework import serializers
from band_members.models import Band_Member

class BandMemberSerializer(serializers.ModelSerializer):
    """
    Band_Member Serializer.

    Used to serialize the Band_Member model to JSON. The fields to be
    serialized are:
    -   short_name
    -   name
    -   instrument
    -   gear
    """

    class Meta:
        model = Band_Member
        fields = ('id', 'short_name', 'name',
                  'instrument', 'gear')