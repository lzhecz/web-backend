from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status

class VideosAPIView(APIView):
    def get(self, request):
        return Response({'videos': []}, status=status.HTTP_200_OK)