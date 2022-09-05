import pygame
import time
import random

HEIGHT = 720
WIDTH = 1280
BGC = (169,169,169)
RAIN_COLOR = (75,0,130)
RAIN_COUNT = 2000
WIND_SPEED = 0

root = pygame.display.set_mode((WIDTH, HEIGHT))

class rain:
    def __init__(self, color = (150,50,150), surf = root, y = 0, x = 1, speed = 5, width = 5, height = 10):
        self.color = color
        self.surf = surf
        self.y = y
        self.x = x
        self.speed = speed
        self.width = width
        self.height = height 
    def draw(self):
        pygame.draw.rect(self.surf, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        pass
    def fall(self):
        self.y += self.speed
        if WIND_SPEED < 0:
            self.x += round(WIND_SPEED-self.speed/10)
        elif WIND_SPEED > 0:
            self.x += round(WIND_SPEED+self.speed/10)
            
        if self.y >= HEIGHT+self.height:
            self.y = random.randint(-200, -100)
            self.x = random.randint(-500,WIDTH+500)
            self.speed = random.randint(5,15)
            self.width = round(self.speed/5)
            self.height = round(self.speed)

running = True
rains = []
for i in range(RAIN_COUNT):
    rains.append(rain(color = RAIN_COLOR))
for i in range(0, len(rains)):
        rains[i].x = random.randint(-500,WIDTH+500)
        rains[i].speed = random.randint(5,15)
        rains[i].width = round(rains[i].speed/3)
        rains[i].height = round(rains[i].speed)
        rains[i].y = random.randint(-200, HEIGHT)

while running:
    root.fill(BGC)
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    for i in range(0, len(rains)):
        rains[i].draw()
        rains[i].fall()
    if keys[pygame.K_LEFT]:
        WIND_SPEED -= 0.25
        print(WIND_SPEED)
    if keys[pygame.K_RIGHT]:
        WIND_SPEED += 0.25
        print(WIND_SPEED)
    if keys[pygame.K_DOWN]:
        WIND_SPEED = 0
        print(WIND_SPEED)
        
    pygame.display.flip()
    time.sleep(1/60)