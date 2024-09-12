from tkinter import Tk, BOTH, Canvas
import tkinter as tk
import os
import shared
import sys
import time
import tkinter.ttk as ttk


class Window:
    
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('"The Maze Solver 3000"')
        self.__root.geometry(f"{width}x{height}+1920+0")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.configure(bg='#FFFFFF')
        self.__running = False
        
        # timer label and frame BEFORE canvas setup/filled
        self.timer_frame = ttk.Frame(self.__root)
        self.timer_frame.pack(side=tk.TOP, fill=tk.X)
        self.__timer_label = ttk.Label(
            self.timer_frame,
            text="Time: 0.00 seconds",
            foreground="black",
            font=("Helvetica", 32, "bold")
            )
        self.__timer_label.pack(pady=10)

        # Canvas setup
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=tk.BOTH, expand=True)

        self.update_timer()

    def bind_key(self, key, callback):
        #print(f"Binding key {key} to callback")
        self.__root.bind(key, callback)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False
        self.__root.destroy()
        print("Window Closed")

    def run(self):
        self.__running = True
        self.__root.mainloop()
        while self.__running:
            self.redraw()

    def get_title(self):
        return self.__root.title()

    def get_canvas(self):
        return self.__canvas
    
    def get_root(self):
        return self.__root
    
    def reset_canvas(self):
        self.__canvas.delete("all")
        print("Resetting Maze")
        shared.filled = False
        #print("Filled Set to False")
        self.redraw()

    def start_timer(self):
        shared.start_time = time.time()
        self.update_timer()
        self.reset_solved_cond()

    def end_timer(self):
        shared.end_time = time.time()
        self.update_timer()

    def update_timer(self):
    # Calculate time only if shared.start_time is valid
        if shared.start_time is not None:
            if not shared.solved:
        # Calculate how much time has elapsed since the start
                elapsed_time = time.time() - shared.start_time
        # Update your label or output with the elapsed time
                self.__timer_label.configure(text=f"Time: {elapsed_time:.2f} seconds")
        # If the loop should continue, repeat after an interval
                self.__root.after(100, self.update_timer)

    def reset_solved_cond(self):
        shared.solved = False
        

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
