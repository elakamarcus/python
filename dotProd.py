#!/bin/python3
import math

# simple vector in a 2d space, x-axis and y-axis
class vector2d:
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y
        print(f'created vector: ({self.x}, {self.y})')

def dotProduct(a, b):
    # simple formula: a.b = a.x * b.x + a.y * b.y
    x = a.x * b.x
    y = a.y * b.y
    return x+y

def dotProductDegree(a, b):
    # a tad more complicated but also more useful a.b = |a| x |b| x cos(0)
    # we can also see that ...  (a.b)/(cos(0) x |a|) = |b| and that (a.b)/(cos(0) x |b|) = |a|
    return vectorLength(a) * vectorLength(b) * math.cos(angleBetweenVectors(a,b))

def vectorLength(a):
    # (a.x^2 + a.y^2)^(1/2)
    return math.sqrt(a.x**2+a.y**2)

def angleBetweenVectors(a, b):
    # cos(0) = a.b  / (|a| x |b|)
    angle = math.acos((dotProduct(a,b))/(vectorLength(a)*vectorLength(b)))
    return angle

def main():
    a = vector2d(-2, 3)
    b = vector2d(3, 4)
    #print(f'vector 1: {a.printVector()}, vector2: {b.printVector()}')
    print(f'First dot product: {dotProduct(a, b)}')
    print(f'Angle between v1 v2: {math.degrees(angleBetweenVectors(a,b)):.2f} degrees')
    print(f'Second dot product: {dotProductDegree(a, b):.2f}')

if __name__ == "__main__":
    main()