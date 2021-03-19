

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
        pass

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
