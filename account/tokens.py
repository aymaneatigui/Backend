from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken

def createToken(user):
    refresh = RefreshToken.for_user(user)
    access = str(refresh.access_token)
    token = AccessToken(access)
    expires_at = token['exp']
    return {
        'refresh': str(refresh),
        'access': access,
        'exp': expires_at,
    }
