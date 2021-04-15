from constants import *
import numpy as np


def path(start_side, end_side):
    """
    Develop a list of actions from two sides of a perimeter search
    :param start_side: the side of the path that represents to source state
    :param end_side: the side of the path that represents the destination state
    :return: a concatenated list, with one of the actions of one list reversed
    """
    actions = []
    while start_side is not None:
        if start_side.action is not None:
            actions.insert(0, start_side.action)
        start_side = start_side.parent
    while end_side is not None:
        if end_side.action is not None:
            actions.append(reverse(end_side.action))
        end_side = end_side.parent
    return actions


def reverse(action):
    """
    Reverse the action provided
    :param action: a tuple of the face and direction
    :return: a tuple with the same face and the opposite direction
    """
    if action is not None:
        direction = Direction.CW if action[1] is Direction.CCW else Direction.CCW  # Toggle between CW and CCW
        action = (action[0], direction)  # tuples are immutable, must create a new one.
    return action


class Node:
    def __init__(self, state, action=None, parent=None):
        """
        Initialize a node for representing the path to a solution
        :param state: either the array of faces, or the cube object
        :param action: the action that was taken to achieve the current state
        :param parent: a reference to the node that was the source of the current state
        """
        self.parent = parent
        self.action = action
        self.steps = None
        self.hash = None
        if hasattr(state, 'faces'):
            self.state = state.faces
        else:
            self.state = state
        self.calculate_hash()

    def __eq__(self, other):
        """
        Overloads the == operator to compare if two nodes have equal states by using the hashes.
        :param other: A node that represents a rubik's cube
        :return: boolean representing hash equality
        """
        return self.hash == other.hash

    def __lt__(self, other):
        return self.hash < other.hash

    def __le__(self, other):
        return self.hash <= other.hash

    def __gt__(self, other):
        return self.hash > other.hash

    def __ge__(self, other):
        return self.hash >= other.hash

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


class SolutionProvider:

    def __init__(self, current_cube):
        """
        Initialize the Solution Provider class
        :param current_cube: This is a reference to the cube object that will be used to receive moves and get the state
        """
        self.cube = current_cube
        self.cube.add_observer(self)
        self.observers = []
        self.moves = []
        self.moves_taken = 0

        self.finished_state = np.zeros((6, 3, 3), dtype=int)
        for face in Faces:
            self.finished_state[face, :, :] = face

        self.actions = []
        for face in Faces:
            for direction in Direction:
                self.actions.append((face, direction))

    def __del__(self):
        self.cube.remove_observer(self)

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

    def simulate_move(self, node, move):
        """
        updated_state = cube.Cube.simulate_move(node.state, move)
        new_node = Node(updated_state, action=move, parent=node)
        return new_node
        :param node: The current node
        :param move: A tuple of face and direction showing which move to make
        :return: a new node of the updated state with the action and parent set
        """
        direction = move[1]
        face = move[0]
        faces = node.state.copy()
        self.cube.move(face, direction, faces)
        return Node(faces, move, parent=node)

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
                new_from_start = self.simulate_move(current_start, action)
                if new_from_start in end_explored:
                    other_side = end_explored[end_explored.index(new_from_start)]
                    self.moves = path(new_from_start, other_side)
                    return
                elif new_from_start not in start_explored and new_from_start not in start_frontier:
                    start_frontier.append(new_from_start)
                new_from_end = self.simulate_move(current_end, action)
                if new_from_end in start_explored:
                    other_side = start_explored[start_explored.index(new_from_end)]
                    self.moves = path(other_side, new_from_end)
                    return
                elif new_from_end not in end_explored and new_from_end not in end_frontier:
                    end_frontier.append(new_from_end)

    def notify(self):
        """
        This function is called to notify any listeners that the list of moves has been updated.
        :return: void
        """
        for observer in self.observers:
            observer.update_hints(self.moves_taken)

    def update(self, move):
        """
        This function is called by a model to inform the SolutionProvider instance that a move has been made, and to
        update their listeners
        :param move: The move that has been mode
        :return: void
        """
        if len(self.moves) > 0:
            if move == self.moves[self.moves_taken]:
                self.moves_taken += 1
            elif move == self.moves[self.moves_taken - 1]:  # We can retrace our steps backwards to re-watch a series of
                # moves
                self.moves_taken -= 1
            else:  # If we take a move that wasn't in-line with the provider, we are off-track and will stop providing hints
                self.moves = []
                self.moves_taken = 0
            if self.moves_taken >= len(self.moves):
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
