class Bird():
    def __init__(self) -> None:
        self.yPos = 0
        self.yVel = 0
        self.jumpForce = -2

    def jump(self, key) -> None:
        
        self.yVel = self.jumpForce


#ICONS 🟩🟨🟦

#CLEAR print("\033c", end="")

import time

import random

from pynput import keyboard



birdIcon = "🟨"
emptyIcon = "🟦"
pipeIcon ="🟩"

screenSizeX = 10
screenSizeY = 10

bird = Bird()

gravity = -0.4
startingPosition = 0.0
velocityY = 0.0
positionY = startingPosition

minPipeSize = 1
maxPipeSize = 4
#-----------------------------------------------------------------------------------------------------------------------------------------------#

def makePipeCol(pipeTopSize: int, emptySpace: int, pipeBottomSize: int, item: int) -> list[str]:
    pipeList = []
    rowNum = 0
    for row in range(pipeTopSize):
        
        rowNum += 1
        if round(positionY) == rowNum:
            pipeList.append("🟨")
        else:
            pipeList.append("🟩")
    for row in range(emptySpace):
        rowNum += 1
        if round(positionY) ==  rowNum:
            pipeList.append("🟨")
        else:
            pipeList.append("🟦")
    for row in range(pipeBottomSize):
        rowNum += 1
        if round(positionY) == rowNum:
            pipeList.append("🟨")
        else:
            pipeList.append("🟩")

    return pipeList[item]

def makeGameScreen(screenSizeX) -> None:
    
    screenList = []

    pipeTopSize = random.randrange(minPipeSize,maxPipeSize)
    pipeBottomSize = random.randrange(minPipeSize,maxPipeSize)
    emptySpace = screenSizeY - (pipeTopSize + pipeBottomSize)

    for item in range(10):
            screenList.append(getBirdRow(positionY,birdIcon,emptyIcon,pipeIcon,screenSizeY,item))

    for _ in range(screenSizeX):
        pipeTopSize = random.randrange(minPipeSize,maxPipeSize)
        pipeBottomSize = random.randrange(minPipeSize,maxPipeSize)
        emptySpace = screenSizeY - (pipeTopSize + pipeBottomSize)
        for item in range(screenSizeY):
            screenList.append(makePipeCol(pipeTopSize, emptySpace, pipeBottomSize, item))
        for _ in range(random.randint(1,3)):
            for _ in range(screenSizeY):
                screenList.append("🟦")

    itemNum = 1

    for item in range(len(screenList)):
        if 1 == 0:
            currentRow= []
            for rowNum in range(screenSizeX):
                currentRow.append(screenList[itemNum])
                itemNum += 10
    #for i in range(screenSizeX):
    #    print(currentRow[i])

#-----------------------------------------------------------------------------------------------------------------------------------------------#

def getBirdRow(birdPositionY: float, birdIcon: str, emptyIcon: str, pipeIcon:str, screenSizeY: int, item: int) -> str:

    birdRow = []

    birdPosUpdate = int(round(birdPositionY))

    for loopNum in range(screenSizeY):
        if birdPosUpdate == loopNum:
            birdRow.append(birdIcon)
        else:
            birdRow.append(emptyIcon)
    
    return birdRow[item]

def gameLoopBird() -> None:



    outOfBounds = screenSizeY

    listener = keyboard.Listener(on_press=bird.jump)
    listener.start()

    bird.yVel -= gravity
    bird.yPos += bird.yVel
    
  

    velocityY = bird.yVel

    
    outOfBounds = 9

                             

              
    if bird.yPos > outOfBounds:
        bird.yPos = outOfBounds

    positionY = bird.yPos


    time.sleep(0.2) 

    print("\033c", end="")

    for item in range(10):
        printItem = getBirdRow(positionY,birdIcon,emptyIcon,pipeIcon,screenSizeY,item)
        print(printItem)
#makeGameScreen(screenSizeX)

#final effort
#this is if i havent gotten the pipes down
#please dont give me a bad grade i worked too hard on this
for _ in range(100000):
    gameLoopBird()