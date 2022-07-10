from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from users_api.models import User
from users_api.serializers import UserSerializer
import requests
# Create your views here.


class InsertUsers(CreateAPIView):
    """
    This class is responsible for insert all user's data into the DB using postman.
    """
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        many = isinstance(data, list)        
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
        )

class UserList(ListAPIView):
    """This class is responsible for showing the list of all users."""

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
    def get(self, request, *args, **kwargs):

        serializer = self.serializer_class(self.get_queryset() , many=True)        
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )