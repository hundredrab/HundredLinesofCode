from rest_framework import serializers
from .models import Track

class ArtistSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=50)


class SerializedTrack(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    artist = ArtistSerializer(many=True)
    release_year  = serializers.DecimalField(4, 0)


class TrackSerializer(serializers.ModelSerializer):
    
    artist = ArtistSerializer(many = True)

    class Meta:
        model = Track
        fields = '__all__'