import pygame as pg, random, math
pg.init()

#game display part
screen = pg.display.set_mode([1400,800])
pg.display.set_caption('galaxy spaceship')
bg = pg.image.load("bestgalaxy.png")
bg = pg.transform.scale(bg,(1400,800))
screen.blit(bg, (0,0))


#class part
class Ship(pg.sprite.Sprite):
	x = 50
	y = 337
	speed = 8

	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("ship.png")
		self.image = pg.transform.scale(self.image,(126,94))
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 337
		self.health = 100

	def moveup(self):
		self.speed = 8
		self.rect.y -= self.speed

	def movedown(self):
		self.speed = 8
		self.rect.y += self.speed




class Rocket(pg.sprite.Sprite):

	def __init__(self,y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("rocket.png")
		self.image = pg.transform.scale(self.image,(100,60))
		self.x = 1450
		self.speed = 20
		self.y = rockey
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = rockey
		self.health = 1

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
		self.health = 200

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
		self.health = 100

	def update(self):
		self.rect.x -= self.speed

class Bullet(pg.sprite.Sprite):

	def __init__(self,y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('bullet.png')
		self.image = pg.transform.scale(self.image,(37,17))
		self.x =146
		self.y = shipy
		self.speed = 30
		self.rect = self.image.get_rect()
		self.rect.x = 146
		self.rect.y = shipy + 38

	def update(self):
		self.rect.x += self.speed


class Redship(pg.sprite.Sprite):

	def __init__(self,y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('enemyship.png')
		self.image = pg.transform.scale(self.image,(140,126))
		self.x = 1450
		self.y = redshipy
		self.speed = 5
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = redshipy
		self.health = 400

	def update(self):
		self.rect.x -= self.speed


class Grayship(pg.sprite.Sprite):

	def __init__(self,y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('othership.png')
		self.image = pg.transform.scale(self.image,(140,140))
		self.x = 1450
		self.y = grayshipy
		self.speed = 8
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = grayshipy
		self.health = 300

	def update(self):
		self.rect.x -= self.speed


class Redbiu(pg.sprite.Sprite):

	def __init__(self,redshipy,redshipx):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('enemybiu.png')
		self.image = pg.transform.scale(self.image,(42,30))
		self.x = redshipx
		self.y = redshipy
		self.speed = 30
		self.rect = self.image.get_rect()
		self.rect.x = redshipx
		self.rect.y = redshipy

	def update(self):
		self.rect.x -= self.speed


class Graybiu(pg.sprite.Sprite):

	def __init__(self,grayshipy,grayshipx):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('enemybiu.png')
		self.image = pg.transform.scale(self.image,(42,30))
		self.x = grayshipx
		self.y = grayshipy
		self.speed = 30
		self.rect = self.image.get_rect()
		self.rect.x = grayshipx
		self.rect.y = grayshipy

	def update(self):
		self.rect.x -= self.speed


class Fireball(pg.sprite.Sprite):

	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('fireball.png')
		self.image = pg.transform.scale(self.image,(1600,800))
		self.x =1450
		self.y = 0
		self.speed = 3
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = 0
		self.health = 3000

	def update(self):
		self.rect.x -= self.speed

#the sprite part
enemy = 0
redshoot = 0
grayshoot = 0
allsprite = pg.sprite.Group()
crashing = pg.sprite.Group()
# from here
redshipy = random.randint(0,674)
grayshipy = random.randint(0,660)
rockey = random.randint(0,740)
meteoy = random.randint(0,700)
rocy = random.randint(0,728)
redship = Redship(redshipy)
grayship = Grayship(grayshipy)
fireball = Fireball()
rocket = Rocket(rockey)
meteor = Meteor(meteoy)
rock = Rock(rocy)
crashing.add(redship)
crashing.add(grayship)
crashing.add(rocket)
crashing.add(meteor)
crashing.add(rock)
crashing.add(fireball)
allsprite.add(redship)
allsprite.add(grayship)
allsprite.add(rocket)
allsprite.add(meteor)
allsprite.add(rock)
allsprite.add(fireball)
# to here
ship = Ship()
allsprite.add(ship)
allsprite.draw(screen)

#the get shot part
shipy = ship.rect.y
bullet = Bullet(shipy)
redshipshot = pg.sprite.collide_rect(bullet, redship)
grayshipshot = pg.sprite.collide_rect(bullet, grayship)
rocketshot = pg.sprite.collide_rect(bullet, rocket)
meteorshot = pg.sprite.collide_rect(bullet, meteor)
rockshot = pg.sprite.collide_rect(bullet, rock)
fireballshot = pg.sprite.collide_rect(bullet, fireball)

#the running and settings part
running = True
playing = False
clock = pg.time.Clock()
keys = pg.key.get_pressed()
crash = pg.sprite.spritecollide(ship, crashing, True)
diebyfireball = pg.sprite.collide_rect(ship, fireball)
score = 0
font = pg.font.SysFont("Arial",50)
level1 = True

# game run part
while running:
	clock.tick(60)
	crash = pg.sprite.spritecollide(ship, crashing, True)
	disappear = pg.sprite.spritecollide(bullet, crashing, True)
	if enemy > 120:
		# from here
		redshipy = random.randint(0,674)
		grayshipy = random.randint(0,660)
		rockey = random.randint(0,740)
		meteoy = random.randint(0,700)
		rocy = random.randint(0,728)
		redship = Redship(redshipy)
		grayship = Grayship(grayshipy)
		rocket = Rocket(rockey)
		meteor = Meteor(meteoy)
		rock = Rock(rocy)
		crashing.add(redship)
		crashing.add(grayship)
		crashing.add(rocket)
		crashing.add(meteor)
		crashing.add(rock)
		allsprite.add(redship)
		allsprite.add(grayship)
		allsprite.add(rocket)
		allsprite.add(meteor)
		allsprite.add(rock)
		# to here
		enemy = 0		
	enemy += 1
	text = font.render('score:' + str(score), True, (212,201,106))
	text.set_alpha(127)
	health = font.render('health:' + str(ship.health), True, (212,201,106))
	health.set_alpha(127)
	bg = pg.image.load("bestgalaxy.png")
	bg = pg.transform.scale(bg,(1400,800))
	bg.blit(text,(130,10))
	bg.blit(health,(400,10))
	pg.display.update()
	
	# the ship part
	keys = pg.key.get_pressed()
	if keys[pg.K_s]:
		if ship.rect.y <= 674:
			Ship.movedown(ship)
	if keys[pg.K_w]:
		if ship.rect.y >= 0:
			Ship.moveup(ship)
	if keys[pg.K_SPACE]:
		shipy = ship.rect.y
		bullet = Bullet(shipy)
		allsprite.add(bullet)
	if crash:
		ship.health -= 20
	if ship.health <= 0:
		running = False
	if disappear:
		allsprite.remove(bullet)
	if diebyfireball:
		running = False
	redshipshot = pg.sprite.collide_rect(bullet, redship)
	grayshipshot = pg.sprite.collide_rect(bullet, grayship)
	rocketshot = pg.sprite.collide_rect(bullet, rocket)
	meteorshot = pg.sprite.collide_rect(bullet, meteor)
	rockshot = pg.sprite.collide_rect(bullet, rock)
	fireballshot = pg.sprite.collide_rect(bullet, fireball)

	# the enemybiu part
	redshoot += 1
	grayshoot += 1
	if redshoot >= 40:
		redshipx = redship.rect.x
		redbiu = Redbiu(redshipy,redshipx)
		crashing.add(redbiu)
		allsprite.add(redbiu)
		redshoot = 0

	if grayshoot >= 70:
		grayshipx = grayship.rect.x
		graybiu = Graybiu(grayshipy,grayshipx)
		crashing.add(graybiu)
		allsprite.add(graybiu)
		grayshoot = 0

	# the enemy part
	if redshipshot:
		redship.health -= 10
	if redship.health <= 0:
		crashing.remove(redship)
		allsprite.remove(redship)
		screen.blit(bg, (0,0))
		score += 100

	if grayshipshot:
		grayship.health -= 10
	if grayship.health <= 0:
		crashing.remove(grayship)
		allsprite.remove(grayship)
		screen.blit(bg, (0,0))
		score += 70

	if rocketshot:
		rocket.health -= 10
	if rocket.health <= 0:
		crashing.remove(rocket)
		allsprite.remove(rocket)
		screen.blit(bg, (0,0))
		score += 20

	if meteorshot:
		meteor.health -= 10
	if meteor.health <= 0:
		crashing.remove(meteor)
		allsprite.remove(meteor)
		screen.blit(bg, (0,0))
		score += 30

	if rockshot:
		rock.health -= 10
	if rock.health <= 0:
		crashing.remove(rock)
		allsprite.remove(rock)
		screen.blit(bg, (0,0))
		score += 30

	if fireballshot:
		fireball.health -= 10
	if fireball.health <= 0:
		crashing.remove(fireball)
		allsprite.remove(fireball)
		screen.blit(bg, (0,0))

	# the level part
	if level1:
		if score >= 500:
			fireball = Fireball()
			crashing.add(fireball)
			allsprite.add(fireball)
			level1 = False
	shipy = ship.rect.y
	bullet = Bullet(shipy) 
	allsprite.update()
	screen.blit(bg, (0,0))
	allsprite.draw(screen)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False 
	pg.display.update()
pg.quit()