from django.urls import path
from chessproject.chessapi import views

urlpatterns = [
    path('pieces/', views.pieces, name='pieces'),
    path('moves/<int:pk>', views.moves, name='moves')
]
