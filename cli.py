from tictactoe import TicTacToe

if __name__ == '__main__':
    single_player = input("Single player mode? (y/n): ").lower() == 'y'
    game = TicTacToe(single_player)
    game.play_game()
