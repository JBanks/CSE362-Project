import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *
import cube

class Display:
    def __init__(self):
        self.xrot = self.yrot = 0
        self.flag = False
        self.k_down = False #TODO maybe remove this one...
        self.cube = cube.Cube()
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

        # glTranslatef(-1.5, -2.0, -10)
        glEnable(GL_DEPTH_TEST)


    def display(self):
        """
                This method displays the cube and has to be called in a loop so it is always displaying
                :param   :
                :param   :
                :return: void
                """
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        print("yo")
        # glLoadIdentity()
        #gluLookAt(10, 3, 0, 0, 0, 0, 0, 1, 0)
        glTranslatef(0.0, 0.0, -25.0 )
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    self.cube.set_cube(i,j,k)
        glFlush()

    def update_move(self, move):
        """
                This method is called after a move every time so it can update the displaying cube
                :param move: 90 degree rotation of a specific face
                of the cube. Brings you into a new display.
                :return: void
                """
        pass

    def update_hints(self,hints):
        """
                This method update the possible hints to a solution
                :param hints: a list of moves that can be made from a particular state
                :return: void
                """
        pass

disp = Display()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        disp.display()

        pygame.time.wait(5000)
        pygame.display.flip()