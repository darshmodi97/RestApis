from rest_framework import serializers
from users_api.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name' ,'last_name', 'company_name', 'age',
                    'city', 'state', 'zip', 'email', 'web']
