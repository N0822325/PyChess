import pygame, os 
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Chess Game")
icon = pygame.image.load('Resources/Chess-icon.png')
number = pygame.image.load('Resources/Numbers/0.png')
pygame.display.set_icon(icon)


eLight = pygame.image.load('Resources/emptySpaceHighlight.png')
aLight = pygame.image.load('Resources/AttackHighlight.png')
back = pygame.image.load('Resources/boardGraphic.png')
wKnighting = pygame.image.load('Resources/PickPiece1.png')
bKnighting = pygame.image.load('Resources/PickPiece2.png')

clock = pygame.time.Clock()

import units
import board

unitCollective = [units.wPawns, units.bPawns, units.wRooks, units.bRooks, units.wQueens, units.bQueens, units.wBishops, units.bBishops, units.wKnights, units.bKnights, units.wKing, units.bKing]


#for i in unitCollective:
    #for j in i:
        #j.imageRef = pygame.transform.scale(j.imageRef, (50,50))

board.set(unitCollective)



def reDraw():
    win.blit(back, (0,0))
    for i in unitCollective:
        for j in i:
            if j == None:
                continue
            win.blit(j.imageRef, ( (j.pos[0]+1)*50, 450 - (j.pos[1]+1)*50 ) )



#startTime = pygame.time.get_ticks()
mousePos = [0,0]
mousePosEnd = [0,0]
isClicked = False
spaces = []

turn = 1
rick = False
kUnitLocation = []
kUnitTeam = 0

while True:
    if units.knightBool:
        if not(kUnitLocation):
            rpp = []
            for i in range(8):
                if not(board.board[i][7] == None):
                    rpp.append(board.board[i][7])
            for i in units.wPawns:
                if i in rpp:
                    kUnitLocation = i.pos
                    kUnitTeam = i.team
                    i.die()
                    win.blit(wKnighting, (52,202))

            rpp = []
            for i in range(8):
                if not(board.board[i][0] == None):
                    rpp.append(board.board[i][0])
            for i in units.bPawns:
                if i in rpp:
                    kUnitLocation = i.pos
                    kUnitTeam = i.team
                    i.die()
                    win.blit(bKnighting, (52,202))
                
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if kUnitTeam == 1:
                    if 202 < pygame.mouse.get_pos()[1] < 296:
                        if 52 < pygame.mouse.get_pos()[0] < 152:
                            units.wQueens.append(units.WhiteQueen())
                            units.wQueens[-1].pos = kUnitLocation
                        if 152 < pygame.mouse.get_pos()[0] < 252:
                            units.wRooks.append(units.WhiteRook())
                            units.wRooks[-1].pos = kUnitLocation
                        if 252 < pygame.mouse.get_pos()[0] < 352:
                            units.wBishops.append(units.WhiteBishop())
                            units.wBishops[-1].pos = kUnitLocation
                        if 352 < pygame.mouse.get_pos()[0] < 448:
                            units.wKnights.append(units.WhiteKnight())
                            units.wKnights[-1].pos = kUnitLocation
                        kUnitLocation = []
                        units.knightBool = False
                else:
                    if 202 < pygame.mouse.get_pos()[1] < 296:
                        if 52 < pygame.mouse.get_pos()[0] < 152:
                            units.bQueens.append(units.BlackQueen())
                            units.bQueens[-1].pos = kUnitLocation
                        if 152 < pygame.mouse.get_pos()[0] < 252:
                            units.bRooks.append(units.BlackRook())
                            units.bRooks[-1].pos = kUnitLocation
                        if 252 < pygame.mouse.get_pos()[0] < 352:
                            units.bBishops.append(units.BlackBishop())
                            units.bBishops[-1].pos = kUnitLocation
                        if 352 < pygame.mouse.get_pos()[0] < 448:
                            units.bKnights.append(units.BlackKnight())
                            units.bKnights[-1].pos = kUnitLocation
                        kUnitLocation = []
                        units.knightBool = False                    

                
        pygame.display.update()
        continue
                                                    
                                        
    #seconds = (pygame.time.get_ticks() - startTime) / 1000
        
    reDraw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            rick = False
            if 70 < pygame.mouse.get_pos()[0] < 130:
                if 10 < pygame.mouse.get_pos()[1] < 40:
                    print("save")
            if 370 < pygame.mouse.get_pos()[0] < 430:
                if 10 < pygame.mouse.get_pos()[1] < 40:
                    print("load")

                
            if 50 < pygame.mouse.get_pos()[0] < 450:
                if 50 < pygame.mouse.get_pos()[1] < 450:
                    mousePos = list(pygame.mouse.get_pos())
                    mousePos[0] = int( (mousePos[0]-50)/50 )
                    mousePos[1] = 7 - int( (mousePos[1]-50)/50 )
                    try:
                        if not (board.board[mousePos[0]][mousePos[1]].team == turn) :
                            break
                    except:
                        pass
                    rick = True
                    try:
                        spaces = board.board[mousePos[0]][mousePos[1]].moveOptions(board.board)
                        isClicked = True
                        for i in range(len(spaces)):
                            spaces[i][0] = ( spaces[i][0] * 50 ) + 50
                            spaces[i][1] = ( ( 7 - spaces[i][1] ) * 50 ) + 50
                            
                    except:
                        pass

        if event.type == pygame.MOUSEBUTTONUP:
            if rick == True:
                if 50 < pygame.mouse.get_pos()[0] < 450:
                    if 50 < pygame.mouse.get_pos()[1] < 450:
                        mousePosEnd = list(pygame.mouse.get_pos())
                        mousePosEnd[0] = int( (mousePosEnd[0]-50)/50 )
                        mousePosEnd[1] = 7 - int( (mousePosEnd[1]-50)/50 )
                    
                        mpe2 = mousePosEnd[:]
                        mpe2[0] = (mpe2[0]*50)+50
                        mpe2[1] = ( ( 7 - mpe2[1] ) *50)+50
                    
                        if mpe2 in spaces:
                            try:
                                board.board[mousePos[0]][mousePos[1]].move(board.board, mousePosEnd)
                                        
                                        #input()
                                    

                                turn*=-1
                            except Exception as e:
                                print("\n",e)
                            board.set(unitCollective)
                isClicked = False

    if isClicked:
        try:
                        
            for i in spaces:
                j = [int((i[0] - 50)/50),int( 7 - ((i[1] - 50)/50) )]

                if board.board[j[0]][j[1]] == None:
                    win.blit(eLight, (i[0], i[1]) )
                else:
                    win.blit(aLight, (i[0], i[1]) )

            win.blit(board.board[mousePos[0]][mousePos[1]].imageRef, ( (pygame.mouse.get_pos()[0]-25, pygame.mouse.get_pos()[1]-25) ) )
            
        except Exception as e:
            print(e)

    pygame.display.update()
    clock.tick(60)

    
    
