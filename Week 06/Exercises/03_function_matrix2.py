#Please write a function named who_won(game_board: list), which takes a
#two-dimensional array as its argument. The array consists of integer values,
#which represent the following situations:

    #0: empty square
    #1: player 1 game piece
    #2: player 2 game piece

#In this exercise it is enough to compare the number of pieces each player has
#on the game board

#The function should return the value 1 if player 1 won, and the value 2 if
#player 2 won. If both players have the same number of pieces on the board,
#the function should return the value 0.

def who_won(game_board: list):
    score_cnt = [0,0]
    winner = 0
    
    for row in game_board:
        for num in row:
            if num == 1:
                score_cnt[0] += 1
            elif num == 2:
                score_cnt[1] += 1
            else:
                continue

            print(score_cnt)

    if score_cnt[0] == score_cnt[1]:
        winner = 0
    elif score_cnt[0] > score_cnt[1]:
        winner = 1
    else:
        winner = 2

    return winner

if __name__ == "__main__":
    play = [[0,1,2,1,1,1,1,1], [0,1,2,1,1,1,1,1], [0,1,2,1,1,1,1,1]]
    print(f"Winner: {who_won(play)}") 
