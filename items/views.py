from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Category, Item, User
from .serializers import CategorySerializer, ItemSerializer, UserRegisterSerializer
from .permissions import IsAuthenticatedOrSafeMethods


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication ]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]


@api_view(http_method_names=['GET', ])
# @permission_classes([IsAuthenticated, ])
@authentication_classes([BasicAuthentication, ])
def get_user_info(request):
    user = request.user
    data = {
        "username": user.username,
        "password": user.password
    }
    return Response(data)


@api_view(http_method_names=['POST'])
def user_register(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)