import pygame as pg, random, math
pg.init()

screen = pg.display.set_mode([1400,800])
pg.display.set_caption('galaxy spaceship')
bg = pg.image.load("bestgalaxy.png")
bg = pg.transform.scale(bg,(1400,800))
screen.blit(bg, (0,0))

class Bird(pg.sprite.Sprite):
	x = 50
	y = 350
	speed = 0

	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("ship.png")
		self.image = pg.transform.scale(self.image,(100,85))
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 350
