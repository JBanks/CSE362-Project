import pygame
import tkinter as tk
from cube import Cube
from display import Display
from solution_provider import SolutionProvider
from record_keeper import RecordKeeper
from constants import *
from pygame.locals import *
import os


class GameController:

    def __init__(self, view, cube):
        """
        Initialize an instance of the GameController
        :param view: A game view instance
        :param cube: a cube instance
        """
        self.view = view
        self.cube = cube
        self.display = Display(self.cube)
        self.solution_provider = SolutionProvider(self.cube)
        self.solution_provider.add_observer(self)
        self.cube.add_observer(self.display)
        self.record_keeper = RecordKeeper()
        self.dimensions = 3
        self.control_state = ControlStates.WHOLE

    def update_ui(self):
        """
        Generate the contents of the user interface
        :return: void
        """
        self.view.show_start_screen()

    def get_hints(self):
        """
        Call the solution provider to retrieve a list of hints
        :return: void
        """
        self.solution_provider.get_optimum()
        self.view.show_hints_list()

    def keypress(self, key):
        """
        When a user presses a key on the keyboard, determine which action should be taken
        :param key: the key pressed by the user
        :return: void
        """
        # TODO: Make sure these function calls are correct.
        translate = {'z': 1, 'x': 2, 'c': 3, 'a': 4, 's': 5, 'd': 6, 'q': 7, 'w': 8, 'e': 9}
        arrows = {37: (0, -45), 38: (1, 45), 39: (0, 45), 40: (1, 45)}
        try:
            key_val = int(key.char)
        except:
            try:
                key_val = translate[key.char]
            except:
                self.cube.update_angle(*arrows[key.keycode])
                print(f"invalid keypress: {key}")
                return
        if (key_val - 1) % 2 == 0:
            self.control_state_update(key_val)
        elif self.control_state == ControlStates.WHOLE:
            self.cube.update_angle(*self.get_rotation(key_val))
        else:
            self.cube.move(*self.get_movement(key_val))

    def click(self, x, y):
        """
        This will take a click from the user and pass it to the appropriate handler.
        :param x: the x coordinate where the user has clicked
        :param y: the y coordinate where the user has clicked
        :return: void
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
        self.view.show_hints_list()

    def update_hints(self, moves_taken):
        self.view.show_hints_list()

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

        movements = {ControlStates.CENTER: {4: (active, Direction.CCW),
                                            6: (active, Direction.CW),
                                            2: (active, Direction.CW),
                                            8: (active, Direction.CCW)},
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
        print(f"sending movement control: {movements[self.control_state][key]}")
        return movements[self.control_state][key]

    def get_rotation(self, key):
        """
        Take the key press and determine which angle will be modified
        :param key: the key that was pressed
        :return: The axis and theta
        """
        rotation = {4: (0, -45), 8: (1, 45), 6: (0, 45), 2: (1, 45)}
        return rotation[key]

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
        old_control_state = self.control_state
        if self.control_state == control_states[key]:
            self.control_state = ControlStates.WHOLE
        else:
            self.control_state = control_states[key]
        print(f"Updating control_state from {old_control_state} to {self.control_state}")

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
        This function will initiate a game
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
        Defines the dimensions of the rubik's cube
        :param n: an integer representing the square root of the number of tiles on each side
        :return: void
        """
        print(f"set_cube({n})") # this one should call the cube's function
        self.cube.set_cube(n)

    def clear_scores(self):
        """
        Empty the high score chart to start fresh
        :return: void
        """
        self.record_keeper.clear()


class GameView(tk.Frame):

    def __init__(self, master, cube, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.grid()
        self.window_width = 800
        self.window_height = 800
        self.submenu_items = []
        self.hints_items = []
        self.canvas = tk.Canvas(self, width=self.window_width, height=self.window_height, borderwidth=0,
                                highlightthickness=0)
        self.canvas.grid()
        self.canvas.update()
        self.cube = cube
        self.controller = GameController(self, cube)
        master.bind("<KeyPress>", self.controller.keypress)
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
        best_moves = "Best Moves:\n18\n40\n15"
        for score in self.controller.record_keeper.get_best_moves():
            best_moves += f"\n{score}"
        best_times = "Best Times:\n4 minutes\n8 minutes\n19 minutes"
        for score in self.controller.record_keeper.get_best_times():
            best_times += f"\n{score} + seconds"
        label = self.canvas.create_text(left + 20, top + 20, text=best_moves, anchor="nw")
        self.submenu_items.append(label)
        label = self.canvas.create_text(right - 20, top + 20, text=best_times, anchor="ne")
        self.submenu_items.append(label)

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
            size_button = self.create_button(f'{i}x{i}x{i}', lambda event, dim=i: self.controller.set_cube(dim),
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

    def pygame_update(self):
        self.controller.display.display()
        self.controller.display.redisplay()
        pygame.display.flip()
        self.master.after(0, self.pygame_update)

    def show_hints_list(self):
        self.clear_hints_list()
        hints_state = self.controller.solution_provider.get_state()
        if len(hints_state[0]) > 0:
            width = 200
            height = 400
            top = WINDOW_HEIGHT - height - BUTTON_SIZE[1] - 2*BUTTON_MARGIN[1]
            left = WINDOW_WIDTH - width
            bottom = WINDOW_HEIGHT - BUTTON_SIZE[1] - 2*BUTTON_MARGIN[1]
            right = WINDOW_WIDTH
            hints_panel = self.canvas.create_rectangle(left, top, right, bottom, SUBMENU_STYLE)
            self.hints_items.append(hints_panel)
            hints = ""
            face_strings = ["Red", "Green", "Orange", "Blue", "Yellow", "White"]
            direction_strings = ["Clockwise", "Counter Clockwise"]
            for hint in hints_state[0]:
                hints += f"{face_strings[hint[0]]}: {direction_strings[hint[1]]}\n"
            top += 20
            left += 20
            label = self.canvas.create_text(left, top, text=hints, anchor="nw")
            self.hints_items.append(label)
            top = top + hints_state[1] * 16
            # print(f"indicator placed at position: {hints_state[1]}")
            left -= 20
            indicator = self.canvas.create_rectangle(left, top, left + 10, top + 10, BUTTON_STYLE)
            self.hints_items.append(indicator)

    def clear_hints_list(self):
        for item in self.hints_items:
            self.canvas.delete(item)

    def show_play_screen(self):

        self.canvas.delete(tk.ALL)
        self.cube_frame = tk.Frame(self.canvas, width=800, height=800)
        self.cube_frame.pack(side=tk.RIGHT)
        os.environ['SDL2_WINDOWID'] = str(self.cube_frame.winfo_id())
        os.environ['SDL2_VIDEODRIVER'] = 'dummy'

        screen = pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)
        screen.fill(pygame.Color(255, 255, 255))

        pygame.display.init()
        self.pygame_update()

        self.create_button('Save', lambda event: self.show_start_screen(),
                           location=(BUTTON_MARGIN[0],
                                     WINDOW_HEIGHT - BUTTON_SIZE[1] - BUTTON_MARGIN[1]))
        self.create_button('Hint', lambda event: self.controller.get_hints(),
                           location=(WINDOW_WIDTH - BUTTON_SIZE[0] - BUTTON_MARGIN[0],
                                     WINDOW_HEIGHT - BUTTON_SIZE[1] - BUTTON_MARGIN[1]))

    def show_finished_screen(self):
        self.canvas.delete(tk.ALL)
        y = WINDOW_HEIGHT - 2 * BUTTON_SIZE[1] - 7 * BUTTON_MARGIN[1]
        self.create_button('High Scores', lambda event: self.show_high_scores(),
                           location=((WINDOW_WIDTH - BUTTON_SIZE[0]) / 2, y))
        y += BUTTON_SIZE[1] + 2 * BUTTON_MARGIN[1]
        self.create_button('Main Screen', lambda event: self.show_start_screen(),
                           location=((WINDOW_WIDTH - BUTTON_SIZE[0]) / 2, y))

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
