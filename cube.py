import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy
from constants import *

class Cube:

    def __init__(self):
        self.faces = numpy.zeros([6, 3, 3], dtype=int)
        self.moves = 0
        self.phi = math.pi/8  # start at pi/8
        self.theta = math.pi/8
        self.active_face = 0
        self.cube_size = 2
        self.n = 2 #pocket cube TODO change the initialization of n so the user choses
        self.gap = 0.2

    def move(self, face, direction):
        """
        This method causes a 90 degree rotation of a specific face
        of the cube (this is what we have defined as a "move")
        :param face: the face to be rotated
        :param direction: the direction in which to rotate the given face
        :return: void
        """

        # top: arr[x,0,:]
        # bottom: arr[x,2,:]
        # right side: arr[x,:,2]
        # left side: arr[x,:,0]

        # for CCW rotations, need to flip whenever moving the bottom
        # of one 3x3 array to the right side of another, or when moving
        # the top of one to the left side of another

        if direction == Direction.CCW:
            # CCW 90 degree rotation

            if face == Faces.RED:
                # red face

                self.faces[0, :, :] = numpy.rot90(self.faces[0, :, :])
                temp1 = self.faces[1, :, 0]
                temp2 = numpy.flip(self.faces[4, 2, :])
                self.faces[4, 2, :] = temp1
                temp1 = self.faces[3, :, 2]
                self.faces[3, :, 2] = temp2
                temp2 = numpy.flip(self.faces[5, 0, :])
                self.faces[5, 0, :] = temp1
                self.faces[1, : 0] = temp2

            elif face == Faces.GREEN:
                # green face

                self.faces[1, :, :] = numpy.rot90(self.faces[1, :, :])
                temp1 = self.faces[2, :, 0]
                temp2 = numpy.flip(self.faces[4, 2, :])
                self.faces[4, 2, :] = temp1
                temp1 = self.faces[0, :, 2]
                self.faces[0, :, 2] = temp2
                temp2 = numpy.flip(self.faces[5, 0, :])
                self.faces[5, 0, :] = temp1
                self.faces[2, : 0] = temp2

            elif face == Faces.ORANGE:
                # orange face

                self.faces[2, :, :] = numpy.rot90(self.faces[2, :, :])
                temp1 = self.faces[3, :, 0]
                temp2 = numpy.flip(self.faces[4, 2, :])
                self.faces[4, 2, :] = temp1
                temp1 = self.faces[1, :, 2]
                self.faces[1, :, 2] = temp2
                temp2 = numpy.flip(self.faces[5, 0, :])
                self.faces[5, 0, :] = temp1
                self.faces[3, : 0] = temp2

            elif face == Faces.BLUE:
                # blue face

                self.faces[3, :, :] = numpy.rot90(self.faces[3, :, :])
                temp1 = self.faces[0, :, 0]
                temp2 = numpy.flip(self.faces[4, 2, :])
                self.faces[4, 2, :] = temp1
                temp1 = self.faces[2, :, 2]
                self.faces[2, :, 2] = temp2
                temp2 = numpy.flip(self.faces[5, 0, :])
                self.faces[5, 0, :] = temp1
                self.faces[0, : 0] = temp2

            elif face == Faces.YELLOW:
                # yellow face

                self.faces[4, :, :] = numpy.rot90(self.faces[4, :, :])
                temp1 = self.faces[2, :, 0]
                temp2 = numpy.flip(self.faces[3, 2, :])
                self.faces[3, 2, :] = temp1
                temp1 = self.faces[0, :, 2]
                self.faces[0, :, 2] = temp2
                temp2 = numpy.flip(self.faces[1, 0, :])
                self.faces[1, 0, :] = temp1
                self.faces[2, : 0] = temp2

            elif face == Faces.WHITE:
                # white face

                self.faces[5, :, :] = numpy.rot90(self.faces[5, :, :])
                temp1 = self.faces[2, :, 0]
                temp2 = numpy.flip(self.faces[1, 2, :])
                self.faces[1, 2, :] = temp1
                temp1 = self.faces[0, :, 2]
                self.faces[0, :, 2] = temp2
                temp2 = numpy.flip(self.faces[3, 0, :])
                self.faces[3, 0, :] = temp1
                self.faces[2, : 0] = temp2

        # for CW rotations, need to flip whenever moving the left side
        # of one 3x3 array to the top of another, or when moving
        # the right side of one to the bottom of another

        elif direction == Direction.CW:
            # CW 90 degree rotation

            # top: arr[x,0,:]
            # bottom: arr[x,2,:]
            # right side: arr[x,:,2]
            # left side: arr[x,:,0]

            if face == Faces.RED:
                self.faces[0, :, :] = numpy.rot90(self.faces[0, :, :], 3)
                temp1 = numpy.flip(self.faces[3, :, 2])
                temp2 = self.faces[4, 2, :]
                self.faces[4, 2, :] = temp1
                temp1 = numpy.flip(self.faces[1, :, 0])
                self.faces[1, :, 0] = temp2
                temp2 = self.faces[5, 0, :]
                self.faces[5, 0, :] = temp1
                self.faces[3, : 2] = temp2

            elif face == Faces.GREEN:
                self.faces[1, :, :] = numpy.rot90(self.faces[1, :, :], 3)
                temp1 = numpy.flip(self.faces[0, :, 2])
                temp2 = self.faces[4, 2, :]
                self.faces[4, 2, :] = temp1
                temp1 = numpy.flip(self.faces[2, :, 0])
                self.faces[2, :, 0] = temp2
                temp2 = self.faces[5, 0, :]
                self.faces[5, 0, :] = temp1
                self.faces[0, : 2] = temp2

            elif face == Faces.ORANGE:
                self.faces[2, :, :] = numpy.rot90(self.faces[2, :, :], 3)
                temp1 = numpy.flip(self.faces[1, :, 2])
                temp2 = self.faces[4, 2, :]
                self.faces[4, 2, :] = temp1
                temp1 = numpy.flip(self.faces[3, :, 0])
                self.faces[3, :, 0] = temp2
                temp2 = self.faces[5, 0, :]
                self.faces[5, 0, :] = temp1
                self.faces[1, : 2] = temp2

            elif face == Faces.BLUE:
                self.faces[3, :, :] = numpy.rot90(self.faces[3, :, :], 3)
                temp1 = numpy.flip(self.faces[2, :, 2])
                temp2 = self.faces[4, 2, :]
                self.faces[4, 2, :] = temp1
                temp1 = numpy.flip(self.faces[0, :, 0])
                self.faces[0, :, 0] = temp2
                temp2 = self.faces[5, 0, :]
                self.faces[5, 0, :] = temp1
                self.faces[2, : 2] = temp2

            elif face == Faces.YELLOW:
                self.faces[4, :, :] = numpy.rot90(self.faces[4, :, :], 3)
                temp1 = numpy.flip(self.faces[0, :, 2])
                temp2 = self.faces[3, 2, :]
                self.faces[3, 2, :] = temp1
                temp1 = numpy.flip(self.faces[2, :, 0])
                self.faces[2, :, 0] = temp2
                temp2 = self.faces[1, 0, :]
                self.faces[1, 0, :] = temp1
                self.faces[0, : 2] = temp2

            elif face == Faces.WHITE:
                self.faces[5, :, :] = numpy.rot90(self.faces[5, :, :], 3)
                temp1 = numpy.flip(self.faces[0, :, 2])
                temp2 = self.faces[1, 2, :]
                self.faces[1, 2, :] = temp1
                temp1 = numpy.flip(self.faces[2, :, 0])
                self.faces[2, :, 0] = temp2
                temp2 = self.faces[3, 0, :]
                self.faces[3, 0, :] = temp1
                self.faces[0, : 2] = temp2

    def solved(self):
        """
        This method returns True if the cube is solved, False otherwise
        :return: bool is_solved
        """
        pass

    def shuffle(self):
        """
        This method shuffles the cube by performing 20 random moves
        :param
        :param
        :return: void
        """
        for i in range(20):
            face_index = random.randint(0, 5)
            direction_index = random.randint(0, 1)
            self.move(face_index, direction_index)

    def update_angle(self, delta_angle, axis):
        """

        :param
        :param
        :return:
        """
        pass

    def notify(self):
        """

        :param
        :param
        :return:
        """
        pass

    def get_state(self):
        """

        :param
        :param
        :return:
        """
        pass

    def undo(self):
        """
        This method returns the cube to the state it was in prior to
        the last move
        :param
        :param
        :return: void
        """
        pass

    def set_cube(self,x,y,z):
        """
        this method is going to set the cube to be displayed
        :return: void
        """
        glPushMatrix()
        glTranslatef((x - 1) * self.cube_size + x * self.gap, (y - 1) * self.cube_size + y * self.gap, (z - 1) * self.cube_size + z * self.gap)
        # front face : red
        glColor(1,0,0)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size/2,self.cube_size/2,self.cube_size/2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glEnd()
        # back face : orange
        glColor3f(1, 176.0 / 255.0, 5.0 / 255.0)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        # top face: blue
        glColor3f(0, 0, 1)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glEnd()

        # bottom face: green
        glColor3f(0, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glEnd()

        # left face: white
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        # right face: yellow
        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        glPopMatrix()




