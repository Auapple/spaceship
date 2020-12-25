import pygame as pg, random, math
pg.init()

screen = pg.display.set_mode([1400,800])
pg.display.set_caption('galaxy spaceship')
bg = pg.image.load("bestgalaxy.png")
bg = pg.transform.scale(bg,(1400,800))
screen.blit(bg, (0,0))


class Ship(pg.sprite.Sprite):
	x = 50
	y = 337
	speed = 8
	health = 100

	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("ship.jpg")
		self.image = pg.transform.scale(self.image,(126,94))
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 337

	def moveup(self):
		self.speed = 8
		self.rect.y -= self.speed

	def movedown(self):
		self.speed = 8
		self.rect.y += self.speed


class Rocket(pg.sprite.Sprite):

	def __init__(self,y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("rocket.jfif")
		self.image = pg.transform.scale(self.image,(100,60))
		self.x = 1450
		self.speed = 20
		self.y = rockey
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = rockey

	def update(self):
		self.rect.x -= self.speed


class Meteor(pg.sprite.Sprite):

	def __init__(self,y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('meteor.png')
		self.image = pg.transform.scale(self.image,(100,100))
		self.x =1450
		self.y = meteoy
		self.speed = 10
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = meteoy

	def update(self):
		self.rect.x -= self.speed


class Rock(pg.sprite.Sprite):

	def __init__(self,y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('rock.png')
		self.image = pg.transform.scale(self.image,(100,72))
		self.x =1450
		self.y = rocy
		self.speed = 10
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = rocy

	def update(self):
		self.rect.x -= self.speed


enemy = 0
rockey = random.randint(0,740)
meteoy = random.randint(0,700)
rocy = random.randint(0,728)
allsprite = pg.sprite.Group()
crashing = pg.sprite.Group()
rocket = Rocket(rockey)
meteor = Meteor(meteoy)
rock = Rock(rocy)
crashing.add(rocket)
crashing.add(meteor)
crashing.add(rock)
allsprite.add(rocket)
allsprite.add(meteor)
allsprite.add(rock)
ship = Ship()
allsprite.add(ship)
allsprite.draw(screen)

running = True
playing = False
clock = pg.time.Clock()
keys = pg.key.get_pressed()
crash = pg.sprite.spritecollide(ship, crashing, True)
score = 0
font = pg.font.SysFont("Arial",50)

while running:
	clock.tick(60)
	crash = pg.sprite.spritecollide(ship, crashing, True)
	if enemy > 120:
		rockey = random.randint(0,740)
		meteoy = random.randint(0,700)
		rocy = random.randint(0,728)
		rocket = Rocket(rockey)
		meteor = Meteor(meteoy)
		rock = Rock(rocy)
		crashing.add(rocket)
		crashing.add(meteor)
		crashing.add(rock)
		allsprite.add(rocket)
		allsprite.add(meteor)
		allsprite.add(rock)
		enemy = 0		
	enemy += 1
	text = font.render('score:' + str(score), True, (212,201,106))
	text.set_alpha(127)
	# pg.display.flip()
	bg = pg.image.load("bestgalaxy.png")
	bg = pg.transform.scale(bg,(1400,800))
	bg.blit(text,(130,10))
	pg.display.update()
	allsprite.update()
	keys = pg.key.get_pressed()
	if keys[pg.K_s]:
		if ship.rect.y <= 674:
			Ship.movedown(ship)
	elif keys[pg.K_w]:
		if ship.rect.y >= 0:
			Ship.moveup(ship)
	if crash:
		running = False
	screen.blit(bg, (0,0))
	allsprite.draw(screen)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False 
	pg.display.update()
pg.quit()