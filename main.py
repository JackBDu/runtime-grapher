##########################################################
###                   PYGAME – Graph                  ###
###   1st Project for Data Structure at NYU Shanghai   ###
##########################################################

__author__ = "Jack B. Du (Jiadong Du)"
__copyright__ = "Copyright 2014, the DS 1st Project @NYUSH"
__version__ = "0.0.1"
__email__ = "JackBDu@nyu.edu"
__status__ = "Developing"



import time
import random
import pygame
from pygame.locals import *
import sys

import functions

############
## SETUPS ##
############

## initialize pygame
pygame.init()

## setups
SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 768
infoObject = pygame.display.Info()
FULLSCREEN_WIDTH = infoObject.current_w
FULLSCREEN_HEIGHT = infoObject.current_h
CURRENT_SCREEN_WIDTH = SCREEN_WIDTH
CURRENT_SCREEN_HEIGHT = SCREEN_HEIGHT
SCREEN_SIZE = (CURRENT_SCREEN_WIDTH, CURRENT_SCREEN_HEIGHT)
MARGIN_BOTTOM = 30
MARGIN_LEFT = 30
MARGIN_RIGHT = 30
MARGIN_TOP = 30
FONT_SIZE = 20
myfont = pygame.font.SysFont("arial", FONT_SIZE)
paused = False
maxValueList = []
reset = True

# default screen mode
fullscreen = False
# set caption on the bar
pygame.display.set_caption('Jack B. Du\'s Graph')
# create screen
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)

# background setup
background = pygame.Surface(screen.get_size())
background = background.convert()
backgorund_color = (0 ,0 , 0)
background.fill(backgorund_color)

# runtime of f
def timer(f, *p):
    begin_time = time.clock()
    f(*p)
    end_time = time.clock()
    
    return(end_time - begin_time)

def main():
    # a list of functions, which support one-list input, two-list input and integer input
    functionList = [functions.countEvens,
                    functions.myMin,
                    functions.myMax,
                    functions.median,
                    functions.secondBiggest,
                    functions.LIS,
                    functions.dot,
                    functions.intersect1,
                    functions.intersect2,
                    functions.fib]
    # plot the functions
    sim(functionList)

def sim(functionList):
    global screen, fullscreen, SCREEN_SIZE, CURRENT_SCREEN_WIDTH, CURRENT_SCREEN_HEIGHT, background, paused, maxValueList, reset
    mainloop = True
    highlightedColor = (255,255,255) # color for highlighted color

    # mainloop 
    while mainloop:
        if reset:
            textX, textY = 0, -400
            manul = 1 # percentage of height
            size = 10 # input step size
            N = size # initial input size
            yPointList = [] # y value for each point
            pointList = [] # all the points
            color = [] # color for each graph
            highlight = 0 # default highlight graph number
            maxDict = {} # dict of max value for different algorithms
            hide = False # whether or not hide the graphs that are not highlighted

            # create different lists of lists for each function
            for num in range(len(functionList)):
                yPointList.append([])
                pointList.append([])
                color.append([])
                color[num]=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
            count = 0 # loop count
            highest = 0 # highest point, max y value of all points
            highlighted = False # whether in the highlighted mode or not
            changed = True # whether changed manually or not

            reset = False
            
        if textY < 0:
            textY += 20
        
        if not paused:
            N += size
        for event in pygame.event.get():
            # the quit on the system bar
            if event.type == QUIT:
                mainloop = False

            elif event.type == KEYDOWN:
                if event.key == K_q: # quit with q/Q key
                    mainloop = False
                elif event.key == K_f: ## press f/F to enter/exit fullscreen mode
                    fullscreen = not fullscreen
                    if fullscreen:
                        CURRENT_SCREEN_WIDTH = FULLSCREEN_WIDTH
                        CURRENT_SCREEN_HEIGHT = FULLSCREEN_HEIGHT
                        SCREEN_SIZE = (CURRENT_SCREEN_WIDTH, CURRENT_SCREEN_HEIGHT)
                        screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
                        background = pygame.Surface(screen.get_size())
                        background = background.convert()
                        background.fill((0, 0, 0))
                    else:
                        CURRENT_SCREEN_WIDTH = SCREEN_WIDTH
                        CURRENT_SCREEN_HEIGHT = SCREEN_HEIGHT
                        SCREEN_SIZE = (CURRENT_SCREEN_WIDTH, CURRENT_SCREEN_HEIGHT)
                        screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
                        background = pygame.Surface(screen.get_size())
                        background = background.convert()
                        background.fill((0, 0, 0))
                elif event.key == K_w: # set background white, highlighted black
                    background.fill((255, 255, 255))
                    highlightedColor = (0,0,0)
                elif event.key == K_b: # set background black, highlighted white
                    background.fill((0, 0, 0))
                    highlightedColor = (255,255,255)
                elif event.key == K_EQUALS: # scale by 10
                    changed = True
                    manul *= 10
                elif event.key == K_MINUS: # scale by 1/10
                    manul /= 10
                    changed = True
                elif event.key == K_d or event.key ==K_0: # press d/0 key to default scale
                    manul = 1
                    changed = True
                elif event.key == K_h:
                    hide = not hide
                elif event.key == K_SPACE:
                    paused = not paused
                elif event.key == K_r:
                    reset = True

                # press n key to scale by 10n
                elif event.key == K_1:
                    manul = 10
                    changed = True
                elif event.key == K_2:
                    manul = 20
                    changed = True
                elif event.key == K_3:
                    manul = 30
                    changed = True
                elif event.key == K_4:
                    manul = 40
                    changed = True
                elif event.key == K_5:
                    manul = 50
                    changed = True
                elif event.key == K_6:
                    manul = 60
                    changed = True
                elif event.key == K_7:
                    manul = 70
                    changed = True
                elif event.key == K_8:
                    manul = 80
                    changed = True
                elif event.key == K_9:
                    manul = 90
                    changed = True

                # highlighting options
                elif event.key == K_UP:
                    changed = False
                    if highlighted:
                        currentPos = valueList.index(valueDict[highlight])
                        if currentPos > 0:  # highlight the upper graph
                            highlight = unsortedValueList.index(valueList[currentPos-1])
                    else:
                        highlighted = True # set to highlighted
                        highlight = unsortedValueList.index(valueList[-1]) # start with the bottom
                elif event.key == K_DOWN:
                    changed = False
                    if highlighted:
                        currentPos = valueList.index(valueDict[highlight])
                        if currentPos < len(functionList)-1: # highlight the lower graph
                            highlight = unsortedValueList.index(valueList[currentPos+1]) 
                    else:
                        highlighted = True # set to highlighted
                        highlight = unsortedValueList.index(valueList[0]) # start with the top
                        
                elif event.key == K_ESCAPE: # press ESC to escape highlight mode
                    highlighted = False

        screen.blit(background,(0,0))
        inputNum = str(int(N/size)) + " (loopCount)"
        loopLabel = myfont.render(inputNum, 1,  (0,0,255))
        screen.blit(loopLabel, (MARGIN_LEFT*2+textX, MARGIN_TOP+textY))
        
        framePointList = [(MARGIN_LEFT,MARGIN_TOP),(MARGIN_LEFT,CURRENT_SCREEN_HEIGHT-MARGIN_BOTTOM),(CURRENT_SCREEN_WIDTH-MARGIN_RIGHT,CURRENT_SCREEN_HEIGHT-MARGIN_BOTTOM)]
        pygame.draw.lines(screen, (150,150,150), False, framePointList, 1)
        if not paused:
            count += 1
            valueDict = {}
            valueList = []

            for function in functionList:
                A = [i for i in range (N)]
                random.shuffle(A)
                try:
                    time = timer(function, A)
                except:
                    try:
                        B = [i for i in range (N)]
                        random.shuffle(B)
                        time = timer(function, A, B)
                    except:
                        time = timer(function, 10*N)
                if time>highest:
                    highest = time
                valueDict[functionList.index(function)] = time
                valueList.append(time)
                yPointList[functionList.index(function)].append(time)

        if highlighted and not(changed):
            if not paused:
                maxValueList = []
            for function in functionList:
                maxValue = max(yPointList[functionList.index(function)])
                maxDict[functionList.index(function)] = maxValue
                maxValueList.append(maxValue)
            manul = highest/maxValueList[highlight]         

        for function in functionList:
            pointList[functionList.index(function)]=[(MARGIN_LEFT,CURRENT_SCREEN_HEIGHT-MARGIN_BOTTOM)]  ## starts from (0,0)

            for num in range(count):
                posX = (CURRENT_SCREEN_WIDTH - MARGIN_LEFT - MARGIN_RIGHT)/count * (num+1) + MARGIN_LEFT
                posY = (CURRENT_SCREEN_HEIGHT - MARGIN_BOTTOM - MARGIN_TOP)*(1-manul*yPointList[functionList.index(function)][num]/highest) + MARGIN_TOP
                pointList[functionList.index(function)].append((posX,posY))
            
        if count > 1:
            if not hide:
                for num in range(len(functionList)):
                    pygame.draw.lines(screen, color[num], False, pointList[num], 1)

            if highlighted:
                pygame.draw.lines(screen, highlightedColor, False, pointList[highlight], 2)

        if not paused:
            unsortedValueList = []
            unsortedValueList += valueList
            valueList.sort()
            valueList.reverse()
        for function in functionList:
            functionInfo = str(format(valueDict[functionList.index(function)],',.6f')) + " (" + str(function)[10:-16] + ")"
            if highlighted and functionList.index(function) == highlight:
                functionLabel = myfont.render(functionInfo, 1, highlightedColor)
            else:
                functionLabel = myfont.render(functionInfo, 1, color[functionList.index(function)])
            screen.blit(functionLabel, (MARGIN_LEFT*2+textX, textY+MARGIN_TOP+FONT_SIZE+FONT_SIZE*valueList.index(valueDict[functionList.index(function)])))

        percentageInfo = str(int(manul*100)) + '%' + " (scale)"
        percentageLabel = myfont.render(percentageInfo, 1, (150,150,150))
        screen.blit(percentageLabel, (MARGIN_LEFT*2+textX, textY+MARGIN_TOP+FONT_SIZE+FONT_SIZE*len(valueList)))
        pygame.display.update()


    pygame.quit()

main()


