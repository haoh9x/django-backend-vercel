from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data.update({'email': self.user.email})
        data.update({'username': self.user.username})
        data.update({'first_name': self.user.first_name})
        data.update({'last_name': self.user.last_name})
        data.update({'created_at': self.user.created_at})
        data.update({'updated_at': self.user.updated_at})
        data.update({'is_active': self.user.is_active})
        data.update({'is_staff': self.user.is_staff})
        data.update({'is_superuser': self.user.is_superuser})

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token
    
class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'last_login', 'created_at', 'updated_at', 'password']
        extra_kwargs = {'password': {'write_only': True}}