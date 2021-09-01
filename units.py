knightBool = False

class UnitTemplate(object):

    def __str__(self):
        info = '\nUnit: ' + self.name
        info += '\nPosition: ' + str(self.pos)
        return info

    def move(self, arr, movePos):
        self.hasMoved = True
        if not(arr[movePos[0]][movePos[1]] == None):
            arr[movePos[0]][movePos[1]].die()
        self.pos = movePos

    def createSpawn(self,spawnPos):
        import pygame
        self.pos = spawnPos
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))


class WhitePawn(UnitTemplate):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/WhitePawn.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = 1
        self.name = 'wPawn' + str(WhitePawn.count + 1)
        self.pos = [WhitePawn.count, 1]
        WhitePawn.count += 1
        self.hasMoved = False

    def knight():
        i = int(input("1-queen 2-rook 3-bishop 4-knight"))
        if i == 1:
            wQueens.append(WhiteQueen())
            wQueens[-1].createSpawn(self.pos)
        elif i == 2:
            wRooks.append(WhiteRook())
            wRooks[-1].createSpawn(self.pos)
        elif i == 3:
            wBishops.append(WhiteBishop())
            wBishops[-1].createSpawn(self.pos)
        elif i == 4:
            wKnights.append(WhiteKnight())
            wKnights[-1].createSpawn(self.pos)
            
        self.die()

    def move(self, arr, movePos):
        self.hasMoved = True
        if not(arr[movePos[0]][movePos[1]] == None):
            arr[movePos[0]][movePos[1]].die()

        self.pos = movePos
        if self.pos[1] == 7 or self.pos[1] == 0:
            global knightBool            
            knightBool = True
            

    def moveOptions(self, arr):
        x, y = self.pos
        moveSpaces = [[x, y + 2 * self.team], [x, y + 1 * self.team], [x + 1, y + 1 * self.team], [x - 1, y + 1 * self.team]]
        if self.hasMoved:
            moveSpaces[0] = []
        for i in range(0, 2):
            try:
                if not arr[moveSpaces[i][0]][moveSpaces[i][1]] == None:
                    raise
            except:
                moveSpaces[i] = []

        for i in range(2, 4):
            try:
                if arr[moveSpaces[i][0]][moveSpaces[i][1]].team == self.team:
                    raise
            except:
                moveSpaces[i] = []

            self.isAttacking = True

        for i in moveSpaces:
            for j in i:
                if j < 0:
                    moveSpaces[moveSpaces.index(i)] = []


        temp = moveSpaces[:]
        for i in temp:
            if not i:
                del moveSpaces[moveSpaces.index(i)]

        return moveSpaces
        
    def die(self):
        wPawns[ int(self.name[-1]) - 1] = None


class BlackPawn(WhitePawn):
    count = 0
    
    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/BlackPawn.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = -1
        self.name = "bPawn" + str(BlackPawn.count + 1)
        self.pos = [ BlackPawn.count, 6]
        BlackPawn.count += 1
        self.hasMoved = False


    def die(self):
        bPawns[ int(self.name[-1]) - 1] = None

class WhiteRook(UnitTemplate):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/WhiteRook.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = 1
        self.pos = [ 0 + (7 * WhiteRook.count),0]

        WhiteRook.count += 1
        self.name = "wRook" + str(WhiteRook.count)

    def moveOptions(self, arr):
        x, y = self.pos
        moveSpaces = [ [[x, i] for i in range(y+1,8)] , [[x, i] for i in range(y-1,-1,-1)], [[i, y] for i in range(x+1,8)], [[i, y] for i in range(x-1,-1,-1)] ]

        for count in range(0,4):
            for i in moveSpaces[count]:
                if arr[i[0]][i[1]] == None:
                    pass
                elif not(arr[ i[0] ][ i[1] ].team == self.team):
                    moveSpaces[count] = moveSpaces[count][ :moveSpaces[count].index(i)+1 ]
                    break
                else:
                    moveSpaces[count] = moveSpaces[count][ :moveSpaces[count].index(i) ]
                    break

      
        temp = []
        for i in moveSpaces:
            for j in i:
                if j:
                    temp.append(j)
        
        moveSpaces = temp
        return moveSpaces
    
    def die(self):
        wRooks[ int(self.name[-1]) - 1] = None


class BlackRook(WhiteRook):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/BlackRook.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = -1
        self.pos = [ 0 + (7 * abs(BlackRook.count)),7]
        
        BlackRook.count += 1
        self.name = "bRook" + str(BlackRook.count)    

    def die(self):
        bRooks[ int(self.name[-1]) - 1] = None




class WhiteQueen(UnitTemplate):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/WhiteQueen.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = 1        
        self.pos = [ 3, 0]

        WhiteQueen.count += 1
        self.name = "wQueen" + str(WhiteQueen.count)
        

    def moveOptions(self,arr):
        x, y = self.pos
        moveSpaces = [ [[x, i] for i in range(y+1,8)] , [[x, i] for i in range(y-1,-1,-1)], [[i, y] for i in range(x+1,8)], [[i, y] for i in range(x-1,-1,-1)] , [], [], [], [] ]

        for count in range(0,2):
            for i in moveSpaces[count]:
                try:
                    j = moveSpaces[count+2][ moveSpaces[count].index(i) ]
                    moveSpaces[4 + count].append([j[0],i[1]])
                except:
                    pass
                
                try:
                    for i in moveSpaces[count]:                    
                        j = moveSpaces[count+3 - (2*count)][ moveSpaces[count].index(i) ]
                        moveSpaces[6 + count].append([j[0],i[1]])
                except:
                    pass               
    
        
        for count in range(0,8):
            for i in moveSpaces[count]:
                if arr[i[0]][i[1]] == None:
                    pass
                elif not(arr[ i[0] ][ i[1] ].team == self.team):
                    moveSpaces[count] = moveSpaces[count][ :moveSpaces[count].index(i)+1 ]
                    break
                else:
                    moveSpaces[count] = moveSpaces[count][ :moveSpaces[count].index(i) ]
                    break

      
        temp = []
        for i in moveSpaces:
            for j in i:
                if j:
                    temp.append(j)
        
        moveSpaces = temp
        return moveSpaces


    def die(self):
        wQueens[ int(self.name[-1]) - 1] = None




        
class BlackQueen(WhiteQueen):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/BlackQueen.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = -1        
        self.pos = [ 3, 7]

        BlackQueen.count += 1
        self.name = "bQueen" + str(BlackQueen.count)

    def die(self):
        bQueens[ int(self.name[-1]) - 1] = None





class WhiteBishop(UnitTemplate):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/WhiteBishop.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = 1        
        self.pos = [ 2 + (3*WhiteBishop.count), 0]

        WhiteBishop.count += 1
        self.name = "wBishop" + str(WhiteBishop.count)

    def moveOptions(self,arr):
        x, y = self.pos
        moveSpaces = [ [[x, i] for i in range(y+1,8)] , [[x, i] for i in range(y-1,-1,-1)], [[i, y] for i in range(x+1,8)], [[i, y] for i in range(x-1,-1,-1)] , [], [], [], [] ]

        for count in range(0,2):
            for i in moveSpaces[count]:
                try:
                    j = moveSpaces[count+2][ moveSpaces[count].index(i) ]
                    moveSpaces[4 + count].append([j[0],i[1]])
                except:
                    pass
                
                try:
                    for i in moveSpaces[count]:                    
                        j = moveSpaces[count+3 - (2*count)][ moveSpaces[count].index(i) ]
                        moveSpaces[6 + count].append([j[0],i[1]])
                except:
                    pass
        
        for count in range(0,8):
            for i in moveSpaces[count]:
                if arr[i[0]][i[1]] == None:
                    pass
                elif not(arr[ i[0] ][ i[1] ].team == self.team):
                    moveSpaces[count] = moveSpaces[count][ :moveSpaces[count].index(i)+1 ]
                    break
                else:
                    moveSpaces[count] = moveSpaces[count][ :moveSpaces[count].index(i) ]
                    break
                
        moveSpaces = moveSpaces[4:]


      
        temp = []
        for i in moveSpaces:
            for j in i:
                if j:
                    temp.append(j)
        
        moveSpaces = temp
        return moveSpaces


    def die(self):
        wBishops[ int(self.name[-1]) - 1] = None



class BlackBishop(WhiteBishop):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/BlackBishop.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = -1        
        self.pos = [ 2 + (3*BlackBishop.count), 7]

        BlackBishop.count += 1
        self.name = "bBishop" + str(BlackBishop.count)

    def die(self):
        bBishops[ int(self.name[-1]) - 1] = None



class WhiteKnight(UnitTemplate):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/WhiteKnight.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = 1        
        self.pos = [ 1 + (5*WhiteKnight.count), 0]

        WhiteKnight.count += 1
        self.name = "wKnight" + str(WhiteKnight.count)

    def moveOptions(self,arr):
        x, y = self.pos
        
        moveSpaces = []
        inverse = 1
        for i in range(-2,3):
            if i == 0:
                continue
            moveSpaces.append( [x+i,y + (-(i+(1*inverse)) )] )
            moveSpaces.append( [x-i,y + (-(i+(1*inverse)) )] )
            inverse*=-1
       

        for i in moveSpaces:
            try:
                if i[0] < 0 or i[1] < 0:
                    moveSpaces[moveSpaces.index(i)] = []
                elif i[0] > 7 or i[1] > 7:
                    moveSpaces[moveSpaces.index(i)] = []
                
                elif arr[i[0]][i[1]].team == self.team:
                    moveSpaces[moveSpaces.index(i)] = []
            except:
                pass


        temp = []
        for i in moveSpaces:
            if i:
                temp.append(i)        
        moveSpaces = temp
        
        return moveSpaces
 

    def die(self):
        wKnights[ int(self.name[-1]) - 1] = None
    

class BlackKnight(WhiteKnight):
    count = 0

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/BlackKnight.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = -1        
        self.pos = [ 1 + (5*BlackKnight.count), 7]

        BlackKnight.count += 1
        self.name = "bKnight" + str(BlackKnight.count)

    def die(self):
        bKnights[ int(self.name[-1]) - 1] = None

class WhiteKing(UnitTemplate):

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/WhiteKing.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = 1        
        self.pos = [ 4, 0]
        self.name = "wKing"

    def check(self,arr):
        checkSpaces = []
        for i in blacks:
            for j in i:
                print(j.name,end=": ")
                print(j.moveOptions(arr))
                if j in bKing:
                    continue
                if j in bPawns:
                    checkSpaces.append([j.pos[0]+1,j.pos[0]-1])
                    checkSpaces.append([j.pos[0]-1,j.pos[0]-1])
                    
                else:
                    checkSpaces.append(j.moveOptions(arr))
        return checkSpaces
        

    def moveOptions(self,arr):
        x, y = self.pos        
        moveSpaces = [ [x, y+1], [x, y-1], [x+1, y], [x-1, y], [x+1,y+1], [x+1,y-1], [x-1,y+1], [x-1,y-1] ]

        try:
            checkSpaces = self.check(arr)
        except Exception as e:
            print(e)

              
        temp = []
        for i in checkSpaces:
            try:
                i[0]/1
                temp.append(i)
            except:
                for j in i:
                    temp.append(j)
        checkSpaces = temp
        print(checkSpaces)

        for i in moveSpaces:
            try:
                if i in checkSpaces:
                    moveSpaces[moveSpaces.index(i)] = [] 
                    
                if i[0] < 0 or i[1] < 0:
                    moveSpaces[moveSpaces.index(i)] = []
                elif i[0] > 7 or i[1] > 7:
                    moveSpaces[moveSpaces.index(i)] = []
                
                elif arr[i[0]][i[1]].team == self.team:
                    moveSpaces[moveSpaces.index(i)] = []



            except:
                pass


        temp = []
        for i in moveSpaces:
            if i:
                temp.append(i)        
        moveSpaces = temp        
        
        return moveSpaces

    def die(self):
        wKing[ int(self.name[-1]) - 1] = None

class BlackKing(WhiteKing):

    def __init__(self):
        import pygame
        self.imageRef = pygame.image.load('Resources/BlackKing.png')
        self.imageRef = pygame.transform.scale(self.imageRef, (50,50))
        
        self.team = -1        
        self.pos = [ 4, 7]
        self.name = "bKing"

    #def moveOptions(self,arr):
        #return []

    def die(self):
        bKing[ int(self.name[-1]) - 1] = None
        
wPawns = [WhitePawn() for i in range(8)]
wKnights = [WhiteKnight() for i in range(2)]
wBishops = [WhiteBishop() for i in range(2)]
wRooks = [WhiteRook() for i in range(2)]
wQueens = [WhiteQueen() for i in range(1)]
wKing = [WhiteKing()]

whites = [wPawns, wKnights, wBishops, wRooks, wQueens, wKing]

bPawns = [BlackPawn() for i in range(8)]
bKnights = [BlackKnight() for i in range(2)]
bBishops = [BlackBishop() for i in range(2)]
bRooks = [BlackRook() for i in range(2)]
bQueens = [BlackQueen() for i in range(1)]
bKing = [BlackKing()]

blacks = [bPawns, bKnights, bBishops, bRooks, bQueens, bKing]
