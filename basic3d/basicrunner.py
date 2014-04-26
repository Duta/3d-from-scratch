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

    def render(obj3Ds):
        # Clear the screen
        screen.fill(colors.white)

        # The co-ordinates of the center of the screen
        cx, cy = w/2, h/2
        # Render each object in the scene
        for obj3D in obj3Ds:
            # The object's location
            ox, oy, oz = obj3D.x, obj3D.y, obj3D.z
            # Render each face of the object
            for face in obj3D.faces:
                # The face's vertices
                vertices = face.vertices
                # The scale factor
                sf = min(cx, cy)
                # Convert the vertices' locations
                # to 2d screen co-ordinates
                xys = []
                for vertex in vertices:
                    # The vertex's location
                    vx = vertex.x + ox
                    vy = vertex.y + oy
                    vz = vertex.z + oz
                    # Project to 2d
                    x = cx + sf*vx/vz
                    y = cy + sf*vy/vz
                    xys.append([x, y])
                # Draw the face to the screen
                pygame.draw.polygon(screen, face.color, xys, 1)

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
