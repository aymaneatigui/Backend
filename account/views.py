from account.models import MyUser
from account.serializer import UserSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

class AllUsers(GenericAPIView, ListModelMixin):
    def get(self,request:Request):
        queryset = MyUser.objects.all()
        users = UserSerializer(queryset, many=True)
        return Response(users.data, status=status.HTTP_200_OK)

class SignUp(GenericAPIView, CreateModelMixin):
    def post(self, request:Request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message" : "User has been created", "Data": serializer.data}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)