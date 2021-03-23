import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *


class Display:
    def __init__(self):
        self.xrot = self.yrot = 0
        self.flag = False
        self.k_down = False #TODO maybe remove this one...

    def display(self):
        """
                This method displays the cube and has to be called in a loop so it is always displaying
                :param   :
                :param   :
                :return: void
                """
        pass

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