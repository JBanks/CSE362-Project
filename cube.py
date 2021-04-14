from display import Display
import random
import math
import numpy
from constants import *
from display import Display


class Cube:
    def __init__(self):
        self.moves = 0
        self.time = 0
        self.phi = math.pi / 8  # horizontal rotation
        self.theta = math.pi / 8  # vertical rotation
        self.active_face = 0
        self.cube_size = 2
        self.n = 2  # pocket cube TODO change the initialization of n so the user choses
        self.gap = 0.2
        self.observers = []  # A list for the observer pattern

        # self.display = Display()
        self.set_cube(3)  # TODO just for test

    def add_observer(self, observer):
        """
        This adds an observer to the list of observers who will be notified when changes occur
        :param observer: must be an object that accepts calls to "update" with a "move" parameter
        :return: void
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        This removes an observer so that they will no longer be notified when changes occur
        :param observer: must be an object that is already in the observers list
        :return: void
        """
        self.observers.remove(observer)

    def notify(self, move):
        """
        This function is called to notify any listeners that the list of moves has been updated.
        :return: void
        """
        for observer in self.observers:
            observer.update(move)

    def print_faces(self):
        print(self.faces)

    def solved(self):
        """
        This method returns True if the cube is solved, False otherwise
        :return: bool is_solved
        """
        for side in range(6):  # repeat for each face
            compare = self.faces[side, 0, 0]  # compare all squares to top left
            for i in range(3):
                for j in range(3):
                    if self.faces[side, i, j] != compare:  # if any not the same, return false
                        return False

        return True

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
        This method will update the angle of the cube to be displayed
        when it is rotated
        :param delta_angle: amount by which to rotate the cube in degrees
        :param axis: 0 (horizontal) or 1 (vertical)
        :return: void
        """
        if axis == 0:
            self.phi += delta_angle
        else:
            self.theta += delta_angle

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

    def set_cube(self, n):
        """
        this method is going to set the cube to be displayed
        :param n = the dimension chosen.
        :return: void
        """
        self.faces = numpy.zeros([6, n, n], dtype=int)
        i = 0
        for colors in range(6):
            for r in range(n):
                for c in range(n):
                    self.faces[colors, r, c] = i
            i += 1
        # self.display.update_move(self.faces)
        # self.display.display(self.faces)

    def move(self, face, direction, faces=None):
        """
        This method causes a 90 degree rotation of a specific face
        of the cube (this is what we have defined as a "move")
        :param face: the face to be rotated
        :param direction: the direction in which to rotate the given face
        :param faces: The current node
        :return: The faces array reflecting the changes requested
        """
        simulation = True
        if faces is None:
            simulation = False
            faces = self.faces

        # top: arr[x,0,:]
        # bottom: arr[x,2,:]
        # right side: arr[x,:,2]
        # left side: arr[x,:,0]
        # for CCW rotations, need to flip whenever moving the bottom
        # of one 3x3 array to the right side of another, or when moving
        # the top of one to the left side of another

        if direction == Direction.CCW:  # CCW 90 degree rotation
            if face == Faces.RED:  # red face
                faces[0, :, :] = numpy.rot90(faces[0, :, :])
                faces[4, :, 0], faces[3, :, 2], faces[5, :, 0], faces[1, :, 0] = \
                    faces[1, :, 0].copy(), numpy.flip(faces[4, :, 0]).copy(), \
                    faces[3, :, 2].copy(), numpy.flip(faces[5, :, 0]).copy()

            elif face == Faces.GREEN:  # green face
                faces[1, :, :] = numpy.rot90(faces[1, :, :])
                faces[4, 2, :], faces[0, :, 2], faces[5, 0, :], faces[2, :, 0] = \
                    faces[2, :, 0].copy(), numpy.flip(faces[4, 2, :]).copy(), \
                    faces[0, :, 2].copy(), numpy.flip(faces[5, 0, :]).copy()

            elif face == Faces.ORANGE:  # orange face
                faces[2, :, :] = numpy.rot90(faces[2, :, :])
                faces[4, :, 2], faces[1, :, 2], faces[5, :, 2], faces[3, :, 0] = \
                    faces[3, :, 0].copy(), numpy.flip(faces[4, :, 2]).copy(), \
                    faces[1, :, 2].copy(), numpy.flip(faces[5, :, 2]).copy()

            elif face == Faces.BLUE:  # blue face
                faces[3, :, :] = numpy.rot90(faces[3, :, :])
                faces[4, 0, :], faces[2, :, 2], faces[5, 2, :], faces[0, :, 0] = \
                    faces[0, :, 0].copy(), numpy.flip(faces[4, 0, :]).copy(), \
                    faces[2, :, 2].copy(), numpy.flip(faces[5, 2, :]).copy()

            elif face == Faces.YELLOW:  # yellow face
                faces[4, :, :] = numpy.rot90(faces[4, :, :])
                faces[3, 0, :], faces[0, 0, :], faces[1, 0, :], faces[2, 0, :] = \
                    faces[2, 0, :].copy(), numpy.flip(faces[3, 0, :]).copy(), \
                    faces[0, 0, :].copy(), numpy.flip(faces[1, 0, :]).copy()

            elif face == Faces.WHITE:  # white face
                faces[5, :, :] = numpy.rot90(faces[5, :, :])
                faces[1, 2, :], faces[0, 2, :], faces[3, 2, :], faces[2, 2, :] = \
                    faces[2, 2, :].copy(), numpy.flip(faces[1, 2, :]).copy(), \
                    faces[0, 2, :].copy(), numpy.flip(faces[3, 2, :]).copy()

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
                faces[0, :, :] = numpy.rot90(faces[0, :, :], 3)
                faces[4, :, 0], faces[1, :, 0], faces[5, :, 0], faces[3, :, 2] = \
                    numpy.flip(faces[3, :, 2]).copy(), faces[4, :, 0].copy(), \
                    numpy.flip(faces[1, :, 0]).copy(), faces[5, :, 0].copy()

            elif face == Faces.GREEN:
                faces[1, :, :] = numpy.rot90(faces[1, :, :], 3)
                faces[4, 2, :], faces[2, :, 0], faces[5, 0, :], faces[0, :, 2] = \
                    numpy.flip(faces[0, :, 2]).copy(), faces[4, 2, :].copy(), \
                    numpy.flip(faces[2, :, 0]).copy(), faces[5, 0, :].copy()

            elif face == Faces.ORANGE:
                faces[2, :, :] = numpy.rot90(faces[2, :, :], 3)
                faces[4, :, 2], faces[3, :, 0], faces[5, :, 2], faces[1, :, 2] = \
                    numpy.flip(faces[1, :, 2]).copy(), faces[4, :, 2].copy(), \
                    numpy.flip(faces[3, :, 0]).copy(), faces[5, :, 2].copy()

            elif face == Faces.BLUE:
                faces[3, :, :] = numpy.rot90(faces[3, :, :], 3)
                faces[4, 0, :], faces[0, :, 0], faces[5, 2, :], faces[2, :, 2] = \
                    numpy.flip(faces[2, :, 2]).copy(), faces[4, 0, :].copy(), \
                    numpy.flip(faces[0, :, 0]).copy(), faces[5, 2, :].copy()

            elif face == Faces.YELLOW:
                faces[4, :, :] = numpy.rot90(faces[4, :, :], 3)
                faces[3, 0, :], faces[2, 0, :], faces[1, 0, :], faces[0, 0, :] = \
                    numpy.flip(faces[0, 0, :]).copy(), faces[3, 0, :].copy(), \
                    numpy.flip(faces[2, 0, :]).copy(), faces[1, 0, :].copy()

            elif face == Faces.WHITE:
                faces[5, :, :] = numpy.rot90(faces[5, :, :], 3)
                faces[1, 2, :], faces[2, 2, :], faces[3, 2, :], faces[0, 2, :] = \
                    numpy.flip(faces[0, 2, :]).copy(), faces[1, 2, :].copy(), \
                    numpy.flip(faces[2, 2, :]).copy(), faces[3, 2, :].copy()

        if not simulation:  # We are operating on the actual cube and need to act appropriately
            self.moves += 1
            self.notify((face, direction))

        return faces
