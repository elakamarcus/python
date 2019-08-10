import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# set the screen measurement
width = 800
height = 600

# set the display
display = (800,600)

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
    gluPerspective(30, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0,0, -10)

    # glRotateF (float) (angle of rotation, x, y, z)
    glRotatef(25, 2, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # y-axis
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                elif event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
            # x-axis
                elif event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                elif event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
            # spin (on axis, this will mess up the coordinates, so beware)
                elif event.key == pygame.K_SPACE:
                    glRotatef(1, 3, 1, 1)
            # stop the motion after one key press
            ''' if event.type == pygame.KEYUP:
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