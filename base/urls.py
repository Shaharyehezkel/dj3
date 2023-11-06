from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.product),
    path('login/',  views.MyTokenObtainPairView.as_view()),
    path('members/',views.members),
    path('register/',views.register),
    path('products/',views.Product_View.as_view()),
    path('products/<int:id>',views.Product_View.as_view()),
    path('categories/',views.Category_View.as_view()),

]
