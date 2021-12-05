from tic_tac_toe import TicTacToe


def main():
    while True:
        ttt = TicTacToe()
        while not ttt.end:
            print(ttt.show_game_board())
            input("Press enter to continue... \n")

            print(ttt.show_game_board(True))
            possible_plays = ttt.possible_plays

            good_play = False
            while not good_play:
                try:
                    number_play = int(input(f"Write the number of the possible "
                                            f"play for the player '{ttt.current_player}': "))
                except ValueError:
                    print(f"[Error] That was not a valid number")
                else:
                    if number_play in possible_plays:
                        ttt.play_turn(number_play)
                        good_play = True
                    else:
                        print(f"[Error] That was not a possible play")

        if ttt.winner_name:
            print(f"\nWinner is '{ttt.winner_name}'")
        else:
            print(f"\nThere is no winner")

        if not input("\nWant to keep playing? write 'yes' or 'no': \n").lower() == "yes":
            break


if __name__ == '__main__':
    main()
