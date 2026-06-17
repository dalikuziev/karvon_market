from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from market.serializers import ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail=True, methods=['get'])
    def products(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = ProductSerializer(user.products.all(), many=True)
        return Response(serializer.data)
