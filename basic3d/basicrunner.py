import sys, pygame, basic3d.colors as colors

def main_loop(w, h, title, obj3Ds, fps=60):
    # The window dimensions
    size = w, h
    # The timer (manages framerate)
    clock = pygame.time.Clock()
    # Time delta between frames
    dt = 0
    # Get a handle on the window
    screen = pygame.display.set_mode(size)
    # Set the window's title
    pygame.display.set_caption(title)

    # Render function
    def render(obj3Ds):
        screen.fill(colors.white)

        cx, cy = w/2, h/2
        for obj3D in obj3Ds:
            ox, oy, oz = obj3D.x, obj3D.y, obj3D.z
            for face in obj3D.faces:
                vertices = face.vertices
                xys = []
                sf = min(cx, cy)
                for vertex in vertices:
                    vx = vertex.x + ox
                    vy = vertex.y + oy
                    vz = vertex.z + oz
                    x = cx + sf*vx/vz
                    y = cy + sf*vy/vz
                    xys.append([x, y])
                pygame.draw.polygon(screen, colors.black, xys, 1)

    # Main loop
    while 1:
        # Check events
        for event in pygame.event.get():
            # Exit on close button press
            if event.type == pygame.QUIT:
                sys.exit()
            # Let the objects handle the events
            for obj3D in obj3Ds:
                obj3D.handle_event(event)

        # Update
        for obj3D in obj3Ds:
            obj3D.update(dt)

        # Redraw
        render(obj3Ds)

        # Flip the buffers
        pygame.display.flip()

        # Run at the given framerate
        dt = clock.tick(fps)/1000.0
