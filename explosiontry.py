import pygame as pg, random, math
pg.init()

#Game display part
screen = pg.display.set_mode([1400,800])
pg.display.set_caption('galaxy spaceship')
bg = pg.image.load("explosion3.gif")
bg = pg.transform.scale(bg,(1400,800))
screen.blit(bg, (0,0))

running = True
clock = pg.time.Clock()

while running:
	clock.tick(60)
	screen.blit(bg, (0,0))
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False 
	pg.display.update()
pg.quit()