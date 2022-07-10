import json
import requests
from django.db.models import Q
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                    RetrieveUpdateDestroyAPIView
                                    )

from users_api.models import User
from users_api.serializers import UserSerializer
from users_api.pagination import CustomPagination
# Create your views here.


class InsertUsersView(CreateAPIView):
    """
    This class is responsible for insert all user's data into the DB using postman.
    """
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        This function will fetch and store the user's data into DB.
        """
        response = requests.get(url='https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json').content
        data = json.loads(response)
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

class UserListView(ListCreateAPIView):
    """This class is responsible for showing the list of all users with 
        paginated response.
    """
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    pagination_class = CustomPagination


    def get_queryset(self):
        ordering = self.request.query_params.get('sort', 'id')
        search_keyword = self.request.query_params.get('name')
        try:
            queryset = User.objects.values('age', 'city', 'company_name',
                                           'email', 'first_name', 'id',
                                           'last_name', 'state', 'web', 'zip')\
                                    .filter(
                                        Q(first_name__icontains=search_keyword)|
                                        Q(last_name__icontains=search_keyword))\
                                    .order_by(ordering)
        except Exception as _:
            queryset = User.objects.values('age', 'city', 'company_name',
                                           'email', 'first_name', 'id',
                                           'last_name', 'state', 'web', 'zip')
        return queryset

    

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer=serializer)

        return Response(
            status=status.HTTP_201_CREATED,
            data={"message":"User created successfully."}
        )


class UserDetailView(RetrieveUpdateDestroyAPIView):
    """
        This class will the user's detail and also allows to update an user's
        detail.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(instance=obj, context={'request': request})
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
