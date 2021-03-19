import math

import math

class Cube:

    def __init__(self):
        self.faces = []  # 6x9 array
        self.moves = 0
        self.phi = math.pi/8  # start at pi/8
        self.theta = math.pi/8
        self.active_face = 0

    def move(self, face, direction):
        """
        This method causes a 90 degree rotation of a specific face
        of the cube (this is what we have defined as a "move")
        :param face: the face to be rotated
        :param direction: the direction in which to rotate the given face
        :return: void
        """
        pass

    def solved(self):
        """
        This method returns True if the cube is solved, False otherwise
        :return: bool is_solved
        """
        pass

    def shuffle(self):
        """
        This method shuffles the cube
        :param
        :param
        :return:
        """
        pass

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

        :param
        :param
        :return:
        """
        pass

    def set_cube(self, n):
        """

        :param
        :param
        :return:
        """
        pass