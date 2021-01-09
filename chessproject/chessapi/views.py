from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from chessproject.chessapi.models import Piece
from chessproject.chessapi.serializers import PieceSerializer
from chessproject.chessapi.bussiness_logic import find_knight_moves_for_the_next_two_turns


@api_view(['POST'])
def pieces(request):
    if request.method == 'POST':
        serializer = PieceSerializer(data=request.data)
        if serializer.is_valid():
            piece = serializer.save()
            return Response(data={'id': piece.id}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def moves(request, pk):
    try:
        piece = Piece.objects.get(pk=pk)
    except Piece.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if piece.type == 'Knight':
            position = request.query_params.get('coordinate', None)
            if position:
                next_possible_moves = find_knight_moves_for_the_next_two_turns(position)
                return Response(data=next_possible_moves, status=status.HTTP_200_OK)
            return Response(status=400)

        else:
            return Response(data=[], status=200)
