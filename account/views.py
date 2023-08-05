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
    