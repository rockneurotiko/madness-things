"""
Show how to use a sprite backed by a graphic.
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
Explanation video: http://youtu.be/vRB_983kUMc
"""
import pygame
import random
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
#Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#Man in mouse
pygame.mouse.set_visible(False)

key_x = 10
key_y = 10

key_x_speed = 0
key_y_speed = 0


"""
#Cuadro moving
rect_x = 50
rect_y = 50

speed_x = 5
speed_y = 5
"""

"""
# SNOW
snow_list = []
for i in range(50):
	x = random.randrange(0,700)
	y = random.randrange(0,500)
	snow_list.append([x,y])
"""

def draw_stick_figure(screen, x, y):
	# Head
	pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)
	# Legs
	pygame.draw.line(screen, BLACK ,[5+x,17+y], [10+x,27+y], 2)
	pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)
	# Body
	pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)
	# Arms
	pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
	pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)



# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				key_x_speed = -3
			if event.key == pygame.K_RIGHT:
				key_x_speed = 3
			if event.key == pygame.K_UP:
				key_y_speed = -3
			if event.key == pygame.K_DOWN:
				key_y_speed = 3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				key_x_speed = 0
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				key_y_speed = 0



	# --- Game logic should go here
	# --- Drawing code should go here
	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	#screen.fill(BLACK)
	screen.fill(WHITE)

	#Draw with mouse
	#pos = pygame.mouse.get_pos()
	#draw_stick_figure(screen, pos[0], pos[1])
	
	key_x += key_x_speed
	key_y += key_y_speed
	draw_stick_figure(screen, key_x, key_y)
	

	"""
	# NIEVE
	for i in range(len(snow_list)):
		pygame.draw.circle(screen, WHITE, snow_list[i], 2)
		snow_list[i][1] += 1
		if snow_list[i][1] > 500:
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			x = random.randrange(0, 700)
			snow_list[i][0] = x
	"""

	"""
	# Cuadrado moviendose
	pygame.draw.rect(screen, WHITE, [rect_x,rect_y,50,50])
	pygame.draw.rect(screen, RED, [rect_x+10,rect_y+10,30,30])
	if rect_x > 650:
		speed_x = speed_x * -1
	if rect_x < 0:
		speed_x = speed_x * -1		
	if rect_y > 450:
		speed_y = speed_y * -1
	if rect_y < 0:
		speed_y = speed_y * -1

	rect_x += speed_x
	rect_y += speed_y
	"""
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	# --- Limit to 60 frames per second
	clock.tick(60)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()