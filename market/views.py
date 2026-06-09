from rest_framework.response import Response
from rest_framework.views import APIView

class HelloAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello World!'})
    def post(self, request):
        return Response({'message': 'Hello World!'})
