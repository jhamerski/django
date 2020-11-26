from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto) # neste linha chamo o método
]
