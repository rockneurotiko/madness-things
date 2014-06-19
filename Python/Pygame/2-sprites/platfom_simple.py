import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 255)
RED = ( 255, 0, 0)
GREEN = ( 0, 255, 0)

size = (800, 600)

class Player(pygame.sprite.Sprite):

	change_x = 0
	change_y = 0

	level = None
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		#The player. take an image, but now a shit
		self.image = pygame.Surface([40,60])
		self.image.fill(RED)

		self.rect = self.image.get_rect()
	def update(self):
		#Move
		#Gravity
		self.calc_grav()

		#Move l/r
		self.rect.x += self.change_x
		#Check collissions
		blocks_hit = pygame.sprite.spritecollide(self,\
		 self.level.platform_list, False)
		for block in blocks_hit:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				self.rect.left = block.rect.right
		#Move u/d
		self.rect.y += self.change_y
		#Check collissions
		blocks_hit = pygame.sprite.spritecollide(self,\
		 self.level.platform_list, False)
		for block in blocks_hit:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
			self.change_y = 0

	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35

		if self.rect.y >= size[1] - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = size[1] - self.rect.height
	
	def jump(self):
		#Saltar
		#Movemos dos pixeles, vemos si haf colision, y si la hay, se salta
		self.rect.y += 2
		platform_hit = pygame.sprite.spritecollide(self, \
			self.level.platform_list, False)
		self.rect.y -= 2

		if len(platform_hit) > 0 or self.rect.bottom >= size[1]:
			self.change_y = -10

	def go_left(self):
		self.change_x = -6
	def go_right(self):
		self.change_x = 6
	def stop(self):
		self.change_x = 0


class Platform(pygame.sprite.Sprite):
	def __init__(self, w, h):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([w,h])
		self.image.fill(GREEN)

		self.rect = self.image.get_rect()

class Level(object):
	#Super class
	platform_list = None
	enemy_list = None

	background = None

	def __init__(self, player):
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player

	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen):
		screen.fill(BLUE)
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)

class Level01(Level):
	def __init__(self, player):
		Level.__init__(self, player)
		level = [[210, 70, 500, 500],
				[210, 70, 200, 400],
				[210, 70, 600, 300],]
		for plat in level:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			self.platform_list.add(block)

def main():
	pygame.init()
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption('jumper')
	pygame.mouse.set_visible(False)

	player = Player()
	lvl_list = []
	lvl_list.append(Level01(player))

	current_lvl_no = 0
	current_lvl = lvl_list[current_lvl_no]

	active_sprite_list = pygame.sprite.Group()
	player.level = current_lvl

	player.rect.x = 340
	player.rect.y = size[1] - player.rect.height
	active_sprite_list.add(player)

	done = False

	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done = True # Flag that we are done so we exit this loop
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.go_left()
				if event.key == pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.jump()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.change_x > 0:
					player.stop()

		active_sprite_list.update()

		current_lvl.update()

		
		if player.rect.right > size[0]:
			player.rect.right = size[0]

		if player.rect.left < 0:
			player.rect.left = 0

		current_lvl.draw(screen)
		active_sprite_list.draw(screen)

		pygame.display.flip()

		clock.tick(60)

	pygame.quit()

if __name__ == '__main__':
	main()