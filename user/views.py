from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status,generics
from user.models import Account

from django.core.mail import send_mail

# Create your views here.

@api_view(["POST", ])
def registration_view(request):
    if request.method=="POST":
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()

            send_mail('Your account has been registered', 'Hai, account.username,
            Thank you for registering in Nirang. ......... , 'donotreply@private.com', ['email'], fail_silently=False)
            
            data['response'] = "succesfully registered"
            data['email']=account.email
            data['username']=account.username
        else:
            data=serializer.errors
        return Response(data)

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=RegistrationSerializer
