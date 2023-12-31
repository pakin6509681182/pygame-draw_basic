import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((700, 500), 0, 32)
pygame.display.set_caption('Drawing')

# set up the color
BLACK = (10,10,10)
RED   = (237,28,36)
YELLOW= (255,194,14)
BLUE  = (  0,   0, 255)
BROWN = (70,35,0)
WHITE =(255,255,255)
YELLOWY =[255,240,0]


# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.rect(DISPLAYSURF, RED, (210,0, 150, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (310, 60, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (160, 60, 100, 30))
pygame.draw.rect(DISPLAYSURF, BLACK, (410, 60, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (310, 60, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (160,30, 450, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (360, 60, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (110,90, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (160, 90, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (210,90, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (210, 60, 100, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (460, 60, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (260, 90, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (310, 90, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (360, 90, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLACK, (410, 90, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (460, 90, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (510, 90, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (560, 90, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (110,120, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (160, 120, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (210,120, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (260,120, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (310, 120, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (360, 120, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (410, 120, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLACK, (460, 120, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (510, 120, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (560, 120, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (610, 120, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (160,150, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (210,150, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (260,150, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (310,150, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (360,150, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLACK, (410, 150, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLACK, (460, 150, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLACK, (510, 150, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLACK, (560, 150, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (210,180, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (260,180, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (310,180, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (360,180, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (410,180, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (460,180, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (160,210, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (210,210, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (260,210, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (310,210, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (360,210, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (410,210, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (460,210, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (510,210, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (260,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (310,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (360,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (410,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (110,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (160,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (460,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (510,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (560,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (210,240, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (60,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (110,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (160,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (210,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (260,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (310,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (360,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (410,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (460,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (510,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (560,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (610,270, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (60,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (110,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (160,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (210,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOWY, (260,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (310,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (360,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOWY, (410,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (460,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, RED, (510,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (560,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (610,300, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (60,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (110,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (160,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (210,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (260,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (310,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (360,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (410,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (460,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (510,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (560,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (610,330, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (60,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (110,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (210,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (260,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (310,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (360,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (410,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (460,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (160,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (510,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (560,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, YELLOW, (610,360, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (160,390, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (210,390, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (260,390, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (410,390, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (460,390, 50, 30))
pygame.draw.rect(DISPLAYSURF, BLUE, (510,390, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (110,420, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (160,420, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (210,420, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (460,420, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (510,420, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (560,420, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (60,450, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (110,450, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (160,450, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (210,450, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (460,450, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (510,450, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (560,450, 50, 30))
pygame.draw.rect(DISPLAYSURF, BROWN, (610,450, 50, 30))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()