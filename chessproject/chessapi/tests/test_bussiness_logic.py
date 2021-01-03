import unittest

from chessproject.chessapi.bussiness_logic import _find_knight_next_moves, find_knight_moves_for_the_next_two_turns


class BussinessLogicTest(unittest.TestCase):
    def test_find_knight_next_moves(self):
        """
        Ensures that the function find_knight_next_moves returns
        the next moves of a Knight
        :return: A list of the Knight next moves
        """
        result = _find_knight_next_moves('d4')
        self.assertEqual(['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5'],
                         result
                         )

    def test_find_knight_next_moves_limit_of_board(self):
        """
        Ensures that the function find_knight_next_moves does not
        return moves that are beyond the board limits
        :return: a list of the Knight next moves
        """
        result = _find_knight_next_moves('h1')
        self.assertEqual(['f2', 'g3'], result)

    def test_find_knight_move_for_next_2_turns(self):
        """
        Ensures that the function find_knight_moves_for_the_next_two_turns
        returns the moves for the next 2 turns of a piece of the type Knight
        :return: a list of the Knight next moves for the next 2 turns
        """
        result = find_knight_moves_for_the_next_two_turns('h1')
        self.assertEqual(['d3', 'e2', 'e4', 'f5', 'g4', 'h3', 'h5'], result)
