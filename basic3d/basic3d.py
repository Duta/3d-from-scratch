import sys, pygame

class Vec3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Face(object):
    def __init__(self, vertices):
        self.vertices = vertices

def render():
    pass

def main_loop(w, h, title, update_func, event_handler, fps=60):
    # The window dimensions
    size = w, h
    # The timer (manages framerate)
    clock = pygame.time.Clock()
    # Get a handle on the window
    screen = pygame.display.set_mode(size)
    # Set the window's title
    pygame.display.set_caption(title)

    # Main loop
    while 1:
        # Check events
        for event in pygame.event.get():
            # Exit on close button press
            if event.type == pygame.QUIT:
                sys.exit()
            # Delegate to the event handler
            event_handler(event)

        # Update
        update_func()

        # Redraw
        render()

        # Flip the buffers
        pygame.display.flip()

        # Run at the given framerate
        clock.tick(fps)

# Example
if __name__ == '__main__':
    def update():               pass
    def event_handler(event):   pass
    main_loop(600, 400, 'Basic 3D', update, event_handler)
