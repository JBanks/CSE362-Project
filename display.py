import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import cube

class Display:
    def __init__(self):
        self.xrot = self.yrot = 0
        self.flag = False
        self.k_down = False #TODO maybe remove this one...
        self.cube = cube.Cube()
        pygame.init()
        self.w = 800
        self.h = 600
        pygame.display.set_mode((self.w, self.h), DOUBLEBUF | OPENGL)
        glutInitDisplayMode( GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

        gluPerspective(45, (self.w / self.h), 0.1, 50.0)
        # glTranslatef(-1.5, -2.0, -10)
        glEnable(GL_DEPTH_TEST)


    def display(self):
        """
                This method displays the cube and has to be called in a loop so it is always displaying
                :param   :
                :param   :
                :return: void
                """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #gluLookAt(10, 3, 0, 0, 0, 0, 0, 1, 0)
        glTranslatef(0.0, 0.0, -25.0 )
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    self.cube.set_cube(i,j,k)
                    # pygame.display.flip()
        # self.cube.set_cube(1,1,1)
        glFlush()
        glutSwapBuffers()

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
    def redisplay(self):
        glViewport(0, 0, self.w, self.h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, self.w/self.h,1.0,1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

disp = Display()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glutReshapeFunc(disp.redisplay())
        glutDialsFunc(disp.display())
        pygame.display.flip()

        print("ok")
        pygame.time.wait(500)
