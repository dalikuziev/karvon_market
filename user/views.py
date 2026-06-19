from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from market.serializers import ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    @action(detail=False, methods=['get'])
    def products(self, request, *args, **kwargs):
        user = request.user
        products = user.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
