# what can this be?
import math
import numpy as np
import pygame as pygame
from Planet import Planet
import random

# important definitions
gravitational_constant = 1
sim_speed = 0.05
G = 10

screen_size = [1500, 1000]

# setup the pygame window
pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

planets = [
    Planet(initial_velocity=[0,0], initial_position=[screen_size[0]/2,screen_size[1]/2], radius=5, mass=10000, colour=(255, 255, 0), sim_speed=0, G=G), # with sim_speed = 0 we can simulate the sun to be the center of the universe
    Planet(initial_velocity=[0, 33], initial_position=[850, 500], radius=2, mass=1, colour=(0, 255, 0), sim_speed=sim_speed, G=G)
    #Planet(initial_velocity=[0, 5], initial_position=[150, 400], radius=2, mass=1, colour=(0, 0, 255), sim_speed=sim_speed, G=G)    
]

#create some random planets
#for i in range(1):
#    planets.append(Planet(initial_velocity=[random.randrange(-20, 20), random.randrange(-20, 20)], initial_position=[random.randrange(screen_size[0]), random.randrange(screen_size[1])], radius=2, mass=1, colour=(255, 255, 255), sim_speed=sim_speed, G=G))





# functions for the game
# the main function, will be repeated every frame (dont quote me on this)
def main():
    # background color to black
    screen.fill((0, 0, 0))

    for p in planets:
        p.update_velocity(planets)

    for p in planets:
        p.update_position()

        pygame.draw.circle(screen, p.colour, p.position, p.radius)


    #check all planets if they are out of reach

    clock.tick(60)
    







# loop for the game -> put all code into the main function in this code
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # calculate the average position of all planets
            x = 0
            y = 0
            for p in planets:
                x += p.position[0]
                y += p.position[1]
            
            print('Average Position: (' + str(x / 101) + ', ' + str(y / 101) + ')')

            running = False
    main()
    # updates the diplay, without this it is not updated and a black window s presented
    pygame.display.flip()
pygame.quit()