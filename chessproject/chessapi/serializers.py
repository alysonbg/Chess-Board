from rest_framework import serializers

from chessproject.chessapi.models import Piece


class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ['type', 'color']
