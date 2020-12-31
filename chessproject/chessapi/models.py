from django.db import models


class Piece(models.Model):
    type = models.CharField(max_length=6, choices=[
        ('Pawn', 'Pawn'),
        ('Bishop', 'Bishop'),
        ('Knight', 'Knight'),
        ('Rook', 'Rook'),
        ('Queen', 'Queen'),
        ('King', 'King'),
    ])
    color = models.CharField(max_length=5, choices=[
        ('white', 'white'),
        ('black', 'black'),
    ])
