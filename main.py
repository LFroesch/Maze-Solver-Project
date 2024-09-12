from graphics import Window
from maze import Maze
import sys
import shared
import time

def regenerate_maze(num_rows, num_cols, margin, cell_size_x, cell_size_y, win=None):
    win.start_timer()
    print("--- Time Started ---")
    if not shared.filled:
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
        print("Maze Created...")
    else:
        shared.filled = False
        win.reset_canvas()
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
        print("Maze Regenerated...")

    # Reset filled status
    
    shared.filled = True
    #print("Filled Set to True")

    print("Starting Solve!")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze cannot be solved!")
    else:
        win.end_timer()
        shared.solved = True
        elapsed_time = shared.end_time - shared.start_time
        print("-------------------------------")
        print(f"- Maze solved in {elapsed_time:.2f} seconds!-")
        print("-      Press R to Reset       -")
        print("-      Press Q to quit        -")
        print("-------------------------------")

def main():
    
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 3 * margin) / num_cols
    cell_size_y = (screen_y - 3 * margin) / num_rows
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    canvas = win.get_canvas()
    root = win.get_root()
    #print("root is defined:", root) 
    title = win.get_title()
    print(f"Launching {title}")

    # Initial maze creation
    regenerate_maze(num_rows, num_cols, margin, cell_size_x, cell_size_y, win)

    # set up keybinds
    win.bind_key('<r>', lambda event: regenerate_maze(num_rows, num_cols, margin, cell_size_x, cell_size_y, win))
    win.bind_key('<q>', lambda event: win.close())

    win.run()

if __name__ == "__main__":
    main()
