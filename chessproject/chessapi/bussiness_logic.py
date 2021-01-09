def _find_knight_next_moves(position):
    """
    Receives a position in algebric notation and returns a list moves that are possible
    :param position: A position in algebric notation
    :return: A list of the moves that are possible
    """
    letters = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
    }
    numbers_to_letters = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
    }
    moves = []

    column, row = letters[position[0]], int(position[1])

    possible_moves = [
        (column - 2, row - 1),
        (column - 2, row + 1),
        (column - 1, row - 2),
        (column - 1, row + 2),
        (column + 1, row - 2),
        (column + 1, row + 2),
        (column + 2, row - 1),
        (column + 2, row + 1),
    ]

    for move in possible_moves:
        if 1 < move[0] <= 8 and 1 < move[1] <= 8:
            formatted_move = f'{numbers_to_letters[move[0]]}{move[1]}'
            moves.append(formatted_move)

    return moves


def find_knight_moves_for_the_next_two_turns(position):
    next_moves = _find_knight_next_moves(position)
    second_turn_moves = []
    for move in next_moves:
        next_turn_moves = _find_knight_next_moves(move)
        for next_turn_move in next_turn_moves:
            second_turn_moves.append(next_turn_move)

    return sorted(list(set(next_moves + second_turn_moves)))
