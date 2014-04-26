import basic3d.basicrunner, pygame
from basic3d.shapes import *

if __name__ == '__main__':
    class BouncingCube(Cube):
        def __init__(self, size):
            super(BouncingCube, self).__init__(size)
            self.dy = 0.1
            self.range = 5

        def update(self):
            half_range = self.range/2
            if self.y < -half_range or self.y > half_range:
                self.invert_bounce()
            self.y += self.dy

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.invert_bounce()

        def invert_bounce(self):
            self.dy *= -1

    # Create a few cubes
    left_small_cube   = BouncingCube(2)
    center_big_cube   = BouncingCube(4)
    right_medium_cube = BouncingCube(3)
    obj3Ds = [center_big_cube, left_small_cube, right_medium_cube]

    # Position them
    offset = 4.5
    left_small_cube.x   -= offset
    right_medium_cube.x += offset

    # Make some bounce in different directions
    center_big_cube.invert_bounce()

    basic3d.basicrunner.main_loop(
        300,
        300,
        'Bouncing Cubes',
        obj3Ds)
