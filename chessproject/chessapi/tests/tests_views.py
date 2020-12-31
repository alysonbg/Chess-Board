from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from chessproject.chessapi.models import Piece


class PiecesViewTestCase(APITestCase):
    def test_create_a_new_piece(self):
        """
        Ensures that is possible to create a new piece
        """
        url = reverse('pieces')
        data = {'type': 'Knight', 'color': 'white'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Piece.objects.count(), 1)

    def test_that_is_not_possible_create_an_invalid_piece(self):
        """
        Ensures that is not possible to create an invalid piece
        """
        url = reverse('pieces')
        data = {'type': 'Turtle', 'color': 'purple'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
