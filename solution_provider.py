from constants import *
import numpy as np
import cube


class Node:
    def __init__(self, state, action=None, parent=None):
        self.parent = parent
        self.action = action
        self.steps = None
        self.hash = None
        if hasattr(state, 'faces'):
            self.state = state.faces
        else:
            self.state = state
        self.calculate_hash()

    def __eq__(self, other_node):
        """
        Overloads the == operator to compare if two nodes have equal states by using the hashes.
        :param other_node: A node that represents a rubik's cube
        :return: boolean representing hash equality
        """
        return self.hash == other_node.hash

    def calculate_hash(self):
        """
        Calculates a hash of 3 integers to represent the state of the cube.  The hash is reversible, so we could remove
        the state storage if memory space becomes an issue.

        Each tile can be represented in 3 bits (values 0 through 6).  There are 9 tiles per face, for a total of 9*3=27
        bits. 2 faces totals 54 bits per integer.  Each cube can then be represented by 3 integers
        :return: list of 3 integers
        """
        self.hash = []
        hash_val = 0
        for face in Faces:
            for tile, i in enumerate(self.state[face].flatten()):
                hash_val += tile << 3 * (i + face % 2)
            if face % 2 == 1:
                self.hash.append(hash_val)
                hash_val = 0
        return self.hash


def path(start_side, end_side):
    actions = []
    while start_side is not None:
        actions.insert(0, start_side.action)
        start_side = start_side.parent
    while end_side is not None:
        actions.append(reverse(end_side.action))
        end_side = end_side.parent
    return actions


def simulate_move(node, move):
    """
    updated_state = cube.Cube.simulate_move(node.state, move)
    new_node = Node(updated_state, action=move, parent=node)
    return new_node
    :param node: 
    :param move: 
    :return: 
    """
    """
    This method causes a 90 degree rotation of a specific face
    of the cube (this is what we have defined as a "move")
    :param face: the face to be rotated
    :param direction: the direction in which to rotate the given face
    :return: void
    """

    direction = move[1]
    face = move[0]
    faces = node.state.copy()

    if direction == Direction.CCW:
        # CCW 90 degree rotation

        if face == Faces.RED:
            # red face

            faces[0, :, :] = np.rot90(faces[0, :, :])
            temp1 = faces[1, :, 0].copy()
            temp2 = np.flip(faces[4, 2, :]).copy()
            faces[4, 2, :] = temp1
            temp1 = faces[3, :, 2].copy()
            faces[3, :, 2] = temp2
            temp2 = np.flip(faces[5, 0, :]).copy()
            faces[5, 0, :] = temp1
            faces[1, :, 0] = temp2

        elif face == Faces.GREEN:
            # green face

            faces[1, :, :] = np.rot90(faces[1, :, :])
            temp1 = faces[2, :, 0].copy()
            temp2 = np.flip(faces[4, 2, :]).copy()
            faces[4, 2, :] = temp1
            temp1 = faces[0, :, 2].copy()
            faces[0, :, 2] = temp2
            temp2 = np.flip(faces[5, 0, :]).copy()
            faces[5, 0, :] = temp1
            faces[2, :, 0] = temp2

        elif face == Faces.ORANGE:
            # orange face

            faces[2, :, :] = np.rot90(faces[2, :, :])
            temp1 = faces[3, :, 0].copy()
            temp2 = np.flip(faces[4, 2, :]).copy()
            faces[4, 2, :] = temp1
            temp1 = faces[1, :, 2].copy()
            faces[1, :, 2] = temp2
            temp2 = np.flip(faces[5, 0, :]).copy()
            faces[5, 0, :] = temp1
            faces[3, :, 0] = temp2

        elif face == Faces.BLUE:
            # blue face

            faces[3, :, :] = np.rot90(faces[3, :, :])
            temp1 = faces[0, :, 0].copy()
            temp2 = np.flip(faces[4, 2, :]).copy()
            faces[4, 2, :] = temp1
            temp1 = faces[2, :, 2].copy()
            faces[2, :, 2] = temp2
            temp2 = np.flip(faces[5, 0, :]).copy()
            faces[5, 0, :] = temp1
            faces[0, :, 0] = temp2

        elif face == Faces.YELLOW:
            # yellow face

            faces[4, :, :] = np.rot90(faces[4, :, :])
            temp1 = faces[2, :, 0].copy()
            temp2 = np.flip(faces[3, 2, :]).copy()
            faces[3, 2, :] = temp1
            temp1 = faces[0, :, 2].copy()
            faces[0, :, 2] = temp2
            temp2 = np.flip(faces[1, 0, :]).copy()
            faces[1, 0, :] = temp1
            faces[2, :, 0] = temp2

        elif face == Faces.WHITE:
            # white face

            faces[5, :, :] = np.rot90(faces[5, :, :])
            temp1 = faces[2, :, 0].copy()
            temp2 = np.flip(faces[1, 2, :]).copy()
            faces[1, 2, :] = temp1
            temp1 = faces[0, :, 2].copy()
            faces[0, :, 2] = temp2
            temp2 = np.flip(faces[3, 0, :]).copy()
            faces[3, 0, :] = temp1
            faces[2, :, 0] = temp2

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
            faces[0, :, :] = np.rot90(faces[0, :, :], 3)
            temp1 = np.flip(faces[3, :, 2]).copy()
            temp2 = faces[4, 2, :].copy()
            faces[4, 2, :] = temp1
            temp1 = np.flip(faces[1, :, 0]).copy()
            faces[1, :, 0] = temp2
            temp2 = faces[5, 0, :].copy()
            faces[5, 0, :] = temp1
            faces[3, :, 2] = temp2

        elif face == Faces.GREEN:
            faces[1, :, :] = np.rot90(faces[1, :, :], 3)
            temp1 = np.flip(faces[0, :, 2]).copy()
            temp2 = faces[4, 2, :].copy()
            faces[4, 2, :] = temp1
            temp1 = np.flip(faces[2, :, 0]).copy()
            faces[2, :, 0] = temp2
            temp2 = faces[5, 0, :].copy()
            faces[5, 0, :] = temp1
            faces[0, :, 2] = temp2

        elif face == Faces.ORANGE:
            faces[2, :, :] = np.rot90(faces[2, :, :], 3)
            temp1 = np.flip(faces[1, :, 2]).copy()
            temp2 = faces[4, 2, :].copy()
            faces[4, 2, :] = temp1
            temp1 = np.flip(faces[3, :, 0]).copy()
            faces[3, :, 0] = temp2
            temp2 = faces[5, 0, :].copy()
            faces[5, 0, :] = temp1
            faces[1, :, 2] = temp2

        elif face == Faces.BLUE:
            faces[3, :, :] = np.rot90(faces[3, :, :], 3)
            temp1 = np.flip(faces[2, :, 2]).copy()
            temp2 = faces[4, 2, :].copy()
            faces[4, 2, :] = temp1
            temp1 = np.flip(faces[0, :, 0]).copy()
            faces[0, :, 0] = temp2
            temp2 = faces[5, 0, :].copy()
            faces[5, 0, :] = temp1
            faces[2, :, 2] = temp2

        elif face == Faces.YELLOW:
            faces[4, :, :] = np.rot90(faces[4, :, :], 3)
            temp1 = np.flip(faces[0, :, 2]).copy()
            temp2 = faces[3, 2, :].copy()
            faces[3, 2, :] = temp1
            temp1 = np.flip(faces[2, :, 0]).copy()
            faces[2, :, 0] = temp2
            temp2 = faces[1, 0, :].copy()
            faces[1, 0, :] = temp1
            faces[0, :, 2] = temp2

        elif face == Faces.WHITE:
            faces[5, :, :] = np.rot90(faces[5, :, :], 3)
            temp1 = np.flip(faces[0, :, 2]).copy()
            temp2 = faces[1, 2, :].copy()
            faces[1, 2, :] = temp1
            temp1 = np.flip(faces[2, :, 0]).copy()
            faces[2, :, 0] = temp2
            temp2 = faces[3, 0, :].copy()
            faces[3, 0, :] = temp1
            faces[0, :, 2] = temp2
    return Node(faces, move, parent=node)


def reverse(action):
    if action is not None:
        direction = (action[1] + 1) % 2  # Toggle between CW and CCW
        action = (action[0], direction)
    return action


class SolutionProvider:

    def __init__(self, cube):
        """
        Initialize the Solution Provider class
        :param cube: This is a reference to the cube object that will be used to receive moves and get the state
        """
        self.cube = cube
        self.observers = []
        self.moves = []
        self.moves_taken = 0

        self.actions = []

        self.finished_state = np.zeros((6, 3, 3), dtype=int)
        for face in Faces:
            self.finished_state[face, :, :] = face
        for face in Faces:
            for direction in Direction:
                self.actions.append((face, direction))

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

    def get_teaching(self):
        """
        This uses the algorithm to learn how to solve a rubik's cube so that we can provide the moves in a way that a
        human can learn to solve a rubik's cube on their own
        :return: sequence of moves that are to be made on the cube
        """
        # This function will not be implemented for the project
        pass

    def get_optimum(self):
        """
        This finds an optimum path between the current cube's state and the solved state.
        :return: sequence of moves that are to be made on the cube
        """
        start_node = Node(self.cube)
        end_node = Node(self.finished_state)
        start_frontier = [start_node]
        end_frontier = [end_node]
        start_explored = []
        end_explored = []
        while start_frontier or end_frontier:
            current_start = start_frontier.pop(0)
            start_explored.append(current_start)
            current_end = end_frontier.pop(0)
            end_explored.append(current_end)
            for action in self.actions:
                new_from_start = simulate_move(current_start, action)
                if new_from_start in end_explored:
                    other_side = end_explored[end_explored.index(new_from_start)]
                    return path(new_from_start, other_side)
                elif new_from_start not in start_explored and new_from_start not in start_frontier:
                    start_frontier.append(new_from_start)
                new_from_end = simulate_move(current_end, action)
                if new_from_end in start_explored:
                    other_side = start_explored[start_explored.index(new_from_end)]
                    return path(other_side, new_from_end)
                elif new_from_end not in end_explored and new_from_end not in end_frontier:
                    end_frontier.append(new_from_end)

    def notify(self):
        """
        This function is called to notify any listeners that the list of moves has been updated.
        :return: void
        """
        for observer in self.observers:
            observer.update(self.moves_taken)

    def update(self, move):
        """
        This function is called by a model to inform the SolutionProvider instance that a move has been made, and to
        update their listeners
        :param move: The move that has been mode
        :return: void
        """
        if move == self.moves[self.moves_taken]:
            self.moves_taken += 1
        elif move == self.moves[self.moves_taken - 1]:  # We can retrace our steps backwards to re-watch a series of
            # moves
            self.moves_taken -= 1
        else:  # If we take a move that wasn't in-line with the provider, we are off-track and will stop providing hints
            self.moves = []
            self.moves_taken = 0
        self.notify()

    def get_state(self):
        """
        This allows the listener to retrieve the current state of the solution provider, including moves taken, and
        moves yet to be taken
        :return: sequence of moves and the number of moves taken so far
        """
        return self.moves, self.moves_taken
