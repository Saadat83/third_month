from django.http import Http404
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer
from .serializers import MyTokenObtainPairSerializer, UserSerializers
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import AnonPermissionOnly


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = RegisterSerializer


class UserListApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)


class UserDetailApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        product = Product.objects.filter(id=id)
        serializer = UserSerializers(user)
        # serializer2 = ProductSerializer(product, many=True)
        data = serializer.data
        # data['product'] = serializer2.data
        # data['quantity'] = len(serializer2.data)
        return Response(data)


class UserDestroyApiView(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(user_id=id)
        except User.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



