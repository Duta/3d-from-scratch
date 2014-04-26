import basic3d.colors as colors
from math import sin, cos

#############################
# All angles are in radians #
#############################

class Vec3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def rotateX(self, theta):
        x, y, z = self.x, self.y, self.z
        self.x = x
        self.y = y*cos(theta) - z*sin(theta)
        self.z = y*sin(theta) + z*cos(theta)

    def rotateY(self, theta):
        x, y, z = self.x, self.y, self.z
        self.x = x*cos(theta) + z*sin(theta)
        self.y = y
        self.z = z*cos(theta) - x*sin(theta)

    def rotateZ(self, theta):
        x, y, z = self.x, self.y, self.z
        self.x = x*cos(theta) - y*sin(theta)
        self.y = x*sin(theta) + y*cos(theta)
        self.z = z

class Face(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.color = colors.black

class Obj3D(object):
    def __init__(self, faces, x=0, y=0, z=8):
        self.faces = faces
        self.x = x
        self.y = y
        self.z = z

    def update(self, dt):
        pass

    def handle_event(self, event):
        pass

    def rotate(self, xTheta, yTheta, zTheta):
        for face in self.faces:
            for vertex in face.vertices:
                vertex.rotateZ(zTheta)
                vertex.rotateY(yTheta)
                vertex.rotateX(xTheta)
