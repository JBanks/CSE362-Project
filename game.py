import tkinter as tk
from cube import Cube
from solution_provider import SolutionProvider
from constants import *


class GameController:

    def __init__(self, view, cube):
        """
        Initialize an instance of the Game class

        """
        self.view = view
        self.cube = cube
        self.solution_provider = SolutionProvider(self.cube)
        self.dimensions = 3
        self.control_state = ControlStates.WHOLE
        pass

    def update_ui(self):
        self.view.show_start_screen()

    def get_hints(self):
        self.solution_provider.get_optimum()

    def keypress(self, key):
        """
        When a user presses a key on the keyboard, determine which action should be taken
        :param key:
        :return:
        """
        print(f"keypress({key})")

    def click(self, x, y):
        """
        This will take a click from the user and pass it to the appropriate handler.
        :param x: the x coordinate where the user has clicked
        :param y: the y coordinate where the user has clicked
        :return:
        """
        print(f"click({x}, {y})")

    def drag(self, start_x, start_y, x, y):
        """
        If the user clicks and drags their mouse, determine what to do with the coordinates from the start and the end
        of the drag
        :param start_x: the x coordinate where the user first clicked
        :param start_y: the y coordinate where the user first clicked
        :param x: the x coordinate where the user released their click
        :param y: the y coordinate where the user released their click
        :return: void
        """
        print(f"drag({start_x}, {start_y}, {x}, {y})")

    def update(self, move):
        """
        Receives the move that was made and updates its internal cube representation
        :param move: the move that was made on the cube
        :return: void
        """
        print(f"update({move})")

    def get_movement(self, key):
        """
        Take the key press and determine which move is to be made on the cube.
        TODO: finish face detection logic
        :param key: The key that was pressed.
        :return: The face and direction of the move to be made.
        """

        # TODO: Determine which faces are in the positions specified
        active = Faces.GREEN
        top = Faces.YELLOW
        left = Faces.RED
        right = Faces.ORANGE
        bottom = Faces.WHITE

        movements = {ControlStates.CENTER: {4: (active, Direction.CW),
                                            6: (active, Direction.CCW)},
                     ControlStates.TOP_LEFT: {4: (top, Direction.CW),
                                              6: (top, Direction.CCW),
                                              2: (left, Direction.CW),
                                              8: (left, Direction.CCW)},
                     ControlStates.TOP_RIGHT: {4: (top, Direction.CW),
                                               6: (top, Direction.CCW),
                                               2: (right, Direction.CCW),
                                               8: (right, Direction.CW)},
                     ControlStates.BOTTOM_LEFT: {4: (bottom, Direction.CCW),
                                                 6: (bottom, Direction.CW),
                                                 2: (left, Direction.CW),
                                                 8: (left, Direction.CCW)},
                     ControlStates.BOTTOM_RIGHT: {4: (bottom, Direction.CCW),
                                                  6: (bottom, Direction.CW),
                                                  2: (right, Direction.CCW),
                                                  8: (right, Direction.CW)}}
        return movements[self.control_state][key]

    def get_rotation(self, key):
        """
        Take the key press and determine which angle will be modified
        :param key: the key that was pressed
        :return: The axis and theta
        """
        print(f"get_rotation({key})")

    def control_state_update(self, key):
        """
        Change the current movement state
        TODO: Perhaps we can have an indicator to show which state we're in
        :param key: the key that was pressed
        :return: void
        """
        control_states = {1: ControlStates.BOTTOM_LEFT,
                          3: ControlStates.BOTTOM_RIGHT,
                          5: ControlStates.CENTER,
                          7: ControlStates.TOP_LEFT,
                          9: ControlStates.TOP_RIGHT}
        if self.control_state == control_states[key]:
            self.control_state = ControlStates.WHOLE
        else:
            self.control_state = control_states[key]

    def reset(self):
        """

        :return:
        """
        print(f"reset()")

    def quit(self):
        """

        :return:
        """
        print(f"quit()")

    def check_movement(self, key):
        """

        :param key:
        :return:
        """
        print(f"check_movement({key})")

    def check_rotation(self, key):
        """

        :param key:
        :return:
        """
        print(f"check_rotation({key})")

    def save(self):
        """

        :return:
        """
        print(f"save()")

    def start_game(self):
        """

        :return:
        """
        self.view.show_play_screen()

    def ask_location(self):
        """

        :return:
        """
        print(f"ask_location()")

    def insert_location(self, location):
        """

        :param location:
        :return:
        """
        print(f"insert_location({location})")

    def set_cube(self, n):
        """

        :param n: an integer representing the square root of the number of tiles on each side
        :return: void
        """
        print(f"set_cube({n})")


class GameView(tk.Frame):

    def __init__(self, master, cube, **kw):
        super().__init__(master, **kw)
        self.grid()
        self.window_width = 800
        self.window_height = 800
        self.submenu_items = []
        self.canvas = tk.Canvas(self, width=self.window_width, height=self.window_height, borderwidth=0,
                                highlightthickness=0)
        self.canvas.grid()
        self.canvas.update()
        self.cube = cube
        self.controller = GameController(self, cube)
        self.controller.update_ui()

    def show_start_screen(self):
        self.canvas.delete(tk.ALL)
        y = WINDOW_HEIGHT - 4 * BUTTON_SIZE[1] - 7 * BUTTON_MARGIN[1]
        self.create_button('Load Game', lambda event: self.controller.start_game(),
                           location=((WINDOW_WIDTH - BUTTON_SIZE[0]) / 2, y))
        y += BUTTON_SIZE[1] + 2 * BUTTON_MARGIN[1]
        self.create_button('High Scores', lambda event: self.show_high_scores(),
                           location=((WINDOW_WIDTH - BUTTON_SIZE[0]) / 2, y))
        y += BUTTON_SIZE[1] + 2 * BUTTON_MARGIN[1]
        self.create_button('Dimensions', lambda event: self.show_dimension_selection(),
                           location=((WINDOW_WIDTH - BUTTON_SIZE[0]) / 2, y))
        y += BUTTON_SIZE[1] + 2 * BUTTON_MARGIN[1]
        self.create_button('Play', lambda event: self.controller.start_game(),
                           location=((WINDOW_WIDTH - BUTTON_SIZE[0]) / 2, y))

    def show_high_scores(self):
        self.clear_submenu()
        width = 300
        height = 400
        top = (WINDOW_HEIGHT - height) / 2
        left = (WINDOW_WIDTH - width) / 2
        bottom = (WINDOW_HEIGHT + height) / 2
        right = (WINDOW_HEIGHT + width) / 2
        submenu = self.canvas.create_rectangle(left, top, right, bottom, SUBMENU_STYLE)
        self.submenu_items.append(submenu)
        x = left + BUTTON_MARGIN[0]
        y = top + 200
        clear_button = self.create_button('Clear Chart', lambda event: self.controller.clear_scores(), location=(
            left + (width - BUTTON_SIZE[0]) / 2,
            top + (height - 2 * BUTTON_SIZE[1] - 3 * BUTTON_MARGIN[1]))
                                          )
        select_button = self.create_button('Close', lambda event: self.clear_submenu(), location=(
            left + (width - BUTTON_SIZE[0]) / 2,
            top + (height - BUTTON_SIZE[1] - BUTTON_MARGIN[1]))
                                           )
        for widget in clear_button:
            self.submenu_items.append(widget)
        for widget in select_button:
            self.submenu_items.append(widget)

    def show_dimension_selection(self):
        self.clear_submenu()
        width = 250
        height = 400
        top = (WINDOW_HEIGHT - height) / 2
        left = (WINDOW_WIDTH - width) / 2
        bottom = (WINDOW_HEIGHT + height) / 2
        right = (WINDOW_HEIGHT + width) / 2
        submenu = self.canvas.create_rectangle(left, top, right, bottom, SUBMENU_STYLE)
        self.submenu_items.append(submenu)
        x = left + BUTTON_MARGIN[0]
        y = top + 200
        for i in [2, 3, 4]:
            size_button = self.create_button(f'{i}x{i}', lambda event, dim=i: self.controller.set_cube(dim),
                                             location=(x, y))
            y += BUTTON_SIZE[1] + 2 * BUTTON_MARGIN[1]
            for widget in size_button:
                self.submenu_items.append(widget)
        select_button = self.create_button('Select', lambda event: self.clear_submenu(), location=(
            left + (width - BUTTON_SIZE[0]) / 2,
            top + (height - BUTTON_SIZE[1] - BUTTON_MARGIN[1]))
                                           )
        for widget in select_button:
            self.submenu_items.append(widget)

    def show_play_screen(self):
        self.canvas.delete(tk.ALL)
        self.create_button('Save', lambda event: self.show_start_screen(),
                           location=(BUTTON_MARGIN[0],
                                     WINDOW_HEIGHT - BUTTON_SIZE[1] - BUTTON_MARGIN[1]))
        self.create_button('Hint', lambda event: self.controller.get_hints(),
                           location=(WINDOW_WIDTH - BUTTON_SIZE[0] - BUTTON_MARGIN[0],
                                     WINDOW_HEIGHT - BUTTON_SIZE[1] - BUTTON_MARGIN[1]))

    def show_finished_screen(self):
        print("show_finished_screen()")

    def clear_submenu(self):
        for submenu_item in self.submenu_items:
            self.canvas.delete(submenu_item)

    def create_button(self, text, action, size=BUTTON_SIZE, location=BUTTON_BOTTOM_RIGHT, rect_style=BUTTON_STYLE,
                      text_style=BUTTON_TEXT_STYLE):
        w, h = size
        x0, y0 = location
        box = self.canvas.create_rectangle(x0, y0, x0 + w, y0 + h, **rect_style)
        label = self.canvas.create_text(x0 + w / 2, y0 + h / 2, text=text, **text_style)
        self.canvas.tag_bind(box, '<Button-1>', action)
        self.canvas.tag_bind(label, '<Button-1>', action)
        return box, label


if __name__ == "__main__":
    root = tk.Tk()
    GameView(root, Cube())
    root.title("CSE 362 - Rubik's Game")
    root.wm_resizable(0, 0)

    root.mainloop()
