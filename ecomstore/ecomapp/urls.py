from django.contrib import admin
from django.urls import path, include


from .views import ListCloths, DetailView, AddToCartView

urlpatterns = [

    path('list_cloths/', ListCloths.as_view(), name='cloths'),
    path('details-view/<int:pk>/', DetailView.as_view(), name='details'),
    path('update-view/<int:pk>/', DetailView.as_view(), name='update'),
    path('delete-view/<int:pk>/', DetailView.as_view(), name='update'),
    path('add-to-cart/',AddToCartView.as_view(),name='add-to-cart')

]
