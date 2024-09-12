from graphics import Window
from maze import Maze
import sys
import shared

def regenerate_maze(num_rows, num_cols, margin, cell_size_x, cell_size_y, win=None):
    if not shared.filled:
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
        print("Maze Created")
    else:
        shared.filled = False
        win.reset_canvas()
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
        print("Maze Regenerated")

    # Reset filled status
    shared.filled = True
    print("Filled Set to True")

    print("Starting Solve")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze cannot be solved!")
    else:
        print("Maze solved!")

def close(event=None):
    try:
        sys.exit()  # Replace with your available method name
    except Exception as e:
        print(f"Error closing: {e}")

      # Use only as a last resort

def main():
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    canvas = win.get_canvas()
    title = win.get_title()
    print(f"Launching {title}")
    print("Placeholder CLI Instructions")

    # Initial maze creation
    regenerate_maze(num_rows, num_cols, margin, cell_size_x, cell_size_y, win)

    # set up keybinds
    win.bind_key('<r>', lambda event: regenerate_maze(num_rows, num_cols, margin, cell_size_x, cell_size_y, win))
    win.bind_key('<q>', lambda event: close())

    win.wait_for_close()

if __name__ == "__main__":
    main()
