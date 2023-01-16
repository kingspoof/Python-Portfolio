# The ball class will simulate a ball, which is going to jump up and down

class Ball:
    def __init__(self, mass, initial_height) -> None:
        self.mass = mass
        self.height = initial_height
        self.velocity = 0
        self.g = -9.81
        self.heights = []

    # timestep, is the time passed in seconds, between the last frame called and now
    def update(self, timestep):
        # update the velocity of our ball
        self.velocity += self.g * timestep

        # update the position, if we hit the ground in the next step, we will flip the ball 
        if (self.height + (self.velocity * timestep) <= 0): 
            self.velocity *= -1

        self.height += self.velocity * timestep
        self.heights.append(self.height)