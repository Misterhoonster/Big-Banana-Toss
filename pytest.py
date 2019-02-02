import pygame, random, math
from PIL import Image
from pygame.locals import *
import time
pygame.init()

class banana():
    def newposindiv(self, val, vel):
        temp = val
        temp += vel
        return temp;

    def __init__(self, posx, posy, xs, ys):
        self.x = posx
        self.y = posy
        self.xspeed = xs
        self.yspeed = ys
        self.image = pygame.image.load('banana.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 100))

    def newpos(self):
        self.x = self.newposindiv(self.x, self.xspeed)
        self.y = self.newposindiv(self.y, self.yspeed)
        self.yspeed += 0.5

#colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)

#Screen
size = [1000,1000]
screen = pygame.display.set_mode(size)
background = pygame.image.load("background.png").convert()
pygame.display.set_caption("Big Banana")
titlescreen = pygame.image.load('titlescreen.png').convert()

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#garbage
garbage = pygame.image.load('trashcan.png')
box = pygame.image.load('blackbox.png')

#Timer Font
font = pygame.font.Font(None, 25)

#Timer stuff
frame_count = 0
frame_rate = 60
start_time = 10

#Player Score/Turn
player_One = 0
player_Two = 0
p1_Turn = 0

arrow = pygame.image.load('arrow.png')
arrow = pygame.transform.scale(arrow, (0, 800))

def distance(x1, x2, y1, y2):
    return (((x2 - x1)**2 + (y2 - y1)**2)) ** 0.5

def gameIntro():
    size = [1000,1000]
    screen = pygame.display.set_mode(size)
    titlescreen = pygame.image.load('titlescreen.png').convert()
    screen.fill(WHITE)
    for i in range(1000):
        screen.blit(titlescreen, (0,0))
        pygame.display.flip()



def gameLoop():
    #colors
    WHITE = (255, 255, 255)
    BLACK = (0,0,0)

    #Screen
    size = [1000,1000]
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("background.png").convert()
    pygame.display.set_caption("Big Banana")

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    #garbage
    garbage = pygame.image.load('trashcan.png')
    box = pygame.image.load('blackbox.png')

    #Timer Font
    font = pygame.font.Font(None, 25)

    #Timer stuff
    frame_count = 0
    frame_rate = 60
    start_time = 10

    #Player Score/Turn
    player_One = 0
    player_Two = 0
    p1_Turn = 0

    arrow = pygame.image.load('arrow.png')
    arrow = pygame.transform.scale(arrow, (0, 800))

    def distance(x1, x2, y1, y2):
        return (((x2 - x1)**2 + (y2 - y1)**2)) ** 0.5

    templist = []
    angle = 0
    pygame.key.set_repeat(1, 50)
    gx = 600
    left = False
    running = True
    while running:
        if(gx < 405):
            left = False
            gx += 5
        elif(left):
            gx -= 5
        elif(gx > 795):
            left = True
        else:
            gx += 5



        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if (event.key == K_a):
                    angle += 0.1
            elif event.type == KEYUP:
                print(angle)
                if event.key == K_a:
                    # Fire banana
                    tempbanana = banana(100, 800, math.cos(angle) * 13, math.sin(angle) * -30)
                    templist.append(tempbanana)

                    # reset angle
                    angle = 0
            elif event.type ==  QUIT:
                running = False

        #Drawing on Screen
        tempangle = angle * 180 / 3.14
        for var in range(int(tempangle / 5)):
            screen.blit(box, (200, 400 - 10 * var))
        screen.blit(garbage,(gx,800))

        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            p1_Turn += 1
            total_seconds = 10
            frame_count = 0
        if p1_Turn % 2 == 0:
            output_Player = "Player One"
            for i in templist:
                i.newpos()
                screen.blit(i.image, (i.x, i.y))
                if distance(i.x, gx + 50, i.y, 800) < 50:
                    print(distance(i.x, gx + 50, i.y, 800) < 50)
                    player_One += 1
        else:
            output_Player = "Player Two"
            for i in templist:
                i.newpos()
                screen.blit(i.image, (i.x, i.y))
                if distance(i.x, gx + 50, i.y, 800) < 50:
                    print(distance(i.x, gx + 50, i.y, 800) < 50)
                    player_Two += 1

        for i in templist:
            if(i.y > 800):
                templist.remove(i)

        minutes = total_seconds // 60
        seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
        output_score1 = "Player One: {0}".format(player_One)
        output_score2 = "Player Two: {0}".format(player_Two)

        text = font.render(output_string, True, WHITE)
        screen.blit(text, [400, 0])

        text = font.render(output_score1, True, WHITE)
        screen.blit(text, [150, 0])

        text = font.render(output_score2, True, WHITE)
        screen.blit(text, [750, 0])

        text = font.render(output_Player, True, WHITE)
        screen.blit(text, [150, 850])

        frame_count += 1

        clock.tick(frame_rate)

        #Refresh Screen
        pygame.display.flip()
gameIntro()
gameLoop()

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
