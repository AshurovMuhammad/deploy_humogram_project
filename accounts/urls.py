from django.urls import path
from accounts.views import register, LoginView, logout_user

urlpatterns = [
    path('login/', LoginView.as_view(), name='sign_in'),
    path("registration/", register),
    path("logout", logout_user, name="logout")
]
