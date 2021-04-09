import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from constants import RGB

class Display:
    def __init__(self):
        self.gap = 0.2
        self.cube_size = 2
        self.xrot = self.yrot = 0
        # self.flag = False
        # self.k_down = False #TODO maybe remove this one...
        # self.cube = cube.Cube()
        pygame.init()
        self.w = 800
        self.h = 600
        pygame.display.set_mode((self.w, self.h), DOUBLEBUF | OPENGL)
        glutInitDisplayMode( GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

        gluPerspective(45, (self.w / self.h), 0.1, 50.0)
        # glTranslatef(-1.5, -2.0, -10)
        glEnable(GL_DEPTH_TEST)


    def display(self,faces):
        """
                This method displays the cube and has to be called in a loop so it is always displaying
                :param   :
                :param   : cube -> the cube lol
                :return: void
                """
        self.faces = faces
        # i = 0
        # n = 2
        # for colors in range(6):
        #     for r in range(n):
        #         for c in range(n):
        #             self.faces[colors, r, c] = i
        #     i += 1
        n = len(self.faces[0][1])
        n = 2


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #gluLookAt(10, 3, 0, 0, 0, 0, 0, 1, 0)
        glTranslatef(0.0, 0.0, -25.0 )

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.set_for_display(k,j,i)

        glFlush()
        glutSwapBuffers()
        pass
    def set_for_display(self,x,y,z):

        glPushMatrix()
        glRotate(self.xrot,1,0,0)
        glRotate(self.yrot,0,1,0)

        glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, (-z + 1) * self.cube_size - z * self.gap)
        # front face : red
        # glColor(1,0,0)
        color = self.faces[0][y][x]
        color = RGB.rgb.get(color)
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size/2,self.cube_size/2,self.cube_size/2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glEnd()

        # bottom face: green
        color = self.faces[1][y][x]
        color = RGB.rgb.get(color)
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glEnd()

        # back face : orange
        color = self.faces[2][y][x]
        color = RGB.rgb.get(color)
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        # top face: blue
        color = self.faces[3][y][x]
        color = RGB.rgb.get(color)
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glEnd()

        # right face: yellow
        color = self.faces[4][y][x]
        color = RGB.rgb.get(color)
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        # left face: white
        color = self.faces[5][y][x]
        color = RGB.rgb.get(color)
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()


        glPopMatrix()
        pass
    def rotate(self,rot,angle):
        if angle == 'x':
            self.angle = ((1,0,0))
            self.yrot += rot
        else :
            self.angle = ((0, 1, 0))
            self.xrot += rot
        print(self.angle)
    # def special_keys(self,key,x,y):
    #     if key == GLUT_KEY_DOWN:
    #         self.xrot += 5
    #     elif key == GLUT_KEY_RIGHT:
    #         self.yrot += 5
    #     glutPostRedisplay()
    # def keys(self, key, x,y):
    #     if key == 27:
    #         print("baby break a sweat, dont get tired yet")
    #         pygame.quit()
    #         quit()

    def update_move(self, move):
        """
                This method is called after a move every time so it can update the displaying cube
                :param move: is a tuple variable, it contains the face to rotate and the direction to rotate
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
        print("ok")

# disp = Display()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#         keypress = pygame.key.get_pressed()
#         if keypress[pygame.K_DOWN]:
#             disp.rotate(5,'y')
#
#         if keypress[pygame.K_RIGHT]:
#             disp.rotate(5, 'x')
#
#         glMatrixMode(GL_MODELVIEW)
#         # glLoadIdentity()
#         glutReshapeFunc(disp.redisplay())
#         glutDialsFunc(disp.display())
#         # glutKeyboardFunc(disp.keys)
#         # glutSpecialFunc(disp.special_keys)
#         pygame.display.flip()
#         pygame.time.wait(500)
# displaysmt = Display()
# displaysmt.display()
