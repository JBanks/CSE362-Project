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
        self.w = 500
        self.h = 500
        self.cube = cube

    def init(self):
        glutInitDisplayMode( GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        gluPerspective(45, (self.w / self.h), 0.1, 50.0)
        glEnable(GL_DEPTH_TEST)
        self.faces, self.phi, self.theta = self.cube.get_state()
        self.n = len(self.faces[0])


    def display(self):
        """
                This method displays the cube and has to be called in a loop so it is always displaying
                :param   :
                :param   : cube -> the cube lol
                :return: void
                """
        self.init()
        self.xrot = (self.phi * 180) / math.pi
        self.yrot = (self.theta * 180) / math.pi

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        for i in range(self.n):
            for j in range(self.n):
                    self.set_for_display(i,j)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glFlush()
        glutSwapBuffers()

        pass
    def set_for_display(self,i,j):
        glPushMatrix()
        x = j
        y = i
        z = 2
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
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        glTranslatef((-x+1) * self.cube_size - x * self.gap + self.gap*2, (-y + 1) * self.cube_size - y * self.gap, -((z - 1) * self.cube_size + z * self.gap - self.gap))
        color = RGB.rgb.get(self.faces[2][i][j])
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
        x_to_translate = (self.n-1) * self.cube_size + (self.n-1) * self.gap - self.cube_size
        z_to_translate = (-x + 1) * self.cube_size - x * self.gap + self.gap
        glTranslatef(x_to_translate, (-y + 1) * self.cube_size - y * self.gap, z_to_translate)
        color = RGB.rgb.get(self.faces[1][i][j])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glEnd()

        # top face: blue
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        x_to_translate = (self.n - 1) * self.cube_size +  - self.cube_size
        z_to_translate = (x - 1) * self.cube_size + x * self.gap - self.gap
        glTranslatef(-x_to_translate, (-y + 1) * self.cube_size - y * self.gap, z_to_translate)
        color = RGB.rgb.get(self.faces[3][i][j])
        glColor(color)
        glBegin(GL_QUADS)

        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        # # right face: yellow
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        y_to_translate = (self.n - 1) * self.cube_size - self.cube_size
        x_to_translate = (y - 1) * self.cube_size + y * self.gap
        z_to_translate = (-x + 1) * self.cube_size - x * self.gap + self.gap
        glTranslatef(x_to_translate, y_to_translate, z_to_translate)
        color = RGB.rgb.get(self.faces[4][i][j])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glEnd()

        #
        # left face: white
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        y_to_translate =  (self.n - 1) * self.cube_size - self.cube_size + self.gap*2
        x_to_translate = (-y + 1) * self.cube_size -y * self.gap + self.gap*2
        z_to_translate = (-x + 1) * self.cube_size -x * self.gap + self.gap
        glTranslatef(x_to_translate, -y_to_translate, z_to_translate)
        color = RGB.rgb.get(self.faces[5][i][j])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glEnd()

        glPopMatrix()

    def update(self, move):
        """
                This method is called after a move every time so it can update the displaying cube
                :param move: is a tuple variable, it contains the face to rotate and the direction to rotate
                :return: void
                """
        self.faces, phi, theta = self.cube.get_state()
        self.phi = phi
        self.theta = theta
        # print(self.faces)
        for i in range(6):
            self.print_func(i)

    def print_func(self,x):
        print(self.faces[x],"\n")

    def redisplay(self):
        glViewport(0, 0, self.w, self.h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, self.w/self.h,1.0,1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()