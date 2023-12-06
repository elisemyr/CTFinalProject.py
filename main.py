def draw_x(x, y):
    turtle.color('light blue') #set the color of the pen to light blue
    turtle.up()#lift the pen (stop drawing)
    turtle.goto(x - 0.75, y - 0.75) #move the turtle to the specified coordinates (x - 0.75, y - 0.75)
    turtle.down() #lower the pen (start drawing)
    turtle.goto(x + 0.75, y + 0.75) #move the turtle to the specified coordinates (x + 0.75, y + 0.75)
    turtle.up()#lift the pen (stop drawing)
    turtle.goto(x - 0.75, y + 0.75) #move the turtle to the specified coordinates (x - 0.75, y + 0.75)
    turtle.down() #lower the pen (start drawing)
    turtle.goto(x + 0.75, y - 0.75)#move the turtle to the specified coordinates (x + 0.75, y - 0.75)



def play(x, y): #function to handle player moves when a click occurs on the turtle graphics screen
    global turn #use the global variable 'turn' to keep track of the current player
    i = 3 - int(y + 5) // 2 #calculate the row (i) and column (j) based on the click coordinates
    j = int(x + 5) // 2 - 1
    if i > 2 or j > 2 or i < 0 or j < 0 or b[i][j] != 0: return #check if the calculated position is out of bounds or if the cell is already occupied
    if turn == 'x': #update the board based on the player's move and switch the player turn
        b[i][j], turn = 1, 'o'
    else:
        b[i][j], turn = 2, 'x'
    draw(b)  #redraw the updated board
    r = gameover(b) #check if the game is over
    if r == 1:
        display_message("Game over! X won!")  #display a message based on the game result
    elif r == 2:
        display_message("Game over! O won!")
    elif r == 3:
        display_message("This is a Tie!")

