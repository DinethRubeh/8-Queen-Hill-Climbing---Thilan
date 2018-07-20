from __future__ import print_function
import random


board = [0,0,0,0,0,0,0,0]
# board = [0,1,2,3,4,5,6,7]

def show_board(board_p):

    new_board = []
    for i in range(len(board)):
        new_board.append([i,board_p[i]])

    print(new_board)

    for i in range(len(board)):
        for j in range(len(board)):
            if [j,i] in new_board:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def determine_h_cost(board):
    h = 0

    #check all queens
    for i in range(len(board)):
        #check interaction with remaining queens
        for j in range(i+1,len(board)):
            #if queen in same column
            if board[i] == board[j]:
                h += 1

            #get offset
            offset = i - j

            #check if there is diagonal interaction
            if board[i] == board[j] + offset or board[i] == board[j] - offset:
                h += 1
    return h

# print(determine_h_cost(board))
# show_board(board)




def best_move(board):

    moves = []
    moves.append([board,determine_h_cost(board)])
    for col in range(len(board)):
        for row in range(len(board)):
            board_copy = list(board)
            if board[col] == row:
                continue
            board_copy[col] = row
            # show_board(board_copy)
            cost_of_state = determine_h_cost(board_copy)
            moves.append([board_copy,cost_of_state])

    # for row in moves:
    #     print(row)

    current = determine_h_cost(board)
    # print(current)
    for row in moves:
        if row[1]<current:
            current = row[1]

    # print(current)

    best_moves = []
    for row in moves:
        if row[1] == current:
            best_moves.append(row[0])

    # for row in best_moves:
    #     print(row)

    next_move = random.choice(best_moves)

    # # print()
    # print(next_move)

    return next_move


# board_next_state = best_move(board)
#
# print(board_next_state)

show_board(board)
print("h = " + str(determine_h_cost(board)))
print()

action_sequence = []

h_cost = determine_h_cost(board)
action_sequence.append([board,h_cost])

number_of_steps = 0
state = 1
while(state == 1):
    board_next_state = best_move(board)
    if board == board_next_state or h_cost == determine_h_cost(board_next_state):
        state = 0
        show_board(board)
        cost = determine_h_cost(board)
        print("h = " + str(cost))
        if cost == 0:
            print("Reached Global Maximum!")
            print()
        else:
            print("Stuck at Local Maximum")
            print()
    else:
        board = board_next_state
        state = 1
        h_cost = determine_h_cost(board)
        action_sequence.append([board,h_cost])
        number_of_steps += 1
        show_board(board)


print("Steps taken: ")
for row in action_sequence:
    print(row)

print()
print("Number of steps: " + str(number_of_steps))











