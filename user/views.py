from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status,generics
from user.models import Account
# Create your views here.

@api_view(["POST", ])
def registration_view(request):
    if request.method=="POST":
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response'] = "succesfully registered"
            data['email']=account.email
            data['username']=account.username
        else:
            data=serializer.errors
        return Response(data)

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=RegistrationSerializer
