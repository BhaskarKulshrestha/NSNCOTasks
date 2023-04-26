from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from api.models import Artist, Work
from api.serializers import ArtistSerializer, WorkSerializer

class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WorkSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Work.objects.all()

        artist_name = self.request.query_params.get('artist', None)
        if artist_name is not None:
            queryset = queryset.filter(artist__name__icontains=artist_name)

        work_type = self.request.query_params.get('work_type', None)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)

        return queryset

class RegisterAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        client = Client.objects.create(name=username, user=user)

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
