# Global Variable

# board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# If game is still going
game_still_going = True

#Winer or Tie
winner = None

current_player = "X"

# Display the game board to the screen
def display_board():
  print()
  print(board[0] + "|" + board[1] + "|" + board[2])
  print('-+-+-')
  print(board[3] + "|" + board[4] + "|" + board[5])
  print('-+-+-')
  print(board[6] + "|" + board[7] + "|" + board[8])
  print()
# ------------- Functions ---------------

# Main
def main():

  # Show the initial game board
  display_board()

  while game_still_going:
   
   #handle a single turn of an arbitrary player
    handle_turn(current_player)

    #check if the game is over
    game_over()

    #Flip to the other player
    next_player()

    #Game ended
    if winner == "x" or winner == "o" or winner == None:
      print("Good game. Thank for playing!")
    


# Handle a turn for an arbitrary player
def handle_turn(player):
  position = input("'s turn to choose a square (1-9): ")
  position = int(position) - 1

  board[position] = "x"
  display_board()

def game_over():
 check_for_winner()
 checl_if_tie()
   
def winner_check():

     global winner

     row = check_rows()
     columns = check_columns()
     diagonal = check_diagonal()
     if row:
         winner = row()
     elif columns:
           winner = columns()
     elif diagonal:
             winner = diagonal()
     else:
             winner = None
             return

     #def tie_check():
      ## return

#def net_player():
  #return

main()


