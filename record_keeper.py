

class RecordKeeper:

    def __init__(self, cube):
        self.is_high_score = False
        self.best_times = []
        self.best_moves = []
        self.cube = cube
        # TODO find where is the time kept?

    def get_best_times(self):
        """
        This will return a list of all the times stored in the best_times list
        :return: List<float> best_times
        """

        return self.best_times

    def get_best_moves(self):
        """
        This will return a list of all the moves stored in the best_moves list
        :return: List<int> best_moves
        """
        return self.best_moves

    def check_high_score(self, moves, time):
        """
        This will return True if the current moves is less than any other in
        best_moves, or if the current time is less than any other in best_times,
        or will return False otherwise, and posts the high score
        :param moves: int, the number of moves made by the player in the current game
        :param time: float, the time in seconds that elapsed in the current game
        :return: bool is_high_score
        """

       # do the same for time
        if self.cube.moves < self.best_moves[0]:
            self.is_high_score = True
        self.best_moves.append(self.cube.moves)
        self.best_moves.sort()

        return self.is_high_score

    # can we get rid of this?
    def post_high_score(self, moves, time):
        """
        This will enter the current score into either best_times and best_moves
        :param moves: int, the number of moves made by the player in the current game
        :param time: float, the time in seconds that elapsed in the current game
        :return: void
        """
        # self.best_times.append(game.total_time)
        # sort the list
        self.best_moves.append(self.cube.moves)
        # sort the list

    def clear(self):
        """
        This will delete all entities in best_times and best_moves
        :return: void
        """
        self.best_moves = []
        self.best_times = []
