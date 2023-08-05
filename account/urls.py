from django.urls import path
from account.views import AllUsers, SignUp
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', AllUsers.as_view(), name="users"),
    path('signup/', SignUp.as_view(), name="Sign_Up"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]