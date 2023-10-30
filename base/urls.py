from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('',views.prodoct),
    path('login/', TokenObtainPairView.as_view()),
    path('members/',views.members),
    path('register/',views.register),

]
