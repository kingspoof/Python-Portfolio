# what can this be?
import math
import numpy as np
import pygame as pygame
from Planet import Planet
import random
from numba import jit

# important definitions
gravitational_constant = 1
sim_speed = 4
G = 10

screen_size = [500, 500]

# setup the pygame window
pygame.init()
my_font = pygame.font.SysFont('Arial', 20)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
print(pygame.display.list_modes())

planets = [
    #Planet(initial_velocity=[0,0], initial_position=[screen_size[0]/2,screen_size[1]/2], radius=20, mass=10000, colour=(255, 255, 0), sim_speed=0, G=G), # with sim_speed = 0 we can simulate the sun to be the center of the universe
    #Planet(initial_velocity=[0, 33], initial_position=[850, 500], radius=2, mass=1, colour=(0, 255, 0), sim_speed=sim_speed, G=G)
    #Planet(initial_velocity=[0, 5], initial_position=[150, 400], radius=2, mass=1, colour=(0, 0, 255), sim_speed=sim_speed, G=G)    

    # 3 Body problem
    Planet(initial_velocity=[0, 0.2], initial_position=[150, 250], radius=2, mass=1, colour=(255, 255, 255), sim_speed=sim_speed, G=G),
    Planet(initial_velocity=[0, 0], initial_position=[250, 250], radius=2, mass=1, colour=(255, 255, 255), sim_speed=sim_speed, G=G),
    Planet(initial_velocity=[0, -0.2], initial_position=[350, 250], radius=2, mass=1, colour=(255, 255, 255), sim_speed=sim_speed, G=G)

]

#create some random planets
#for i in range(10):
    #planets.append(Planet(initial_velocity=[random.randrange(-20, 20), random.randrange(-20, 20)], initial_position=[random.randrange(screen_size[0]), random.randrange(screen_size[1])], radius=2, mass=1, colour=(255, 255, 255), sim_speed=sim_speed, G=G))





# functions for the game
# the main function, will be repeated every frame (dont quote me on this)
def main(screen, planets, clock):
    # background color to black
    screen.fill((0, 0, 0))

    for p in planets:
        p.update_velocity(planets, sim_speed)

    for p in planets:
        p.update_position(sim_speed)

        pygame.draw.circle(screen, p.colour, p.position, p.radius)
        if(len(p.last_positions) > 2):
            pygame.draw.aalines(surface=screen, color=(p.colour[0] / 6, p.colour[1] / 6, p.colour[2] / 6), closed=False, points=p.last_positions)


    #check all planets if they are out of reach
    print(clock.get_fps())
    clock.tick(60)
    



# loop for the game -> put all code into the main function in this code
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: sim_speed += 0.02
            if event.key == pygame.K_DOWN: sim_speed -= 0.02
    main(screen=screen, planets=planets, clock=clock)

    #display the current sim speed
    text_surface = my_font.render('Sim speed: ' + str(sim_speed), False, (255, 255, 255))
    screen.blit(text_surface, (2,2))

    # updates the diplay, without this it is not updated and a black window s presented
    pygame.display.flip()
    pygame.transform.smoothscale(screen, (screen_size[0] / 2, screen_size[1] / 2))

pygame.quit()