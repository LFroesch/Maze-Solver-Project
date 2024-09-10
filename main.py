from tkinter import Tk, BOTH, Canvas
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
    def __init__(self, _x1, _x2, _y1, _y2, win=None): # Set window as optional and default to None
        self.has_left_wall = True # Initialize all walls as true to start
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = win
    
    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

def main():
    # Intro Print Debug & Window Block
    print("Launching Maze Solver")
    print("Placeholder CLI Instructions")
    win = Window(800, 600) # Define Window Size & Init Window

    #p1 = Point(100, 100) # Init First Point
    #p2 = Point(300, 300) # Init Second Point
    #line1 = Line(p1, p2) # Init Line between p1 and p2
    #win.draw_line(line1, "black") # Draw on window from above with window method draw_line on line1 in black

    #            x1, x2,  y1,  y2    []
    cell1 = Cell(100, 200, 100, 200, win) # top left
    cell2 = Cell(200, 300, 200, 300, win) # bot right
    cell3 = Cell(200, 300, 100, 200, win) # top right
    cell4 = Cell(100, 200, 200, 300, win) # bot left
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()

    # Close Print Debug 
    win.wait_for_close()
    print("window closed...")

if __name__ == "__main__":
    main()