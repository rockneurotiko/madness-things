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

			if isinstance(block, MovingPlatform):
				self.rect.x += block.change_x

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

class MovingPlatform(Platform):
	change_x = 0
	change_y = 0

	boundary_top = 0
	boundary_bottom = 0
	boundary_left = 0
	boundary_right = 0
	
	player = None
	level = None

	def update(self):
		self.rect.x += self.change_x

		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# If we are moving right, set our right side
			# to the left side of the item we hit
			if self.change_x < 0:
				self.player.rect.right = self.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.player.rect.left = self.rect.right

		self.rect.y += self.change_y
		hit = pygame.sprite.collide_rect(self, self.player)
		if hit:
			# If we are moving right, set our right side
			# to the left side of the item we hit
			if self.change_y < 0:
				self.player.rect.bottom = self.rect.top
			else:
				# Otherwise if we are moving left, do the opposite.
				self.player.rect.top = self.rect.bottom

		# Check the boundaries and see if we need to reverse
		# direction.
		if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
			self.change_y *= -1
		cur_pos = self.rect.x - self.level.world_shift
		if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
			self.change_x *= -1


class Level(object):
	#Super class
	platform_list = None
	enemy_list = None

	background = None

	world_shift = 0
	level_limit = -1000

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
	def shift_world(self, shift_x):
		""" When the user moves left/right and we need to scroll everything:
		"""
		# Keep track of the shift amount
		self.world_shift += shift_x
		# Go through all the sprite lists and shift
		for platform in self.platform_list:
			platform.rect.x += shift_x
		for enemy in self.enemy_list:
			enemy.rect.x += shift_x

class Level_01(Level):
	def __init__(self, player):
		Level.__init__(self, player)

		self.level_limit = -1500
		level = [[210, 70, 500, 500],
				[210, 70, 800, 400],
				[210, 70, 1000, 500],
				[210, 70, 1120, 280],]
		for plat in level:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			self.platform_list.add(block)

		# Add a custom moving platform
		block = MovingPlatform(70, 40)
		block.rect.x = 1350
		block.rect.y = 280
		block.boundary_left = 1350
		block.boundary_right = 1600
		block.change_x = 1
		block.player = self.player
		block.level = self
		self.platform_list.add(block)

# Create platforms for the level
class Level_02(Level):
	""" Definition for level 2. """
	def __init__(self, player):
		""" Create level 1. """
		# Call the parent constructor
		Level.__init__(self, player)
		self.level_limit = -1000
		# Array with type of platform, and x, y location of the platform.
		level = [[210, 70, 500, 550],
		[210, 70, 800, 400],
		[210, 70, 1000, 500],
		[210, 70, 1120, 280],]
		# Go through the array above and add platforms
		for platform in level:
			block = Platform(platform[0], platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platform_list.add(block)
		# Add a custom moving platform
		block = MovingPlatform(70, 70)
		block.rect.x = 1500
		block.rect.y = 300
		block.boundary_top = 100
		block.boundary_bottom = 550
		block.change_y = -1
		block.player = self.player
		block.level = self
		self.platform_list.add(block)

def main():
	pygame.init()
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption('jumper')
	pygame.mouse.set_visible(False)

	player = Player()
	lvl_list = []
	lvl_list.append(Level_01(player))
	lvl_list.append(Level_02(player))

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

		# If the player gets near the right side, shift the world left (-x)
		if player.rect.x >= 500:
			diff = player.rect.x - 500
			player.rect.x = 500
			current_lvl.shift_world(-diff)
		# If the player gets near the left side, shift the world right (+x)
		if player.rect.x <= 120:
			diff = 120 - player.rect.x
			player.rect.x = 120
			current_lvl.shift_world(diff)

		# If the player gets to the end of the level, go to the next level
		current_position = player.rect.x + current_lvl.world_shift
		if current_position < current_lvl.level_limit:
			if current_lvl_no < len(lvl_list)-1:
				player.rect.x = 120
				current_lvl_no += 1
				current_lvl = lvl_list[current_lvl_no]
				player.level = current_lvl
			else:
				# Out of levels. This just exits the program.
				# You'll want to do something better.
				done = True

		"""
		if player.rect.right > size[0]:
			player.rect.right = size[0]

		if player.rect.left < 0:
			player.rect.left = 0
		"""
		current_lvl.draw(screen)
		active_sprite_list.draw(screen)

		pygame.display.flip()

		clock.tick(60)

	pygame.quit()

if __name__ == '__main__':
	main()