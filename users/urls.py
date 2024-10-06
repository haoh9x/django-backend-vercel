from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, EmailExistView, UsernameExistView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    re_path(r"^exist/email/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$", EmailExistView.as_view()),
    re_path(r"^exist/username/(?P<username>\w+)/$", UsernameExistView.as_view()),
]
urlpatterns += router.urls