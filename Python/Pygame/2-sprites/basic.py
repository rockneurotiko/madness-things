import pygame
import random

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

size = (700, 500)


class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y += 1

		if self.rect.y > size[1]:
			self.reset_pos() 
	def reset_pos(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, size[0])


pygame.init()


pygame.mouse.set_visible(False)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
#Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

blocks = pygame.sprite.Group()

sprites = pygame.sprite.Group()

for i in range(50):
	block = Block(BLACK, 20, 15)
	block.rect.x = random.randrange(size[0]) 
	block.rect.y = random.randrange(size[1])

	blocks.add(block)
	sprites.add(block)

player = Block(RED, 20, 15)
sprites.add(player) 

score = 0
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(WHITE)

	player.rect.x, player.rect.y = pygame.mouse.get_pos()
	blocks_hit_list = pygame.sprite.spritecollide(player, blocks, False)  # El ultimo boolean, si es True, elimina las colisiones
	
	for i in blocks_hit_list:
		score += 1
		print(score)
		i.reset_pos()

	blocks.update()
	sprites.draw(screen)


	#pygame.display.flip()

	pygame.display.flip()
	clock.tick(60)

pygame.quit()