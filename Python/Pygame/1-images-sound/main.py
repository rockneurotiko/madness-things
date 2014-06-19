import pygame

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

pygame.init()

size = (700, 500)

pygame.mouse.set_visible(False)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
#Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

fondo = pygame.image.load('fondo.jpg').convert()
p1_image = pygame.image.load('p1_ship.png').convert()
p1_image.set_colorkey(BLACK)

click_sound = pygame.mixer.Sound('laser5.ogg')

# screen.blit(fondo, [0,0])
# pygame.display.flip()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			click_sound.play()


	p1_position = pygame.mouse.get_pos()
	screen.blit(fondo, [0,0])
	screen.blit(p1_image, p1_position)

	#pygame.display.flip()

	pygame.display.flip()
	clock.tick(60)

pygame.quit()