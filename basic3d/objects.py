class Vec3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Face(object):
    def __init__(self, vertices):
        self.vertices = vertices

class Obj3D(object):
    def __init__(self, faces, x=0, y=0, z=8):
        self.faces = faces
        self.x = x
        self.y = y
        self.z = z

    def update(self):
        pass

    def handle_event(self, event):
        pass
