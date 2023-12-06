def draw_board():
    turtle.pencolor('light gray') #change the color of the ink of the turtle drawing, which is hidden then it is the color of the boxes of the tic tac toe
    turtle.pensize(10) #change the thickness of the lines that the turtle draws
    turtle.up() #lift the pen (stop drawing)
    turtle.goto(-3, -1) #move the turtle to the specified coordinates (-3, -1)
    turtle.seth(0) #set the orientation of the turtle to 0 degrees (facing right)
    turtle.down() #lower the pen (start drawing)
    turtle.forward(6) #move the turtle forward by 6 units, drawing a horizontal line
    turtle.up() #lift the pen (stop drawing)
    turtle.goto(-3, 1) #move the turtle to the specified coordinates (-3, -1)
    turtle.seth(0) #set the orientation of the turtle to 0 degrees (facing right)
    turtle.down() #lower the pen (start drawing)
    turtle.fd(6) #move the turtle forward by 6 units, drawing another horizontal line
    turtle.up() #lift the pen (stop drawing)
    turtle.goto(-1, -3) #move the turtle to the specified coordinates (-3, -1)
    turtle.seth(90) #set the orientation of the turtle to 90 degrees (facing upward)
    turtle.down() #lower the pen (start drawing)
    turtle.fd(6)#move the turtle forward by 6 units, drawing another horizontal line
    turtle.up()#lift the pen (stop drawing)
    turtle.goto(1, -3)#move the turtle to the specified coordinates (-3, -1)
    turtle.seth(90) #set the orientation of the turtle to 0 degrees (facing right)
    turtle.down()#lower the pen (start drawing)
    turtle.fd(6)#move the turtle forward by 6 units, drawing another horizontal line
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

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #initialize the tic-tac-toe board with empty cells
draw(b) #draw the initial state of the board
turn = 'x' #set the initial player turn to 'x'
screen.onclick(play) #set up an event listener for mouse clicks on the turtle graphics screen
turtle.mainloop() #start the main event loop to listen for user input and update the screen

