from rest_framework import serializers
from rest_framework.validators import ValidationError
from account.models import MyUser


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=60)
    first_name = serializers.CharField(max_length=60)
    last_name = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['id','username','email','first_name','last_name','password']


    def validate(self, attrs):
        email_exist = MyUser.objects.filter(email=attrs['email']).exists()
        username_exist = MyUser.objects.filter(username=attrs['username']).exists()
        if email_exist:
            raise ValidationError("This email is already in use")
        if username_exist:
            raise ValidationError("This username already taken")

        return super().validate(attrs)
    
