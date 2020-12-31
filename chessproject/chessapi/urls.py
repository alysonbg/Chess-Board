from django.urls import path
from chessproject.chessapi import views

urlpatterns = [
    path('pieces/', views.pieces, name='pieces')
]
