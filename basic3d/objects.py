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
        x = self.x
        y = self.y*cos(theta) - self.z*sin(theta)
        z = self.y*sin(theta) + self.z*cos(theta)
        self.x, self.y, self.z = x, y, z

    def rotateY(self, theta):
        x = self.x*cos(theta) + self.z*sin(theta)
        y = self.y
        z = -self.x*sin(theta) + self.z*cos(theta)
        self.x, self.y, self.z = x, y, z

    def rotateZ(self, theta):
        x = self.x*cos(theta) - self.y*sin(theta)
        y = self.x*sin(theta) + self.y*cos(theta)
        z = self.z
        self.x, self.y, self.z = x, y, z

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
