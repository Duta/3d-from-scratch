from basic3d.objects import *

class Cuboid(Obj3D):
    def __init__(self, w, h, d):
        half_w, half_h, half_d = w/2, h/2, d/2
        vertices = [
            Vec3( half_w, -half_h, -half_d),
            Vec3( half_w, -half_h,  half_d),
            Vec3(-half_w, -half_h,  half_d),
            Vec3(-half_w, -half_h, -half_d),
            Vec3( half_w,  half_h, -half_d),
            Vec3( half_w,  half_h,  half_d),
            Vec3(-half_w,  half_h,  half_d),
            Vec3(-half_w,  half_h, -half_d)
        ]
        faces = [
            Face([vertices[0], vertices[1], vertices[2], vertices[3]]),
            Face([vertices[4], vertices[7], vertices[6], vertices[5]]),
            Face([vertices[0], vertices[4], vertices[5], vertices[1]]),
            Face([vertices[1], vertices[5], vertices[6], vertices[2]]),
            Face([vertices[2], vertices[6], vertices[7], vertices[3]]),
            Face([vertices[4], vertices[0], vertices[3], vertices[7]])
        ]
        super(Cuboid, self).__init__(faces)
        self.w = w
        self.h = h
        self.d = d

class Cube(Cuboid):
    def __init__(self, size):
        super(Cube, self).__init__(size, size, size)
