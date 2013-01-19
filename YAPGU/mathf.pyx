"""
Mathematics utility functions and classes:
I have no idea why I named it "mathf".
"""
from __future__ import division

#Oh so fast.
cdef extern from "math.h":
    float cosf(float theta)
    float sinf(float theta)
    float atan2f(float x, float y)
    float sqrtf(float x)

cdef float pi = 3.14159265
cdef float pi_180 = pi/180.0 #

cdef float radians(float deg):
    return deg*pi_180


cdef class Vector2D:
    '''
    Two-dimensional vector class.
    '''
    cdef public float x, y
    def __init__(Vector2D self, float x, float y):
        self.x,self.y = x,y
    def __add__(Vector2D self, Vector2D rhs):
        return Vector2D(self.x + rhs.x, self.y + rhs.y)
    def __sub__(Vector2D self, Vector2D rhs):
        return Vector2D(self.x - rhs.x, self.y - rhs.y)
    def __mul__(Vector2D self, float rhs):
        return Vector2D(self.x * rhs, self.y * rhs)
    def __div__(Vector2D self, float rhs):
        return Vector2D(self.x / rhs, self.y / rhs)
    def __iadd__(Vector2D self, Vector2D rhs):
        self.x += rhs.x
        self.y += rhs.y
        return self
    def __isub__(Vector2D self, Vector2D rhs):
        self.x -= rhs.x
        self.y -= rhs.y
        return self
    def __imul__(Vector2D self, float rhs):
        self.x *= rhs
        self.y *= rhs
        return self
    def __idiv__(Vector2D self, float rhs):
        self.x /= rhs
        self.y /= rhs
        return self
    def __richcmp__(self, other, int c): #TODO: Hmm, lesser and greater operators?
        if not isinstance(other, Vector2D):
            return False
        if c == 2:
            return self.x == (<Vector2D>other).x and self.y == (<Vector2D>other).y
        elif c == 3:
            return self.x != (<Vector2D>other).x or self.y != (<Vector2D>other).y

    def __neg__ (Vector2D self):
        return Vector2D(-self.x,-self.y)
    def __str__(Vector2D self):
        return "(" + str(self.x) + "," + str(self.y) +  ")"
    
cpdef float Length(Vector2D vec):
    return sqrtf(vec.x**2 + vec.y**2)

cpdef Vector2D Normalized(Vector2D vec):
    if vec.x == 0 and vec.y == 0:
        return Vector2D(0.0,0.0)
    return vec / Length(vec)

cpdef float Distance(Vector2D vec1, Vector2D vec2 ):
    return sqrtf((vec1.x-vec2.x)**2 + (vec1.y-vec2.y)**2)

cpdef float Dot(Vector2D a, Vector2D b):
    return (a.x*b.x + a.y*b.y)

cpdef float LookAt(Vector2D a, Vector2D b):
    """ Returns rotation in degrees.
    a is object, that b wants see."""
    return atan2f((a.x - b.x), (a.y - b.y)) * 180.0/pi

cpdef Vector2D SetLength(Vector2D v, float l):
    return Normalized(v) * l

cpdef MoveLocal(Vector2D vec, float rot, float dist):
    cdef float angle_radians = -radians(rot)
    vec.x +=  -sinf(angle_radians) * dist
    vec.y +=  cosf(angle_radians) * dist

