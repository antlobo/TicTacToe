import copy


class TicTacToe:
    """
    A class to handle all current game data and carry out game functions
    """
    _TICTACTOE_VALUES = {1: "X", 2: "O"}

    _DEFAULT_TICTACTOE_GAME_BOARD = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    _WINNER = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def __init__(self):
        self.end = False

        self._current_player_num = 1
        self._number_plays = 9
        self._tictactoe = copy.deepcopy(self._DEFAULT_TICTACTOE_GAME_BOARD)
        self._winner = None

    @property
    def current_player(self) -> str:
        """
        Name of the current player
        :return: a string with the name of the current player X or O
        """
        return self._TICTACTOE_VALUES[self._current_player_num]

    @property
    def remaining_plays(self) -> int:
        """
        Number of plays remaining, starts at 9
        :return: an integer that represents the quantity of the remaining plays available
        """
        return self._number_plays

    @property
    def winner_name(self) -> str:
        """
        Name of the winner, default value is None
        :return: string with the name of the winner X or O
        """
        return self._winner

    @property
    def possible_plays(self) -> list:
        """
        Possible plays available
        :return: list of the possible plays available
        """
        possible_numbers_play = [item for row in self._tictactoe for item in row if item not in ("X", "O")]
        return possible_numbers_play

    def show_game_board(self, possible_play: bool = False) -> str:
        """
        Creates a representation of the current TicTacToe game board
        :param possible_play: if True, prints the game board with the possible plays else prints the
        game board with 'X's and 'O's
        :return: string with the representation of the game board
        """
        board = ""
        for i, row in enumerate(self._tictactoe, 0):
            for j, value in enumerate(row, 0):
                if possible_play:
                    value_to_print = value
                else:
                    value_to_print = value if value in ("X", "O") else " "
                if j <= 1:
                    board += f"{value_to_print} | "
                else:
                    board += f"{value_to_print} \n"
            if i <= 1:
                board += f"--|---|--\n"
        return board

    def play_turn(self, number_play) -> None:
        """
        Sets the name of the player in the board at the spot number: number_play
        :param number_play: number of the spot played by the user
        """
        for i, row in enumerate(self._tictactoe, 0):
            for j, value in enumerate(row, 0):
                if value == number_play:
                    self._tictactoe[i][j] = self.current_player

        self._check_winner()
        self._number_plays -= 1
        self._current_player_num = 2 if self._current_player_num == 1 else 1
        if self.remaining_plays == 0:
            self.end = True

    def _check_winner(self) -> None:
        """
        Checks if there is a winner and sets the variables '_winner' with the winner's name and 'end' with a True
        """
        for row in self._WINNER:
            if self._winner:
                break
            (a1, a2), (b1, b2), (c1, c2) = row
            if self._tictactoe[a1][a2] == self._tictactoe[b1][b2] == self._tictactoe[c1][c2]:
                self._winner = self._tictactoe[a1][a2]
                self.end = True
