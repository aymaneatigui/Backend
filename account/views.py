from account.models import MyUser
from account.serializer import UserSerializer
from account.tokens import createToken
from django.contrib.auth import authenticate

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated


class AllUsers(GenericAPIView, ListModelMixin):
    permission_classes = [IsAuthenticated]
    def get(self,request:Request):
        queryset = MyUser.objects.all()
        users = UserSerializer(queryset, many=True)
        return Response(users.data, status=status.HTTP_200_OK)

class Signup(GenericAPIView, CreateModelMixin):
    def post(self, request:Request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = createToken(user)
            user.refresh_token = tokens["refresh"]
            user.save()
            return Response({"Message" : "User has been created", 'Token': tokens,"Data": serializer.data}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Login(APIView):
    def post(self, request:Request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            tokens = createToken(user)
            user.refresh_token = tokens["refresh"]
            user.save()
            return Response({'message':'Login Successfull','Tokens':tokens},status=status.HTTP_200_OK)        
        return Response({'message':'Invalid Email Or Password'},status=status.HTTP_401_UNAUTHORIZED)
    