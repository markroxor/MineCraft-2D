import pygame,sys,random
from pygame.locals import *


Black = (0  ,  0,  0)
Brown = (153, 76,  0)
Green = (0,  255,  0)
Blue  = (0,    0,255)
WHITE = (255,255,255)

Dirt = 0
Grass = 1
Water = 2
Coal = 3 
Cloud = 4
Cloud1 = 5

colours = {
	Dirt : Brown,
	Grass: Green,
	Water: Blue,
	Coal : Black
}
textures = {
	Dirt : pygame.image.load('Brown.png'),
	Grass : pygame.image.load('Green.png'),
	Water : pygame.image.load('blue.png'),
	Coal : pygame.image.load('Coal.png'),	
	Cloud : pygame.image.load('cloud.png'),	
	Cloud1 : pygame.image.load('cloud.png')
}

inventory = {
		Dirt: 000,
		Grass:000,
		Water:000,
		Coal: 000,
}
TILESIZE = 10
MAPWIDTH = 75
MAPHEIGHT = 50


resources = [Dirt,Grass,Water,Coal]
tilemap = [[Dirt for w in xrange(MAPWIDTH)] for h in xrange(MAPHEIGHT)]


pygame.init()
Display = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE+50))

INVFONT = pygame.font.Font('Hack-Regular.ttf',18)

for rw in xrange(MAPHEIGHT):
	for cl in xrange(MAPWIDTH):
		rn = random.randint(0,15)
		if rn==0:
			tile = Coal
		elif rn==1 or rn==2:
			tile = Water
		elif rn >=3 and rn <=7:
			tile = Grass
		else:
			tile = Dirt
		tilemap[rw][cl] = tile

PLAYER = pygame.image.load("player3.png").convert_alpha()
playerPos=[0,0]
CloudPos = [0,random.randint(0,MAPHEIGHT*TILESIZE)]
CloudPos1 = [0,random.randint(0,MAPHEIGHT*TILESIZE)]

while 1:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == KEYDOWN:
			if event.key == K_RIGHT and playerPos[0]+1<MAPWIDTH:
				playerPos[0]+=1
			if event.key == K_UP and playerPos[1]-1>-1:
				playerPos[1]-=1
			if event.key == K_DOWN and playerPos[1]+1<MAPHEIGHT:
				playerPos[1]+=1
			if event.key == K_LEFT and playerPos[0]-1>-1:
				playerPos[0]-=1
			if event.key == K_SPACE:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile]+=1
				tilemap[playerPos[1]][playerPos[0]] = Dirt

			if event.key == K_z:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[Dirt]>0:
					inventory[Dirt] -= 1
					tilemap[playerPos[1]][playerPos[0]] = Dirt
					inventory[currentTile]+=1
			if event.key == K_x:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[Grass]>0:
					inventory[Grass] -= 1
					tilemap[playerPos[1]][playerPos[0]] = Grass
					inventory[currentTile]+=1
			if event.key == K_c:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[Water]>0:
					inventory[Water] -= 1
					tilemap[playerPos[1]][playerPos[0]] = Water
					inventory[currentTile]+=1
			if event.key == K_v:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[Coal]>0:
					inventory[Coal] -= 1
					tilemap[playerPos[1]][playerPos[0]] = Coal
					inventory[currentTile]+=1

	CloudPos[0]+=3
	if CloudPos[0]>MAPWIDTH*TILESIZE:
		CloudPos[0] = 0
		CloudPos[1] = random.randint(0,MAPHEIGHT*TILESIZE)

	CloudPos1[0]+=2
	if CloudPos1[0]>MAPWIDTH*TILESIZE:
		CloudPos1[0] = 0
		CloudPos1[1] = random.randint(0,MAPHEIGHT*TILESIZE)

	for row in xrange(MAPHEIGHT):
		for column in xrange(MAPWIDTH):
			#pygame.draw.rect(Display,colours[tilemap[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
			Display.blit(textures[tilemap[row][column]],(column*TILESIZE,row*TILESIZE))
	Display.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	Display.blit(textures[Cloud],(CloudPos[0],CloudPos[1]-50))
	Display.blit(textures[Cloud1],(CloudPos1[0],CloudPos1[1]-50))
	
	placePosition = 10
	for item in resources:
		Display.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition+=20
		textObj = INVFONT.render(str(inventory[item]),True,WHITE,Black)
		Display.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition+=70

	pygame.display.update()