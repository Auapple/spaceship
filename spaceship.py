import pygame as pg, random, math
pg.init()

#Game display part
screen = pg.display.set_mode([1400,800])
pg.display.set_caption('galaxy spaceship')
galaxy = pg.image.load("bestgalaxy.png")
bg = pg.transform.scale(galaxy,(1400,800))
screen.blit(bg, (0,0))
explo1 = pg.image.load('explosion1.png')
explo2 = pg.image.load('explosion2.png')
explo3 = pg.image.load('explosion3.png')
explo4 = pg.image.load('explosion4.png')
explo1 = pg.transform.scale(explo1,(100,100))
explo2 = pg.transform.scale(explo2,(100,100))
explo3 = pg.transform.scale(explo3,(100,100))
explo4 = pg.transform.scale(explo4,(100,100))
picture = [explo1,explo2,explo3,explo4]
bullpic = pg.image.load('bullet.png')
bullpic = pg.transform.scale(bullpic,(37,17))

#Class part
class Ship(pg.sprite.Sprite):
	x = 50
	y = 337
	speed = 16

	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("ship.png")
		self.image = pg.transform.scale(self.image,(126,94))
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 337
		self.health = 100
		self.speed = 16

	def moveup(self):
		self.rect.y -= self.speed

	def movedown(self):
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
		self.health = 150

	def update(self):
		self.rect.x -= self.speed

class Bullet(pg.sprite.Sprite):

	def __init__(self,y):
		pg.sprite.Sprite.__init__(self)
		self.image = bullpic
		self.x = 146
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
		self.redshoot = 0

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
		self.grayshoot = 0

	def update(self):
		self.rect.x -= self.speed


class Redbiu(pg.sprite.Sprite):

	def __init__(self,redshipy,redshipx):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('enemybiu.png')
		self.image = pg.transform.scale(self.image,(42,30))
		self.x = redshipx
		self.y = redshipy + 48
		self.speed = 30
		self.rect = self.image.get_rect()
		self.rect.x = redshipx
		self.rect.y = redshipy + 48

	def update(self):
		self.rect.x -= self.speed


class Graybiu(pg.sprite.Sprite):

	def __init__(self,grayshipy,grayshipx):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('enemybiu.png')
		self.image = pg.transform.scale(self.image,(42,30))
		self.x = grayshipx
		self.y = grayshipy + 55
		self.speed = 30
		self.rect = self.image.get_rect()
		self.rect.x = grayshipx
		self.rect.y = grayshipy + 55

	def update(self):
		self.rect.x -= self.speed


class Bossbiu(pg.sprite.Sprite):

	def __init__(self,bossy,bossx):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('enemybiu.png')
		self.image = pg.transform.scale(self.image,(42,30))
		self.x = bossx
		self.y = bossy
		self.speed = 30
		self.rect = self.image.get_rect()
		self.rect.x = bossx
		self.rect.y = bossy

	def update(self):
		self.rect.x -= self.speed


class Fireball(pg.sprite.Sprite):

	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('fireball.png')
		self.image = pg.transform.scale(self.image,(1600,800))
		self.x =1450
		self.y = 0
		self.speed = 1
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = 0
		self.health = 300

	def update(self):
		self.rect.x -= self.speed


class Fireflake(pg.sprite.Sprite):

	def __init__(self,x,y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('fireball.png')
		self.image = pg.transform.scale(self.image,(600,300))
		self.x = x
		self.y = y
		self.speed = 4
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.health = 500

	def update(self):
		self.rect.x -= self.speed

class Explosion(pg.sprite.Sprite):

	def __init__(self,explox,exploy):
		pg.sprite.Sprite.__init__(self)
		global picture
		self.image = picture[0]
		self.rect = self.image.get_rect()
		self.rect.x = explox
		self.rect.y = exploy
		picture = [explo1,explo2,explo3,explo4]
		self.count = 0

	def update(self):
		if self.count < 4:
			self.image = picture[self.count]
			self.image = pg.transform.scale(self.image,(100,100))
			self.count += 1

class Cogwheel(pg.sprite.Sprite):

	def __init__(self,cogy):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('cogwheel.jpg')
		self.image = pg.transform.scale(self.image,(50,50))
		self.rect = self.image.get_rect()
		self.rect.x = 1450
		self.rect.y = cogy

	def update(self):
		self.rect.x -= 4	

class Boss(pg.sprite.Sprite):

	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load('enemyboss.png')
		self.image = pg.transform.scale(self.image,(800,800))
		self.rect = self.image.get_rect()
		self.rect.x = 1420
		self.rect.y = 0
		self.count = 0
		self.speed = 2
		self.bossshoot = 0
		self.bossrocket = 0
		self.health = 3000

	def update(self):
		if self.rect.x >= 700:
			self.rect.x -= self.speed

class Missile(pg.sprite.Sprite):

	def __init__(self,y,bossx):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("missile.png")
		self.image = pg.transform.scale(self.image,(100,28))
		self.x = bossx
		self.speed = 20
		self.y = missiley
		self.rect = self.image.get_rect()
		self.rect.x = bossx
		self.rect.y = missiley
		self.health = 1

	def update(self):
		self.rect.x -= self.speed


#The sprite part
enemy = 0
redshoot = 0
grayshoot = 0
cog = 0
allsprite = pg.sprite.Group()
crashing = pg.sprite.Group()
redships = pg.sprite.Group()
grayships = pg.sprite.Group()
rockets = pg.sprite.Group()
meteors = pg.sprite.Group()
rocks = pg.sprite.Group()
fireballs = pg.sprite.Group()
fireflakes = pg.sprite.Group()
enemybius = pg.sprite.Group()
bullets = pg.sprite.Group()
explosions = pg.sprite.Group()
cogwheels = pg.sprite.Group()
bosses = pg.sprite.Group()
missiles = pg.sprite.Group()
explox = 200
exploy = 200


# from here
redshipy = random.randint(0,674)
grayshipy = random.randint(0,660)
rockey = random.randint(0,740)
meteoy = random.randint(0,700)
rocy = random.randint(0,728)
redship = Redship(redshipy)
grayship = Grayship(grayshipy)
fireball = Fireball()
fireflake = Fireflake(-600,0)
boss = Boss()
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
redships.add(redship)
grayships.add(grayship)
rockets.add(rocket)
meteors.add(meteor)
rocks.add(rock)
#fireballs.add(fireball)
# to here
ship = Ship()
allsprite.add(ship)
allsprite.draw(screen)

#the running and settings part
running = True
playing = False
clock = pg.time.Clock()
keys = pg.key.get_pressed()
score = 0
font = pg.font.SysFont("Arial",50)
bigword = pg.font.SysFont('Arial',350)
level1 = True
level2 = True
level3 = True
second = 0
movement = True
win = False


# game run part
while running:
	clock.tick(60)
	diebyfireball = pg.sprite.collide_rect(ship, fireball)
	diebyfireflake = pg.sprite.collide_rect(ship,fireflake)
	crash = pg.sprite.spritecollide(ship, crashing, True)
	fix = pg.sprite.spritecollide(ship, cogwheels, True)
	if enemy >= 120:
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
		redships.add(redship)
		grayships.add(grayship)
		rockets.add(rocket)
		meteors.add(meteor)
		rocks.add(rock)
		allsprite.add(redship)
		allsprite.add(grayship)
		allsprite.add(rocket)
		allsprite.add(meteor)
		allsprite.add(rock)
		# to here
		enemy = 0
	enemy += 1
	if cog >= 300:
		cogy = random.randint(0,750)
		cogwheel = Cogwheel(cogy)
		cogwheels.add(cogwheel)
		allsprite.add(cogwheel)
		cog = 0
	cog += 1
	text = font.render('score:' + str(score), True, (212,201,106))
	text.set_alpha(127)
	health = font.render('health:' + str(ship.health), True, (212,201,106))
	health.set_alpha(127)
	bg = pg.transform.scale(galaxy,(1400,800))
	bg.blit(text,(130,10))
	bg.blit(health,(400,10))
	pg.display.update()
	
	# the ship part
	keys = pg.key.get_pressed()
	if win == False:
		if movement == True:
			if keys[pg.K_s]:
				if ship.rect.y <= 674:
					Ship.movedown(ship)
			if keys[pg.K_w]:
				if ship.rect.y >= 0:
					Ship.moveup(ship)
			if keys[pg.K_SPACE]:
				shipy = ship.rect.y
				bullet = Bullet(shipy)
				bullets.add(bullet)
				allsprite.add(bullet)
	if crash:
		ship.health -= 20
		print(ship.health)
	if ship.health <= 0:
		running = False
		print('died')
	if diebyfireball:
		ship.health = 0
	if diebyfireflake:
		ship.health = 0
	if fix:
		if ship.health < 100:
			ship.health += 20

	# the enemy part
	for i in allsprite:
		if i.rect.x <= -600:
			allsprite.remove(i)
	for i in crashing:
		if i.rect.x <= -600:
			crashing.remove(i)
	for i in enemybius:
		if i.rect.x <= -600:
			enemybius.remove(i)
	for i in redships:
		if i.rect.x <= -600:
			redships.remove(i)
	for i in grayships:
		if i.rect.x <= -600:
			grayships.remove(i)
	# for i in :
	# 	if i.rect.x <= -600:
	# 		.remove(i)
	for i in redships:
		redhit = pg.sprite.spritecollide(i,bullets,True)
		if redhit:
			i.health -= 10
		i.redshoot += 1
		if i.redshoot >= 20:
			redshipx = i.rect.x
			redbiu = Redbiu(i.rect.y,i.rect.x)
			crashing.add(redbiu)
			allsprite.add(redbiu)
			enemybius.add(redbiu)
			i.redshoot = 0
		if i.health <= 0:
			redships.remove(i)
			allsprite.remove(i)
			explox = i.rect.x
			exploy = i.rect.y
			explosion = Explosion(explox,exploy)
			allsprite.add(explosion)
			explosions.add(explosion)
			crashing.add(explosion)
			score += 100

	for i in grayships:
		grayhit = pg.sprite.spritecollide(i,bullets,True)
		if grayhit:
			i.health -= 10
		i.grayshoot += 1
		if i.grayshoot >= 40:
			grayshipx = i.rect.x
			graybiu = Graybiu(i.rect.y,i.rect.x)
			crashing.add(graybiu)
			allsprite.add(graybiu)
			enemybius.add(graybiu)
			i.grayshoot = 0
		if i.health <= 0:
			grayships.remove(i)
			allsprite.remove(i)
			explox = i.rect.x
			exploy = i.rect.y
			explosion = Explosion(explox,exploy)
			allsprite.add(explosion)
			explosions.add(explosion)
			crashing.add(explosion)
			score += 70

	for i in rockets:
		rockethit = pg.sprite.spritecollide(i,bullets,True)
		if rockethit:
			i.health -= 10
		if i.health <= 0:
			rockets.remove(i)
			allsprite.remove(i)
			explox = i.rect.x
			exploy = i.rect.y
			explosion = Explosion(explox,exploy)
			allsprite.add(explosion)
			explosions.add(explosion)
			crashing.add(explosion)
			score += 20

	for i in meteors:
		meteorhit = pg.sprite.spritecollide(i,bullets,True)
		if meteorhit:
			i.health -= 10
		if i.health <= 0:
			meteors.remove(i)
			allsprite.remove(i)
			score += 40

	for i in rocks:
		rockhit = pg.sprite.spritecollide(i,bullets,True)
		if rockhit:
			i.health -= 10
		if i.health <= 0:
			rocks.remove(i)
			allsprite.remove(i)
			score += 30


	# the bullet crash part
	for i in bullets:
		bullethit = pg.sprite.spritecollide(i,enemybius,True)
		if bullethit:
			bullets.remove(i)
			allsprite.remove(i)

	for i in enemybius:
		enemybiuhit = pg.sprite.spritecollide(i,bullets,True)
		if enemybiuhit:
			enemybius.remove(i)
			allsprite.remove(i)
			crashing.remove(i)

	for i in explosions:
		if i.count >= 4:
			explosions.remove(i)
			allsprite.remove(i)
			crashing.remove(i)


	# the level part
	if level1:
		if score >= 500:
			second += 1
			#movement = False
			if second <= 30:
				warning = bigword.render('WARNING', True, (255,0,0))
				bg.blit(warning,(30,200))
				screen.blit(bg, (0,0))
			if second > 30 and second <= 60:
				bg = pg.transform.scale(galaxy,(1400,800))
				text = font.render('score:' + str(score), True, (212,201,106))
				text.set_alpha(127)
				health = font.render('health:' + str(ship.health), True, (212,201,106))
				health.set_alpha(127)
				bg.blit(text,(130,10))
				bg.blit(health,(400,10))
				fireba = bigword.render('FIREBALL', True, (255,0,0))
				incoming = bigword.render('INCOMING', True, (255,0,0))
				bg.blit(fireba,(30,0))
				bg.blit(incoming,(-30,400))
				screen.blit(bg, (0,0))
			if second > 60 and second <= 90:
				bg = pg.transform.scale(galaxy,(1400,800))
				text = font.render('score:' + str(score), True, (212,201,106))
				text.set_alpha(127)
				health = font.render('health:' + str(ship.health), True, (212,201,106))
				health.set_alpha(127)
				bg.blit(text,(130,10))
				bg.blit(health,(400,10))
				sheep = bigword.render('SHIP', True, (255,0,0))
				upgraded = bigword.render('UPGRADED', True, (255,0,0))
				bg.blit(sheep,(400,0))
				bg.blit(upgraded,(-15,400))
				screen.blit(bg, (0,0))
			if second > 90 and second <= 120:
				bg = pg.transform.scale(galaxy,(1400,800))
				text = font.render('score:' + str(score), True, (212,201,106))
				text.set_alpha(127)
				health = font.render('health:' + str(ship.health), True, (212,201,106))
				health.set_alpha(127)
				bg.blit(text,(130,10))
				bg.blit(health,(400,10))
				sped = bigword.render('SPEED', True, (255,0,0))
				more = bigword.render('16 --> 24', True, (255,0,0))
				bg.blit(sped,(200,0))
				bg.blit(more,(100,400))
				screen.blit(bg, (0,0))
			if second > 120:
				bg = pg.transform.scale(galaxy,(1400,800))
				text = font.render('score:' + str(score), True, (212,201,106))
				text.set_alpha(127)
				health = font.render('health:' + str(ship.health), True, (212,201,106))
				health.set_alpha(127)
				bg.blit(text,(130,10))
				bg.blit(health,(400,10))
				screen.blit(bg, (0,0))
				fireball = Fireball()
				crashing.add(fireball)
				allsprite.add(fireball)
				fireballs.add(fireball)
				ship.speed = 24
				movement = True
				second = 0
				level1 = False
	if level2:
		if score >= 1000:
			second += 1
			#movement = False
			if second <= 30:
				bg.blit(warning,(30,200))
				screen.blit(bg, (0,0))
			if second > 30 and second <= 60:
				bg = pg.transform.scale(galaxy,(1400,800))
				text = font.render('score:' + str(score), True, (212,201,106))
				text.set_alpha(127)
				health = font.render('health:' + str(ship.health), True, (212,201,106))
				health.set_alpha(127)
				bg.blit(text,(130,10))
				bg.blit(health,(400,10))
				shipboss = bigword.render('SHIPBOSS', True, (255,0,0))
				bg.blit(shipboss,(-20,0))
				bg.blit(incoming,(-30,400))
				screen.blit(bg, (0,0))
			if second > 60 and second <= 90:
				bg = pg.transform.scale(galaxy,(1400,800))
				text = font.render('score:' + str(score), True, (212,201,106))
				text.set_alpha(127)
				health = font.render('health:' + str(ship.health), True, (212,201,106))
				health.set_alpha(127)
				bg.blit(text,(130,10))
				bg.blit(health,(400,10))
				bg.blit(sheep,(400,0))
				bg.blit(upgraded,(-15,400))
				screen.blit(bg, (0,0))
			if second > 90 and second <= 120:
				bg = pg.transform.scale(galaxy,(1400,800))
				text = font.render('score:' + str(score), True, (212,201,106))
				text.set_alpha(127)
				health = font.render('health:' + str(ship.health), True, (212,201,106))
				health.set_alpha(127)
				bg.blit(text,(130,10))
				bg.blit(health,(400,10))
				more = bigword.render('24 --> 32', True, (255,0,0))
				bg.blit(sped,(200,0))
				bg.blit(more,(100,400))
				screen.blit(bg, (0,0))
			if second > 120:
				bg = pg.transform.scale(galaxy,(1400,800))
				text = font.render('score:' + str(score), True, (212,201,106))
				text.set_alpha(127)
				health = font.render('health:' + str(ship.health), True, (212,201,106))
				health.set_alpha(127)
				bg.blit(text,(130,10))
				bg.blit(health,(400,10))
				screen.blit(bg, (0,0))
				boss = Boss()
				crashing.add(boss)
				allsprite.add(boss)
				bosses.add(boss)
				ship.speed = 32
				level2 = False


	# the boss part
	for i in fireballs:
		fireballhit = pg.sprite.spritecollide(i,bullets,True)
		fireballx = i.rect.x
		if fireballhit:
			i.health -= 10
		if i.health <= 0:
			fireballs.remove(i)
			allsprite.remove(i)
			crashing.remove(i)
			fireflake = Fireflake(fireballx,0)
			allsprite.add(fireflake)
			crashing.add(fireflake)
			fireflakes.add(fireflake)
			fireflake = Fireflake(fireballx + 150,300)
			allsprite.add(fireflake)
			crashing.add(fireflake)
			fireflakes.add(fireflake)
			fireflake = Fireflake(fireballx + 100,500)
			allsprite.add(fireflake)
			crashing.add(fireflake)
			fireflakes.add(fireflake)

	for i in fireflakes:
		fireflakehit = pg.sprite.spritecollide(i,bullets,True)
		if fireflakehit:
			i.health -= 10
		if i.health <= 0:
			fireflakes.remove(i)
			allsprite.remove(i)
			crashing.remove(i)

	for i in bosses:
		bosshit = pg.sprite.spritecollide(i,bullets,True)
		if bosshit:
			i.health -= 10
		i.bossshoot += 1
		i.bossrocket += 1
		if i.bossshoot >= 25:
			bossx = i.rect.x
			bossy = i.rect.y
			bossx += 115
			bossy += 207
			bossbiu = Bossbiu(bossy,bossx)
			crashing.add(bossbiu)
			allsprite.add(bossbiu)
			enemybius.add(bossbiu)
			bossx -= 154
			bossy += 178
			bossbiu = Bossbiu(bossy,bossx)
			crashing.add(bossbiu)
			allsprite.add(bossbiu)
			enemybius.add(bossbiu)
			bossx += 154
			bossy += 178
			bossbiu = Bossbiu(bossy,bossx)
			crashing.add(bossbiu)
			allsprite.add(bossbiu)
			enemybius.add(bossbiu)
			i.bossshoot = 0
		if i.bossrocket >= 4:
			bossx = boss.rect.x
			bossx += 400
			missiley = random.randint(0,740)
			missile = Missile(missiley,bossx)
			crashing.add(missile)
			allsprite.add(missile)
			missiles.add(missile)
			allsprite.remove(boss)
			allsprite.add(boss)
			i.bossrocket = 0
		if i.health <= 0:
			bosses.remove(i)
			allsprite.remove(i)

	for i in missiles:
		missilehit = pg.sprite.spritecollide(i,bullets,True)
		if missilehit:
			i.health -= 10
		if i.health <= 0:
			missiles.remove(i)
			allsprite.remove(i)
			explox = i.rect.x
			exploy = i.rect.y
			explosion = Explosion(explox,exploy)
			allsprite.add(explosion)
			explosions.add(explosion)
			crashing.add(explosion)

			
	# last running part
	shipy = ship.rect.y
	bullet = Bullet(shipy)
	if win == False:
		allsprite.update()
	if win == True:
		hooray = bigword.render('YOU WIN', True, (255,0,0))
		bg.blit(hooray,(100,200))
	screen.blit(bg, (0,0))
	allsprite.draw(screen)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False 
	pg.display.update()
pg.quit()