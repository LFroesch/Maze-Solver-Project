from tkinter import Tk, BOTH, Canvas
import os
import shared
import sys

class Window:
    
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver 3000")
        self.__root.geometry(f"{width}x{height}+1920+0")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def bind_key(self, key, callback):
        print(f"Binding key {key} to callback")
        self.__root.bind(key, callback)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False
        self.__root.destroy()
        print("Window closed")

    def run(self):
        self.__running = True
        self.__root.mainloop()

    def get_title(self):
        return self.__root.title()

    def get_canvas(self):
        return self.__canvas
    
    def reset_canvas(self):
        self.__canvas.delete("all")
        print("Resetting Canvas")
        shared.filled = False
        print("Filled Set to False")
        self.redraw()

    def quit():
        sys.exit()
        


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
