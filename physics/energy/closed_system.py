import math
import numpy as np
import pygame as pygame


sim_speed = 0.1

class Ball:
    def __init__(self, mass, init_position, init_vel, screen_size) -> None:
        self.mass = mass
        self.velocity = init_vel
        self.position = init_position
        self.screen_size = screen_size
        self.gravity = 9.81
        self.radius = 10

    def get_height(self):
        return self.screen_size[1] - self.position[1]

    def get_potential_energy(self):
        return self.mass * self.gravity * self.get_height()
    
    def get_kinetic_energy(self):
        return 0.5 * self.mass * (math.sqrt((self.velocity[0])**2 + (self.velocity[1])**2))**2

    def update(self, sim_speed):
        # update the velocity of the body
        self.velocity[1] += (self.gravity * sim_speed)

        # update the position of the body
        next_x = self.position[0] + self.velocity[0] * sim_speed
        next_y = self.position[1] + self.velocity[1] * sim_speed

        #check if the ball is still in the bounds
        if((next_y + self.radius) > self.screen_size[1] or (next_y - self.radius) < 0):
            self.velocity[1] *= -1
        
        self.position[0] = next_x
        self.position[1] = next_y





#init the game window
screen_size = [1000, 1000]
pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


ball = Ball(mass=10, init_position=[20, 20], init_vel=[0,0], screen_size=screen_size)
def main():
    clock.tick(60)
    print(clock.get_fps())

    # draw the ball
    ball.update(sim_speed=sim_speed)
    pygame.draw.circle(screen, (0, 0, 255), ball.position, ball.radius)

    #draw the two graphs for the kinetic and the potential energy
    #kinetic
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen_size[0] - 40, 0, 40, ball.get_kinetic_energy() / 95))
    #potential (under kinetic to show that it does not change)
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(screen_size[0] - 40, ball.get_kinetic_energy() / 95, 40, ball.get_potential_energy() / 95))





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    main()
    pygame.display.flip()
pygame.quit()

