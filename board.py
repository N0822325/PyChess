board = [[None for x in range(8)] for y in range(8)]


def cls():
    global board
    board= [[None for x in range(8)] for y in range(8)]
#resets to an 8x8 board of null values


def set(objects):
    cls()
    for i in objects:
        for j in i:
            if j == None:
                continue
            board [j.pos[0]] [j.pos[1]] = j
#replaces all null values with relevant objects
    
    
    
def disp():
    x = 65
    for i in board:
        y = 1
        print("\n",chr(x))
        for j in i:
            print(str(y) + ": ", end="")
            try:
                print(j.name)
            except:
                print(None)
            y += 1
        x += 1
#Displays the current board with locations of each piece
