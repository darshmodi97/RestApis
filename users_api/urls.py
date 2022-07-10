from django.urls import path
from users_api.views import InsertUsers, UserList

app_name = "users_api"

urlpatterns=[
    path('insert', InsertUsers.as_view(), name='insert_users'),
    path('api/users', UserList.as_view(), name='users_list')
]