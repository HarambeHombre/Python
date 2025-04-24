#Create a blank tic-tac-toe library where values "X" and "O" will be stored.

#Build grid values that will later be overridden
values_dict = {1:1,
          2:2,
          3:3,
          4:4,
          5:5,
          6:6,
          7:7,
          8:8,
          9:9,}

# Grid values that will be removed as they are added on grid, when no more values game should result in a tie.
tie_check = {1:1,
          2:2,
          3:3,
          4:4,
          5:5,
          6:6,
          7:7,
          8:8,
          9:9,}

# Show initial playing area.
print(f'''
Tic-tac-toe
 {values_dict[1]} | {values_dict[2]} | {values_dict[3]}
---+---+---
 {values_dict[4]} | {values_dict[5]} | {values_dict[6]}
---+---+---
 {values_dict[7]} | {values_dict[8]} | {values_dict[9]}
    ''')

game_on = True
# Run game until game_on is false.
while game_on:
    # Take user input to see who is playing, and then choose a space on the gameboard to place the X or O
    user_selection = input('Type either "X" or "O" to select who\'s turn it is: ').upper()

    # Logic checks to make sure user only can type X or O, used upper to make sure no errors would occur for a lower case entry
    if user_selection != 'X' and user_selection != 'O':
        print('Not valid, please try again.')
    else:
        grid_location = input(f'Input a number from above to add an "{user_selection}" to that space: ')

        # Logic check to make sure grid_location can only be a number in values_dict
        if int(grid_location) in values_dict:
            for g_value in values_dict:
                if int(grid_location) == g_value:
                    # Logic checks to make sure X does not override O and vice versa
                    if values_dict[g_value] != 'X' and values_dict[g_value] != 'O':
                        values_dict.update({g_value: user_selection})
                        tie_check.pop(g_value)
                    else:
                        print('Space already taken, try again.')
        else:
            print('Not a valid grid space, please try again.')


    #Create the actual board that will be played on. Inputting a number from below will assign either "X" or "O" to that spot and update the display.
    playing_area = f'''
    Tic-tac-toe
     {values_dict[1]} | {values_dict[2]} | {values_dict[3]}
    ---+---+---
     {values_dict[4]} | {values_dict[5]} | {values_dict[6]}
    ---+---+---
     {values_dict[7]} | {values_dict[8]} | {values_dict[9]}
        '''

    print(playing_area)


    # Logic checks to see if anyone won, or tied.
    if not tie_check:
        print('Tie Game!')
        game_on = False

    if values_dict[1] == 'X' and values_dict[2] == 'X' and values_dict[3] == 'X':
        print('"X" wins!')
        game_on = False
    if values_dict[4] == 'X' and values_dict[5] == 'X' and values_dict[6] == 'X':
        print('"X" wins!')
        game_on = False
    if values_dict[7] == 'X' and values_dict[8] == 'X' and values_dict[9] == 'X':
        print('"X" wins!')
        game_on = False
    if values_dict[1] == 'X' and values_dict[4] == 'X' and values_dict[7] == 'X':
        print('"X" wins!')
        game_on = False
    if values_dict[2] == 'X' and values_dict[5] == 'X' and values_dict[8] == 'X':
        print('"X" wins!')
        game_on = False
    if values_dict[3] == 'X' and values_dict[6] == 'X' and values_dict[9] == 'X':
        print('"X" wins!')
        game_on = False
    if values_dict[1] == 'X' and values_dict[5] == 'X' and values_dict[9] == 'X':
        print('"X" wins!')
        game_on = False
    if values_dict[3] == 'X' and values_dict[5] == 'X' and values_dict[7] == 'X':
        print('"X" wins!')
        game_on = False
        
    if values_dict[1] == 'O' and values_dict[2] == 'O' and values_dict[3] == 'O':
        print('"O" wins!')
        game_on = False
    if values_dict[4] == 'O' and values_dict[5] == 'O' and values_dict[6] == 'O':
        print('"O" wins!')
        game_on = False
    if values_dict[7] == 'O' and values_dict[8] == 'O' and values_dict[9] == 'O':
        print('"O" wins!')
        game_on = False
    if values_dict[1] == 'O' and values_dict[4] == 'O' and values_dict[7] == 'O':
        print('"O" wins!')
        game_on = False
    if values_dict[2] == 'O' and values_dict[5] == 'O' and values_dict[8] == 'O':
        print('"O" wins!')
        game_on = False
    if values_dict[3] == 'O' and values_dict[6] == 'O' and values_dict[9] == 'O':
        print('"O" wins!')
        game_on = False
    if values_dict[1] == 'O' and values_dict[5] == 'O' and values_dict[9] == 'O':
        print('"O" wins!')
        game_on = False
    if values_dict[3] == 'O' and values_dict[5] == 'O' and values_dict[7] == 'O':
        print('"O" wins!')
        game_on = False