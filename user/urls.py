
from django.urls import path,include
from user import views

urlpatterns = [
    path('register/',views.registration_view,name="register"),
    path('rest-auth/',include('rest_auth.urls')),

]
