import turtle #importing the turtle module for graphics

#set up the turtle screen
screen = turtle.Screen() #create a turtle graphics screen
screen.setup(864, 864) #set up the dimensions of the screen (width: 864 pixels, height: 864 pixels)
screen.title("Tic Tac Toe @ 2 Players") #set the title of the turtle graphics window
screen.setworldcoordinates(-5, -5, 5, 5) ## Set the world coordinates for the turtle graphics screen, the visible area will be from (-5, -5) to (5, 5) with the center at (0, 0)
screen.bgpic("gradsquare.gif") #set background image
screen.tracer(0, 0) #turn off automatic screen updates
turtle.hideturtle() #hide the default turtle cursor

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

def draw_circle(x, y):
    turtle.up() #lift the pen (stop drawing)
    turtle.goto(x, y - 0.75) #move the turtle to the specified coordinates (x, y - 0.75)
    turtle.seth(0) #set the orientation of the turtle to 0 degrees (facing right)
    turtle.pencolor('magenta') #change the color of the ink of the turtle drawing ( the O circle from tic tac toe game)
    turtle.down() #lower the pen (start drawing)
    turtle.circle(0.75, steps=100) #draw a circle with a radius of 0.75 units, using 100 steps for a smoother circle


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


def draw_piece(i, j, p): #function to draw a game piece on the tic-tac-toe board at position (i, j) with player type p
    if p == 0: return #check if the piece is empty (p == 0), if so, return without drawing
    x, y = 2 * (j - 1), -2 * (i - 1) #calculate the coordinates (x, y) based on the board position (i, j)
    if p == 1: #if the player type is 1, draw an 'X' at the calculated coordinates
        draw_x(x, y)
    else:#if the player type is 2, draw a circle at the calculated coordinates
        draw_circle(x, y)
def draw(b): #function to draw the entire tic-tac-toe board based on the current state (b)
    draw_board() #draw the tic-tac-toe board
    for i in range(3): #iterate through each cell in the board
        for j in range(3):
            draw_piece(i, j, b[i][j]) #draw the piece at the current cell based on the player type in the board state (b)
    screen.update() #update the screen to display the changes

# return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
def gameover(b): #function to check if the game is over and return the result
    #row checks
    if b[0][0] > 0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
    if b[1][0] > 0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
    if b[2][0] > 0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
     #column checks   
    if b[0][0] > 0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
    if b[0][1] > 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
    if b[0][2] > 0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
    #diagonal checks
    if b[0][0] > 0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
    if b[2][0] > 0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
    #check for a tie (all cells filled)
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p == 9:
        return 3 #tie
    else:
        return 0 #if no win or tie, return 0 (game not over)

def display_message(message):  
    # Display the message in the center of the new window
    turtle.penup() #lift the pen (stop drawing)
    turtle.goto(0, 0) #move the turtle to the center of the window (coordinates 0, 0)
    turtle.pendown() #lower the pen (start drawing)
    turtle.color('black') #set the pen color to black
    turtle.write(message, align="center", font=("Courier New", 50, "normal")) #write the message on the screen with specified alignment and font

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
        turtle.ontimer(turtle.bye, 2000) #exits the turtle screen after 2 seconds 
    elif r == 2:
        display_message("Game over! O won!")
        turtle.ontimer(turtle.bye, 2000)
    elif r == 3:
        display_message("This is a Tie!")
        turtle.ontimer(turtle.bye, 2000)

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #initialize the tic-tac-toe board with empty cells
draw(b) #draw the initial state of the board
turn = 'x' #set the initial player turn to 'x'
screen.onclick(play) #set up an event listener for mouse clicks on the turtle graphics screen
turtle.mainloop() #start the main event loop to listen for user input and update the screen

