import basic3d.basicrunner, basic3d.colors, pygame, math
from basic3d.shapes import *

class BouncingCube(Cube):
    def __init__(self, size):
        super(BouncingCube, self).__init__(size)
        # The delta y of the cube
        self.dy = 1
        # The y range the cube can move in
        self.range = 5
        # Randomize the colors of the faces
        for face in self.faces:
            face.color = basic3d.colors.random_known_color()

    def update(self, dt):
        # If the cube has gone out of
        # range, invert the direction
        half_range = self.range/2
        if self.y < -half_range:
            self.dy = abs(self.dy)
        if self.y > half_range:
            self.dy = -abs(self.dy)
        # Move
        self.y += dt * self.dy
        # Rotate
        self.rotate(0, dt * math.pi/2, 0)

    def handle_event(self, event):
        # On mouse press, invert the direction
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.invert_direction()

    def invert_direction(self):
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
    middle_cube.invert_direction()

    basic3d.basicrunner.main_loop(
        300,
        300,
        'Bouncing Cubes',
        obj3Ds)
