# x represents the rows (i)
# y represents the cols (j)

# GLOBAL VARIABLES:
keys = ['C', 'P', 'A', 'B'];        # Keys for printing symbols on the board
dx = [0,0,1,-1]                     # Moving in x-axis
dy = [1,-1,0,0]                     # Moving in y-axis
flag_state = 0                      # 0 = not with the flag; 1 = just picked up the flag; 2 = with the flag; 

# ---===---===---=*=---===---===--- #

# Initializing cordinates from user input
def initBoard(): #void
    global px, py, cx, cy, ax, ay, bx, by
    px = int(input()); py = int(input());       # Percy cordinates
    cx = int(input()); cy = int(input());       # Clarrise Cordinates
    ax = int(input()); ay = int(input());       # Water Cordinates
    bx = int(input()); by = int(input());       # Flag Cordinates


def printBoard(): #void
    flush(); # Update the main_cord list
    for i in range(8):
        for j in range(8):
            if [i,j] not in main_cord:      # If coordinates aren't in main_cord, print an hyphen 
                print('-', end = '');
            else:                           # Otherwise, print the corresponding key
                                            # Since Percy and Clarissa cames before     
                index = main_cord.index([i,j])
                print(keys[index], end='');

            print(' ',end='') if j != 7 else print()    # Print a space after each row and a newline on the last one

# Update the main_cord list with current coordinates
def flush(): #void
    global main_cord
    # Clarrise cordinates comes first to override percy if she gets in the same spot.
    main_cord = [[cx,cy], [px,py], [ax,ay], [bx,by]]; 


def clarisse_move(): # bool
    global cx, cy, px, py
    if cy != py:
        if cy > py:
            cy -= 1;
        elif cy < py:
            cy += 1;
    else:       # When they're on the same collumn
        if cx > px:
            cx -= 1;
        elif cx < px:
            cx += 1;

    if cx == px and cy == py:
        return 1

    return 0


def check_clarisse(): # bool
    global cx, ax, cy, ay
    if cx == ax and cy == ay:       # if clarrisa enters the water field
        return  1
    return 0


def percy_move():
    global px, py, ax, ay
    move = input()

    if move == "direita": d=0
    elif move == "esquerda": d=1
    elif move == "baixo": d=2
    elif move == "cima": d=3

    px += dx[d]; py += dy[d];           # Make one move in the assigned direction

    if px == ax and py == ay: 
        print("Sinto o poder de Poseidon em minhas veias!")
        px += dx[d]; py += dy[d];       # Make another move in the assigned direction if percy enter water  


def percy_win(): #void
    print("Vitória!! Nunca subestime o cabeça de alga!")
    printBoard()


def clarisse_win(): #void
    print("Ah não, Annabeth vai me matar...")
    printBoard()


def check_flag(): # int
    global px, pt, bx, by
    if px == bx and py == by:       # If he pick up the flag
        bx = -1; by = -1;           # Put the flag outside the board
        return 1;                   # Define the flag_state to 1 (has just picked it up)

    return 0                        # Otherwise, mantain flag_state in 0 (not picked up yet); 


def printStatement(): #void
    global flag_state

    if flag_state == 0:
        print("Preciso pegar aquela maldita bandeira vermelha.")
    elif flag_state == 1:
        print("Isso! Consegui a bandeira!")
        flag_state += 1
    elif flag_state == 2:
        print("Agora eu só preciso meter o pé daqui!")


def main():
    global flag_state

    initBoard();
    flush();

    # printBoard()

    while(1) :
        if clarisse_move(): clarisse_win(); break;          # If clarisse reaches percy, she win.
        if check_clarisse(): percy_win(); break;            # If clarisse enter water, percy win.
        
        percy_move()
        if not flag_state: flag_state = check_flag()        # Check if the the flag was picked up in this round.

        # If the flag was already picked up and percy are in the first row, percy win.
        if flag_state and px == 0: percy_win(); break;

        printStatement()
        printBoard()
        print()
        
    return 1


main()
