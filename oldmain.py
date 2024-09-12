from tkinter import Tk, BOTH, Canvas
from time import sleep
import os # for specifying game window location

class Window:

    def __init__(self, width, height): 
        self.__root = Tk() # designate root wwindow
        self.__root.title("Maze Solver") # Set title
        self.__root.geometry(f"{width}x{height}+1920+0") # Set window placement(1920 because 2 monitor)

        # use .title 'tkinter' method with title arg to set title on self.root
        self.__canvas = Canvas(self.__root, width=width, height=height)

        # set canvas widget onto root window with width and height defined in init call
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close) # when window delete, run self.close
        
        # cell params
        self.current_cell = None
        self.cell_width = 100
        self.cell_width = 100

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
    
    def draw_move(self, to_cell, undo=False):
        start_x = self.current_cell.x * self.cell_width + self.cell_width / 2
        start_y = self.current_cell.y * self.cell_height + self.cell_height / 2
        end_x = to_cell.x * self.cell_width + self.cell_width / 2
        end_y = to_cell.y * self.cell_height + self.cell_height / 2
        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        line.draw(self.__canvas, "red" if not undo else "gray")

        self.current_cell = to_cell

class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for i in range(self.num_rows): # iterate through column
            column = []
            for j in range(self.num_cols): # iterate through row
                x = self.x + (i * self.cell_size_x)
                y = self.y + (j * self.cell_size_y)
                size_x = self.cell_size_x
                size_y = self.cell_size_y
                new_cell = Cell(x, y, size_x, size_y, self.win) # create new_cell 
                column.append(new_cell) # append new cell to column
            self._cells.append(column) # after the loop append the column to _cells

            # now that they are all in _cells - draw the cells at specified spots in grid
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(.05)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, x, y, size_x, size_y, win=None): # Set window as optional and default to None
        self.has_left_wall = True # Initialize all walls as true to start
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.win = win

    @property
    def x2(self):
        return self.x + self.size_x
    
    @property
    def y2(self):
        return self.y + self.size_y
    
    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self.x, self.y), Point(self.x, self.y2))
            self.win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self.x2, self.y), Point(self.x2, self.y2))
            self.win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self.x, self.y), Point(self.x2, self.y))
            self.win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self.x, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line, "black")

def main():
    # Intro Print Debug & Window Block
    print("Launching Maze Solver")
    print("Placeholder CLI Instructions")
    win = Window(800, 800) # Define Window Size & Init Window

    maze = Maze(
            0,
            0,
            5, #rows
            5, #cols
            100, #width
            100, #height
            win,
            )

    # Close Print Debug 
    win.wait_for_close()
    print("window closed...")

if __name__ == "__main__":
    main()