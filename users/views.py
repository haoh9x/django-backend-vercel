from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import CustomUser
from .serializers import UserAdminSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserAdminSerializer
    permission_classes = [IsAdminUser]

    lookup_field = 'username'
    
    @action(methods=['post'], detail=True, url_path='inactive', url_name='inactive')
    def inactive(self, reuqest, username):
        try:
           user = CustomUser.objects.get(username=username)
           user.is_active = False
           user.save()
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=UserAdminSerializer(user).data, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=True, url_path='active', url_name='active')
    def active(self, reuqest, username):
        try:
           user = CustomUser.objects.get(username=username)
           user.is_active = True
           user.save()
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=UserAdminSerializer(user).data, status=status.HTTP_200_OK)

class EmailExistView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, email):
        try:
           user = CustomUser.objects.filter(email=email).exists()
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user)
    
class UsernameExistView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, username):
        try:
           user = CustomUser.objects.filter(username=username).exists()
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user)