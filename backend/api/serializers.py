from rest_framework import serializers
from api.models import Artist, Client, Work

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(), source='artist')
    clients = ClientSerializer(many=True, read_only=True)

    class Meta:
        model = Work
        fields = '__all__'
