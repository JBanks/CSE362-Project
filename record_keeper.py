class RecordKeeper:

    def __init__(self):
        self.is_high_score = False
        self.best_times = []
        self.best_moves = []
        self.high_scores_list = []

    def get_best_times(self):
        """
        This will return a list of all the times stored in the best_times list
        :return: List<float> best_times
        """
        pass

    def get_best_moves(self):
        """
        This will return a list of all the moves stored in the best_moves list
        :return: List<int> best_moves
        """
        pass

    def check_high_score(self, moves, time):
        """
        This will return true if the current score is a greater than all others
        in high_scores_list, or false otherwise
        :param moves: int, the number of moves made by the player in the current game
        :param time: float, the time in seconds that elapsed in the current game
        :return: bool is_high_score
        """
        pass

    def post_high_score(self, moves, time):
        """
        This will enter the current score into high_scores_list
        :param moves: int, the number of moves made by the player in the current game
        :param time: float, the time in seconds that elapsed in the current game
        :return: void
        """
        pass

    def clear(self):
        """
        This will delete all entities in high_scores_list
        :return: void
        """
        pass