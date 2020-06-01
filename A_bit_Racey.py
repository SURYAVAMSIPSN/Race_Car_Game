# Timepass - Game Development. 
# Let's make a racecar game! 

import pygame
import time
import random

pygame.init() # initiate pygame and its modules. Always put this first. 

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255) # color definition in RGB. 

red = (200, 0, 0) # Dark red
blue = (0, 0, 255)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

FPS = 60

gameDisplay = pygame.display.set_mode((display_width, display_height)) # games with some resolution
pygame.display.set_caption('A bit Racey') # Name of the game. 
clock = pygame.time.Clock() # game clock. 

carImg = pygame.image.load('my_car.png') # load the required image. 
car_width =73. # you need to measure this. 

pygame.display.set_icon(carImg)

def quit_game():
    pygame.quit()
    quit()


def things_dodged(count): # for getting score. 
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0)) # Display score. 
    
    


def things(thingx, thingy, thingw, thingh, color): 
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    


def car(x, y):
    gameDisplay.blit(carImg, (x, y)) # put car img at x, y

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2, display_height/2)) # at center
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()

def crash():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quit_game)

        pygame.display.update()
        clock.tick(15) 

def button(msg, x, y, w, h, ic, ac, action=None): # Generic button function. 
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() # mouse click
    
        
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None: # if we get a click.
            action() # call object function.             
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    
    textRect.center = ( (x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)
    

def unpause():
    global pause
    pause = False

def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quit_game)

        pygame.display.update()
        clock.tick(15)  



def game_intro():
    
    intro = True 
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2, display_height/2)) # at center
        gameDisplay.blit(TextSurf, TextRect)
        
        
        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop) # pass function as an object
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)
    
        pygame.display.update()
        clock.tick(7)
        

def game_loop():
    
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)  
    
    x_change = 0
    
    thing_startx = random.randrange(0, display_width) # object should be at random spot at startup
    thing_starty = -600
    thing_speed = 4 # each time we draw, move up to 7 pixels
    thing_width = 100 # pixels
    thing_height = 100
    
    dodged = 0
    
    gameExit = False # We have not exit. 
    
    while not gameExit: # as long as exit is still false
        for event in pygame.event.get(): # get's an event. Mouse click? Key press? etc.
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #print(event) # print whatever that's happening. 
            
            # let's try to control the image. 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # if left key, let's move left
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                
            if event.type == pygame.KEYUP: # if key released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        x += x_change
        gameDisplay.fill(white) # Fill the screen with this color. 
        
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        
        thing_starty += thing_speed # we want object to move down, 
        # closer towards car.
        
        car(x, y)    # Mettez la voiture. 
        
        things_dodged(dodged)
        
        # Detect crash against boundaris! 
        if x > display_width - car_width or x < 0: # consider car width
            crash() # initiate crash. 
        
        if thing_starty > display_height: # redraw box if it disappears
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            # Make things difficult
            thing_speed += 0.5 # increase speed. :) 
            thing_width += (dodged* 1.2) 
            
        # crashing into obstacles. 
        if y < thing_starty + thing_height:
            
            if (x > thing_startx and x < thing_startx + thing_width) or (x + car_width > thing_startx and x + car_width < thing_startx + thing_width):
                print('x Crossover')
                crash()
        pygame.display.update() # keep updating display. Keep redrawing screen. 
        clock.tick(FPS) # for FPS. 
      
if __name__ == '__main__':  
    try:    
        game_intro() # initiate the game! 
        game_loop() # Run the game!!
        
        # Uninitiate pygame. Exit. 
        pygame.quit()
        quit()
    except Exception as e: print(e)
