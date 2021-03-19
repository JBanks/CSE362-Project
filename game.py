

class Game:
    def keypress(self, key):
        """

        :param key:
        :return:
        """
        pass

    def click(self, x, y):
        """
        This will take a click from the user and pass it to the appropriate handler.
        :param x: the x coordinate where the user has clicked
        :param y: the y coordinate where the user has clicked
        :return:
        """
        pass

    def drag(self, start_x, start_y, x, y):
        pass

    def update(self, move):
        pass

    def get_movement(self, key):
        pass

    def get_rotation(self, key):
        pass

    def state_update(self, key):
        pass

    def reset(self):
        pass

    def quit(self):
        pass

    def check_movement(self, key):
        pass

    def check_rotation(self, key):
        pass

    def save(self):
        pass

    def start_game(self):
        pass

    def ask_location(self):
        pass

    def insert_location(self, location):
        pass

    def set_cube(self, n):
        pass
