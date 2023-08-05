from django.urls import path
from account.views import AllUsers, Signup, Login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', AllUsers.as_view(), name="users"),
    path('signup/', Signup.as_view(), name="Sign_Up"),
    path('login/', Login.as_view(), name="Login"),
]