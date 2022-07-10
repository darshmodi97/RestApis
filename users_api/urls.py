from django.urls import path
from users_api.views import InsertUsersView, UserListView, UserDetailView
app_name = "users_api"

urlpatterns=[
    path('insert', InsertUsersView.as_view(), name='insert_users'),
    path('api/users', UserListView.as_view(), name='users_list'),
    path('api/users/<int:pk>', UserDetailView.as_view(), name='user_detail')
]