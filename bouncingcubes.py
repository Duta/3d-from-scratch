import basic3d.basicrunner, pygame, math
from basic3d.shapes import *

class BouncingCube(Cube):
    def __init__(self, size):
        super(BouncingCube, self).__init__(size)
        self.dy = 1
        self.range = 5

    def update(self, dt):
        half_range = self.range/2
        if self.y < -half_range or self.y > half_range:
            self.invert_bounce()
        self.y += dt * self.dy
        self.rotate(0, dt * math.pi/2, 0)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.invert_bounce()

    def invert_bounce(self):
        self.dy *= -1

if __name__ == '__main__':
    # Create a few cubes
    left_cube   = BouncingCube(2)
    middle_cube = BouncingCube(4)
    right_cube  = BouncingCube(3)
    obj3Ds = [middle_cube, left_cube, right_cube]

    # Position them
    offset = 4.5
    left_cube.x  -= offset
    right_cube.x += offset

    # Make some bounce in different directions
    middle_cube.invert_bounce()

    basic3d.basicrunner.main_loop(
        300,
        300,
        'Bouncing Cubes',
        obj3Ds)
