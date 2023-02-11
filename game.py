from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("************************")
        print(" WELCOME TO TICTACTOE")
        print("************************")
        
    
        board = Board()
        player = Player()
        computer =Player(False)

        board.print_board()
         
        while(True):  #game
                  
            while(True): #round

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("ITS A TIE! TRY AGAIN ")
                    break 
                elif board.check_is_game_over(player, player_move):
                    print("AWESOME! YOU WON THE GAME")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("OOPS... COMPUTER WON. TRY AGAIN ")
                        break 
        
            play_again = input("WOULD YOU LIKE TO PLAY AGAIN ? ENTER X FOR YES OR O FOR NO").upper()

            if play_again =="O":
                print("Bye! come back soon ")
                break 
        
            elif play_again =="X":
                self.start_new_round(board)
        
            else:
                print("Your input was not valid but i assume you want to play again")
                self.start_new_round(board)
        
    def start_new_round(self, board):
        print("***************")
        print("NEW ROUND ")
        print("***************")
        board.reset_board()
        board.print_board()

game = TicTacToeGame()
game.start()


