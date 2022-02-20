import itertools
play = True
players = [1, 2]
game = []
 
def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (/)")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (\\)")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):

    try:
        if game_map[row][column] != 0:
          print("This space is occupied, try another!")
          return False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
          game_map[row][column] = player
        for count, row in enumerate(game_map):
          print (count, row)
        return True
    except IndexError:
        print("Did you attempt to play a row or column outside the range?")
        return False
    except Exception as e:
        print(str(e))
        return False


play = True
players = [1, 2]
while play:
    
    game_size = int(input("What size game TicTacToe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)] 
    game_won = False
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Player: {current_player}")
            column_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            played = game_board(game, current_player, row_choice, column_choice)
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting!")
            elif again.lower() == "n":
                print("Byeeeee!!!")
                play = False
            else:
                print("Not a valid answer, but... see ya!")
                play = False
