import math

class Planet:
    def __init__(self, initial_velocity, initial_position, radius, mass, colour, sim_speed, G) -> None:
        self.velocity = initial_velocity
        self.position = initial_position
        self.radius = radius
        self.colour = colour
        self.sim_speed = sim_speed
        self.mass = mass
        self.G =  G
        self.last_positions = []


    def update_velocity(self, bodies, sim_speed):
        for body in bodies:
            if(self != body):
                #Calculate the attraction between the two bodies
                dist_sqr = math.sqrt((self.position[0] - body.position[0])**2 + (self.position[1] - body.position[1])**2)
                dist_v = ((body.position[0] - self.position[0]) / dist_sqr, (body.position[1] - self.position[1]) / dist_sqr)
                #print(dist_sqr)

                # calculate the force according to newton f = G * m1 * m2 / r^2
                force = ((self.mass * body.mass) / (dist_sqr**2)) * self.G

                # normalize the force
                force = (force * dist_v[0], force * dist_v[1])
                
                #calculate acceleration F = m * a
                acceleration = (force[0] / self.mass, force[1] / self.mass)

                # add acceleration to the velocity
                self.velocity[0] += acceleration[0] * sim_speed
                self.velocity[1] += acceleration[1] * sim_speed
        return

    def update_position(self, sim_speed):
        self.position[0] += self.velocity[0] * sim_speed
        self.position[1] += self.velocity[1] * sim_speed

        if(sim_speed > 0):
            self.last_positions.append([self.position[0], self.position[1]])
            if(len(self.last_positions) >= 250):
                #self.last_positions.pop(0)
                i = 1
        return