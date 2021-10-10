from tkinter import *

SIZE = 600

import math

def distance(p1, p2):
    """calculates the distance between two points in a plane"""
    d = float(math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2))
    return d


def triangle_area(p1, p2, p3):
    """uses Herons formula to calculate the area of a triangle given the coordinates of three points."""
    a = distance(p1, p2)
    b = distance(p1, p3)
    c = distance(p2, p3)
    s = (1 / 2) * (a + b + c)
    area = float(math.sqrt(s * (s - a) * (s - b) * (s - c)))

    return area


top = (200, 50)
botleft = (50, 200)
botright = (400, 200)


def triangle(top, botleft, botright, img):
    """Draws a triangle."""
    for y in range(top[1], botright[1]):
        for x in range(botleft[0], botright[0]):
           
            a = distance(top, botright)
            b = distance(top, botleft)
            c = distance(botleft, botright)
            s = (1 / 2) * (a + b + c)
            
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            

            if triangle_area((x, y), top, botleft) + triangle_area((x, y), botleft, botright) + triangle_area((x, y),
                                                                                                              botright,
                                                                                                              top) < area + 0.00001:
                img.put("#ffffff", (x, y))


def cross(a, b):
    c = [a[0] * b[1] - a[1] * b[0]]

    return c


def main():
    """Create your image and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    triangle(top, botleft, botright, img)
    mainloop()


if __name__ == '__main__':
    main()




