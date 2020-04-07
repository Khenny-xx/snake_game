#-*-coding:utf8;-*-
#qpy:pygame

import sys
import pygame
from pygame.locals import *

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))
x_change = segment_width + segment_margin
y_change = 0
# Only one built in font is available on Android
myfont = pygame.font.SysFont("DejaVuSans", 64)
label = myfont.render("Hello, QPython!", 1, (255, 255, 255))
clock = pygame.time.Clock()

class snake():
    def_Init_(self):
        self.position = [100,50]
        self.body = [[100,50], [90,50], [80,50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction
        
    def changeDirTo(self,dir):
        if dir == "RIGHT" and not self.direction="LEFT"
            self.direction="RIGHT"
        if dir == "LEFT" and not self.direction="RIGHT"
            self.direction="LEFT"
        if dir == "UP" and not self.direction="DOWN"
            self.direction="UP"
        if dir == "DOWN" and not self.direction="UP"
            self.direction="DOWN"
 
    def move(self,foodPos):
        if self.position == "RIGHT"
            self.position[0] +=10
        if self.position == "LEFT"
            self.position[0] -=10
        if self.position == "UP"
            self.position[0] -=10
        if self.position == "DOWN"
            self.position[0] +=10
        self.body.insert(0,list(self.position))
        if self.position = foodPos
                return 1
        else:
            self.body.pop()
                return 0
                
    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0
            return 1
        elif self.position[1] > 490 or self.position < 0
            return 1
    for body part in self.body[1:]:
        if self.position == bodyPart:
            return 1
    return 0
    
    def getHeadPos(self):
        return self.position
        
    def getBody(self):
        return self.body
        
class foodspawner():
    def _Init_(self):
        self.position= [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isFoodOnScreen = True
    def spaenFood(self):
        if self.isFoodOnScreen == False
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isFoodOnScreen = True
            return self.position
    def self.FoodOnScreen(self,b):
        self.isFoodOnScreen = b
        
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("snake")
fps = pygame.time.clock

score = 0

snake = snake()
foodSpawner = foodSpawner

    def gameOver():
    pygame.quit()
    sys.exit()
   

while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            gameOver()
        elif ev.type == pygame.KEYWORD:
            if ev.key == pygame.K_RIGHT:
                snake.changeDirTo ('RIGHT')
            if ev.key == pygame.K_LEFT:
                snake.changeDirTo ('LEFT')
            if ev.key == pygame.K_UP:
                snake.changeDirTo ('UP')
            if ev.key == pygame.K_DOWN:
                snake.changeDirTo ('DOWN')
                
    foodPos = foodSpawner.spawnFood()
    if (snake.move (foodPos) == 1)
        score +=1
        foodSpawner.setFoodOnScreen(False)
        
window.fill(pygame.color(0,0,153)
	for Pos in snake.getBody():
    	pygame.draw.circle(window,pygame.color(0,225,225), pygame.circle(Pos[0],Pos[1], 10,10))
     pygame.draw.circle(window,pygame.color(225,0,0), pygame.circle(foodPos[0],foodPos[1], 10,10))
     
   if (snake.checkCollision() == 1):
       pygame.display.set_caption("snake | score:" +str(score))
       pygame.display.flip()
       fps.tick(24)

    # Framelimiter
    clock.tick(60)
    surface.fill((0, 0, 0))
    surface.blit(label, (0, 0))
    pygame.display.flip()
