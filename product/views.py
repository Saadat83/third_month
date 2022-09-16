import math

from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser

from rest_framework.response import Response

from .models import Product, Category
from rest_framework.views import APIView
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import permissions, status, generics


class ProductListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        products = Product.objects.all()

        page = int(request.GET.get('page', 1))
        per_page = 4
        total = products.count()
        start = (page - 1) * per_page
        end = page * per_page

        serializer = ProductSerializer(products[start:end], many=True)
        return Response({
            'data': serializer.data,
            'total': total,
            'page': page,
            'last_page': math.ceil(total/per_page)
        })


class ProductFilterApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'name', 'price']


class ProductCreateApiView(APIView):

    def post(self, request):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def put(self, requests, id):
        post = self.get_object(id)
        serializer = ProductSerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializers = ProductSerializer(post)
        data = serializers.data
        return Response(data)


class ProductDestroyApiView(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListApiView(APIView):
    def get(self, request):
        products = Category.objects.all()
        serializers = CategorySerializer(products, many=True)
        return Response(serializers.data)


class CategoryCreateApiView(APIView):
    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def put(self, requests, id):
        post = self.get_object(id)
        serializer = CategorySerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, name):
        category = self.get_object(name)
        products = Product.objects.filter(category__name=name)
        serializer = CategorySerializer(category)
        serializer2 = ProductSerializer(products, many=True)
        data = serializer.data
        data['products'] = serializer2.data

        return Response(data)


class CategoryDestroyApiView(APIView):

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilterPriceApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, price):
        prod = Product.objects.filter(price=price)
        serializers = ProductSerializer(prod, many=True)
        data = serializers.data
        return Response(data)


class AvgPriceListApiView(APIView):

    def get(self, request):
        products = Product.objects.all()
        price_list = []
        for p in products:
            price_list.append(p.price)
        avg_price = sum(price_list) / len(price_list)

        data = {
            "avg_price": avg_price
        }
        return Response(data)


class MinPriceApiView(APIView):

    def get(self, request):
        products = Product.objects.all()
        price_list = []
        for i in products:
            price_list.append(i.price)
        min_price = min(price_list)

        data = {
            "min_price": min_price
        }
        return Response(data)


class MaxPriceApiView(APIView):

    def get(self, request):
        products = Product.objects.all()
        price_list = []
        for i in products:
            price_list.append(i.price)
        max_price = max(price_list)

        data = {
            "max_price": max_price
        }
        return Response(data)


class Revenue(APIView):

    def get(self, request):
        products = Product.objects.all()
        revenue = []
        for i in products:
            one = i.price * i.quantity
            revenue.append(one)
        revenue = sum(revenue)

        data = {
            "revenue": revenue
        }
        return Response(data)


class Dashboard(APIView):
    def get(self, request):
        products = Product.objects.all()
        price_list = []
        revenue = []
        for p in products:
            price_list.append(p.price)
        avg_price = sum(price_list) / len(price_list)
        min_price = min(price_list)
        max_price = max(price_list)
        quantity_of_prod = len(price_list)
        for i in products:
            one = i.price * i.quantity
            revenue.append(one)
        revenue = sum(revenue)
        inf = {
            "avg_price": avg_price,
            "min_price": min_price,
            "max_price": max_price,
            "revenue": revenue,
            "quantity_of_prod": quantity_of_prod

        }
        return Response(inf)





