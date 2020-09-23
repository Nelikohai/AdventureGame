#imports Modules
import pygame, sys, os

#setup window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Adventure Game")
screen = pygame.display.set_mode((500, 500), 0, False)
rootDirectory = os.path.dirname(__file__)
imageDirectory = rootDirectory + '\\img'
textDirectory = rootDirectory + '\\text'



TitleFont = pygame.font.SysFont("", 50)
NormalFont = pygame.font.SysFont("", 20)

#Title
Title = TitleFont.render("Adventure Game", 1, (255, 255, 255))
Titlerect = Title.get_rect()
Titlerect.topleft = (20, 20)

#Clicks
click = False
rightClick = False

#Button
btnStart = pygame.draw.rect(screen, (100, 250, 50), (30, 175,150, 40))
txtStart = NormalFont.render("Start", 1, (0, 0, 0))
txtStartrect = txtStart.get_rect()
txtStartrect.center = (100, 196)
#Buttons for Answers

#Other Field Variables
mouseX, mouseY = pygame.mouse.get_pos()
questionCount = 0

userDictionary = {
    "name": "",
    "class": ""

}


currentQuestions = []

pygame.display.update()


def grabFile(fileName):

    #[Type of Sentence (Sentence/Question)][The actual words said]
    dialogue = open(textDirectory +'\\' + fileName + '.txt')
    #local variables that can be used in either if statement
    myCount = 0
    tempArray1 = []
    
    if fileName == "text":
    #local variables that can only be used in this if statement
        tempArray2 = []
        
        for line in dialogue:
            tempArray1.insert(myCount,line)
            tempArray2.insert(myCount,dialogue.readline())
            myCount = myCount + 1
        
        textArray = [tempArray1,tempArray2]
    elif fileName == "questions":
        #local variable
        #TODO: changeing Delimiters to a comma
        tempString = dialogue.readlines()
        currentAnswers = tempString[questionCount]
        
        #print(tempString)
        #We need to turn the string into a delimited array
        textArray = currentAnswers.split(",")

                
    dialogue.close()
    return textArray

def fpsAndMouse():
    #FPS
    myFPS = NormalFont.render(str(round(mainClock.get_fps(), 2)), 1, (255, 10, 10))

    myFPSrect = myFPS.get_rect()
    myFPSrect.topleft = (440, 15)
    screen.blit(myFPS, myFPSrect)

    mouseX, mouseY = pygame.mouse.get_pos()
    #shows the x and y of the mouse real time
    xAndy = NormalFont.render("(" + str(mouseX) + ", " + str(mouseY) + ")", 1, (255, 255, 255))
    xAndyrect = xAndy.get_rect()
    xAndyrect.topleft = (mouseX + 15, mouseY - 15)
    screen.blit(xAndy,xAndyrect)
    return mouseX, mouseY

#sends in dialouge and puts it on screen
def createText(text):
    txtBox = NormalFont.render(text, 1, (255, 255, 255))
    txtBoxrect = txtStart.get_rect()
    txtBoxrect.topleft = (20, 370)
    screen.blit(txtBox, txtBoxrect)

#create buttons to click for answering questions
def createAnswers(text):
    #parameter: Array that has the answers in them

    #btn Creation
    global btnAnswer1, btnAnswer2, btnAnswer3, btnAnswer4
    btnAnswer1 = pygame.draw.rect(screen, (100, 250, 50), (30, 395, 150, 30))
    btnAnswer2 = pygame.draw.rect(screen, (100, 250, 50), (200, 395, 150, 30))
    btnAnswer3 = pygame.draw.rect(screen, (100, 250, 50), (30, 445, 150, 30))
    btnAnswer4 = pygame.draw.rect(screen, (100, 250, 50), (200, 445, 150, 30))

    #txt Creation
    txtBtn1 = NormalFont.render(text[0], 1, (0, 0, 0))
    txtBtn1rect = txtBtn1.get_rect()
    txtBtn1rect.topleft = (40, 405)
    txtBtn2 = NormalFont.render(text[1], 1, (0, 0, 0))
    txtBtn2rect = txtBtn2.get_rect()
    txtBtn2rect.topleft = (210, 405)
    txtBtn3 = NormalFont.render(text[2], 1, (0, 0, 0))
    txtBtn3rect = txtBtn3.get_rect()
    txtBtn3rect.topleft = (40, 455)
    txtBtn4 = NormalFont.render(text[3], 1, (0, 0, 0))
    txtBtn4rect = txtBtn4.get_rect()
    txtBtn4rect.topleft = (210, 455)

    screen.blit(txtBtn1, txtBtn1rect)
    screen.blit(txtBtn2, txtBtn2rect)
    screen.blit(txtBtn3, txtBtn3rect)
    screen.blit(txtBtn4, txtBtn4rect)

def grabKey(currentAnswer):
    global questionCount
    #function will grab the key, set value
    #ONLY IF WE CLICK THE BUTTON
    #Count is the count of how many times the 'for loop' runs
    count = 0
        #if the count is equal to the question count (which is equal to the number of questions)
    for x in userDictionary.keys():
        if count == questionCount:

            userDictionary[x] = currentAnswer
        else:
            count = count + 1
    questionCount = questionCount + 1

def gameScreen():
    secondWhile = True
    clickCount = 0
    click = False
    questionCount = 0
    clickcounter = True
    responses = None
    global userDictionary
    character = None
    background = "cliff.jpg"
    
    while secondWhile == True:

        #makes the background black
        screen.fill((0, 0, 0))

        #For Changing Backgrounds
        #if(clickCount == 7):
          #  background = ""
        
        myImage = pygame.transform.smoothscale(pygame.image.load(imageDirectory + "\\" + background), (500, 350))

        screen.blit(myImage,(0, 0))                  #           x   y       width  height

        #Adding Items/Characters on screen
        #if(clickCount == 7):
            #character = ""

            #myCharacter = pygame.transform.smoothscale(
            #pygame.image.load(imageDirectory + "\\" + character), (500, 350))

            #screen.blit(myCharacter,(0, 0)) 
        
        pygame.draw.rect(screen, (255, 255, 255), (0, 350, 500, 150), 0)
        pygame.draw.rect(screen, (0, 0, 0), (10, 360, 480, 130), 0)
        

        mouseX, mouseY = fpsAndMouse()

        #Where to do run game

        #Displays text until the end of the array
        #if clickCount < len(myText[1]):
          #  createText(myText[1][clickCount])

        #if the catergory is question
          #TODO Add Ending
        try:
            if myText[0][clickCount]=="Question\n":
                
                    createText(myText[1][clickCount])
                    #create a text box below the normal text
                    #just for the questions
                    responses = grabFile("questions")
                    createAnswers(responses)
                    
                    
                    clickcounter = False
            #if the category is sentence
            elif myText[0][clickCount]=="Sentence\n":
                    if(myText[1][clickCount].find("NAME") == -1):
                        createText(myText[1][clickCount])
                    else:
                        myText[1][clickCount] = myText[1][clickCount].replace("NAME", userDictionary["name"])
                        createText(myText[1][clickCount])

                    if(myText[1][clickCount].find("CLASS") == -1):
                        createText(myText[1][clickCount])
                    else:
                        myText[1][clickCount] = myText[1][clickCount].replace("CLASS", userDictionary["class"])
                        createText(myText[1][clickCount])
        except IndexError:
            #Display a message that signals that the game is over,
            #Set clickcounter to false
            createText("Something unfortunate happened. Welp, press that X. /GAME RESTART")
            clickcounter = False
        
        if clickcounter == True:

        #goes to the next index when you click
            if click == True:
                clickCount = clickCount + 1
        else:
            currentAnswer = ""
            if btnAnswer1.collidepoint((mouseX, mouseY)):
                if click == True:
                    #stuff
                    currentAnswer = responses[0]
                    clickcounter = True
                    clickCount = clickCount + 1
                    grabKey(currentAnswer)
            elif btnAnswer2.collidepoint((mouseX, mouseY)):
                if click == True:
                    #stuff
                    currentAnswer = responses[1]
                    clickcounter = True
                    clickCount = clickCount + 1
                    grabKey(currentAnswer)
            elif btnAnswer3.collidepoint((mouseX, mouseY)):
                if click == True:
                    #stuff
                    currentAnswer = responses[2]
                    clickcounter = True
                    clickCount = clickCount + 1
                    grabKey(currentAnswer)
            elif btnAnswer4.collidepoint((mouseX, mouseY)):
                if click == True:
                    #stuff
                    currentAnswer = responses[3]
                    clickcounter = True
                    clickCount = clickCount + 1
                    grabKey(currentAnswer)

            

        #where to stop the code for gameplay
        click = False

        rightClick = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                else:
                    rightClick = True

        pygame.display.update()
        mainClock.tick(60)







def titleScreen():
    firstWhile = True
    while firstWhile == True:

        #TODO: make some cool backgrounds
        img0 = pygame.image.load(imageDirectory + "\\vinedbrick.png")
        screen.blit(img0, (0, 0))


        #draws the button
        btnStart = pygame.draw.rect(screen, (100, 250, 50), (30, 175,150, 40))
        #moved blits to the while true
        screen.blit(txtStart, txtStartrect)
        screen.blit(Title, Titlerect)

        mouseX, mouseY = fpsAndMouse()

        #Our first Button click event
        if btnStart.collidepoint((mouseX, mouseY)):
            if click == True:
                #do something
                firstWhile = False
                gameScreen()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #updates the display
        pygame.display.flip()
        mainClock.tick(60)


myText = grabFile("text")
titleScreen()
