import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from constants import RGB



class Display:
    def __init__(self,cube):
        self.gap = 0.09
        self.cube_size = 2
        self.xrot = self.yrot = 0
        # pygame.init()
        self.w = 500
        self.h = 500
        self.cube = cube

    def init(self):
        # pygame.init()
        # pygame.display.set_mode((self.w, self.h), DOUBLEBUF | OPENGL)
        glutInitDisplayMode( GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        gluPerspective(45, (self.w / self.h), 0.1, 50.0)
        # glTranslatef(-1.5, -2.0, -10)
        glEnable(GL_DEPTH_TEST)

    def display(self):
        """
                This method displays the cube and has to be called in a loop so it is always displaying
                :param   :
                :param   : cube -> the cube lol
                :return: void
                """
        self.init()

        self.faces = self.cube.get_state()
        self.n = len(self.faces[0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        #gluLookAt(10, 3, 0, 0, 0, 0, 0, 1, 0)
        # glTranslatef(0.0, 0.0, -25.0 )
        for i in range(self.n):
            for j in range(self.n):
                # for k in range(n):
                    self.set_for_display(i,j)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glFlush()
        glutSwapBuffers()

        pass
    def set_for_display(self,i,j):
        #TODO rotations aren't good
        glPushMatrix()

        x = j
        y = i
        z = 2
        # glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, (z - 1) * self.cube_size + z * self.gap)/////self.n-1+self.gap
        (-x + 1) * self.cube_size - x * self.gap + self.gap
        # front face : red
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot,1,0,0)
        glRotate(self.yrot,0,1,0)
        glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, (z - 1) * self.cube_size + z * self.gap - self.gap)
        color = RGB.rgb.get(self.faces[0][i][j])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size/2,self.cube_size/2,self.cube_size/2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)

        glEnd()

        # # back face : orange
        # glLoadIdentity()
        # glTranslatef(0, 0, -25.0)
        # glRotate(self.xrot,1,0,0)
        # glRotate(self.yrot,0,1,0)
        # glTranslatef((-x + 1) * self.cube_size - x * self.gap, (-y + 1) * self.cube_size - y * self.gap, z *self.n-1 )
        # # glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, -z)
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, -((z - 1) * self.cube_size + z * self.gap - self.gap))
        # glTranslatef(0,0,-(self.n-1+self.gap*2) * 2) #x2 because i have to bring it to the center from the previous translate and then the same size
        color = RGB.rgb.get(self.faces[2][i][-j + self.n-1])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        # bottom face: green
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        #n-1 = has to start here the front/back face ends * la grandeur du cube
        #(self.n-1) * self.gap il faut ajuster le gap
        #enlever la taille du cube pour une raison mathematique que j'ignore.....
        x_to_translate = (self.n-1) * self.cube_size + (self.n-1) * self.gap - self.cube_size
        z_to_translate = (-x + 1) * self.cube_size - x * self.gap + self.gap
        glTranslatef( x_to_translate,(-y + 1) * self.cube_size - y * self.gap, z_to_translate)
        color = RGB.rgb.get(self.faces[1][i][j])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glEnd()

        # glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)

        #
        # top face: blue
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        x_to_translate = (self.n - 1) * self.cube_size +  - self.cube_size
        glTranslatef(-x_to_translate, (-y + 1) * self.cube_size - y * self.gap, z_to_translate)
        color = RGB.rgb.get(self.faces[3][i][-j + self.n-1])
        glColor(color)
        glBegin(GL_QUADS)

        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)


        # glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glEnd()
        #
        # # right face: yellow
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        y_to_translate = (self.n - 1) * self.cube_size - self.cube_size
        x_to_translate = (x - 1) * self.cube_size + x * self.gap - self.gap * 2
        z_to_translate = (y - 1) * self.cube_size + y * self.gap - self.gap

        glTranslatef(-x_to_translate, y_to_translate, -z_to_translate)
        color = RGB.rgb.get(self.faces[4][j][i])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)



        # glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glEnd()
        #

        #
        # left face: white
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        # glTranslatef((-x + 1) * self.cube_size - x * self.gap, (y - 1) * self.cube_size + y * self.gap, 0)
        # glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, (z - 1) * self.cube_size + z * self.gap)
        y_to_translate =  (self.n - 1) * self.cube_size - self.cube_size + self.gap*2
        glTranslatef(-x_to_translate, -y_to_translate, -z_to_translate)
        color = RGB.rgb.get(self.faces[5][-j + self.n-1][i])
        glColor(color)
        glBegin(GL_QUADS)

        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)

        # glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        glPopMatrix()

    def rotate(self,rot,angle):
        if angle == 'x':
            self.yrot += rot
        else :
            self.xrot += rot

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

    def update(self, move):
        """
                This method is called after a move every time so it can update the displaying cube
                :param move: is a tuple variable, it contains the face to rotate and the direction to rotate
                :return: void
                """
        self.faces = self.cube.get_state()


    def redisplay(self):
        glViewport(0, 0, self.w, self.h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, self.w/self.h,1.0,1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()