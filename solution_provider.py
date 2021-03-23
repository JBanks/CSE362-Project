from constants import *


class Node:
    def __init__(self, state):
        self.parent = None
        self.steps = None
        self.hash = None
        self.state = state.copy()
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
            for tile, i in enumerate(self.state.faces):
                hash_val += tile << 3 * i
            if face % 2 == 1:
                self.hash.append(hash_val)
                hash_val = 0
        return self.hash


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
        pass

    def get_optimum(self):
        """
        This finds an optimum path between the current cube's state and the solved state.
        :return: sequence of moves that are to be made on the cube
        """
        # TODO: Complete the get_optimum function
        start_node = Node(self.cube)
        end_node = Node(finished_state)
        start_frontier = [start_node]
        end_frontier = [end_node]
        start_explored = []
        end_explored = []
        while start_frontier or end_frontier:
            current_start = start_frontier.pop()
            current_end = end_frontier.pop()
            for action in self.actions:
                new_from_start = simulate_move(current_start, action)
                if new_from_start in end_explored:
                    other_side = end_explored.find(new_from_start)
                    return path(new_from_start, other_side)
                elif new_from_start not in start_explored and new_from_start not in start_frontier:
                    start_frontier.push(new_from_start)
                new_from_end = simulate_move(current_end, action)
                if new_from_end in start_explored:
                    other_side = start_explored.find(new_from_end)
                    return path(other_side, new_from_end)
                elif new_from_end not in end_explored and new_from_end not in end_frontier:
                    end_frontier.push(new_from_end)

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
