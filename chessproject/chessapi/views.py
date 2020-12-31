from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from chessproject.chessapi.serializers import PieceSerializer


@api_view(['POST'])
def pieces(request):
    if request.method == 'POST':
        serializer = PieceSerializer(data=request.data)
        if serializer.is_valid():
            piece = serializer.save()
            return Response(data={'id': piece.id}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
