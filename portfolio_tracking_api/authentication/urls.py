from django.urls import path
from .views import GoogleLoginApi

urlpatterns = [
    path("auth/login/google/", GoogleLoginApi.as_view(), name="login-with-google"),
]
