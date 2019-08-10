import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math


# set the screen measurement
width = 800
height = 600

# set the display
display = (800,600)

# <3 math for angle calulations
def angle_calculation(a,b):
    cos_a = np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))
    r = math.degrees(math.acos( min(1,max(cos_a,-1)) ))
    return r

# define vertices
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

# define colors
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

# define edges (lines)
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

# define surfaces
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()

    # set window title
    pygame.display.set_caption('test')
    # set window size and tell pygame to use opengl
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    # set perspective po
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0,0, -10)

    # glRotateF (float) (angle of rotation, x, y, z)
    # glRotatef(25, 2, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # y-axis
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for x in range(3):
#                    glTranslatef(0,1,0)
                        glTranslatef(x, -x, 0)

                elif event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
            # x-axis
                elif event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                elif event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
            # spin (on axis, this will mess up the coordinates, so beware)
            '''    elif event.key == pygame.K_SPACE:
                    glRotatef(1, 3, 1, 1)
            # stop the motion after one key press
             if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #        glTranslatef(0,0,0)
            #        glRotatef(0,0,0,0)

            # z-axis
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(0,0,1.0)
            if event.button == 5:
                glTranslatef(0,0,-1.0)
        '''
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()

main()