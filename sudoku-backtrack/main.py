import tkinter as tk
from tkinter import messagebox

# class for the sudoku solver
class Sudoku:
    # intialize constructor with game properties
    def __init__(self, size):
        self.window = tk.Tk()
        # game window
        self.window.title("Sudoku Solver")
        width = size * 115
        height = size * 65 + 140
        self.window.geometry(f"{width}x{height}")
        self.size = size
        # intial puzzle with 0s
        self.grid = [[0] * size for _ in range(size)]
        # dictionary for game components
        self.entries = {}
        # grid components
        for i in range(size):
            for j in range(size):
                # create component and place on grid
                e = tk.Entry(self.window, width=5, font=("arial", 22))
                e.grid(row=i, column=j, padx=5, pady=5)
                # store in dictionary
                self.entries[(i, j)] = e
        # solver button & its placement on grid
        solver = tk.Button(self.window, text="Solve", command=self.solvePuzzle, font=("arial", 24))
        solver.grid(row=size, column=0, columnspan=size, padx=5, pady=5)
        # reset button & its placement on grid
        reset = tk.Button(self.window, text="Reset", command=self.resetPuzzle, font=("arial", 24))
        reset.grid(row=size+1, column=0, columnspan=size, padx=5, pady=5)
    # method to solve the puzzle
    def solvePuzzle(self):
        # get values from grid
        for i in range(self.size):
            for j in range(self.size):
                # get value frm grid
                val = self.entries[(i, j)].get()
                # if not empty convert to int and store in grid
                if (val):
                    self.grid[i][j] = int(val)
        # solve the puzzle
        if self.solveSudoku(self.grid):
            # show the puzzle
            for i in range(self.size):
                for j in range(self.size):
                    # clear entries
                    self.entries[(i, j)].delete(0, tk.END)
                    # insert solved entries 
                    self.entries[(i, j)].insert(0, self.grid[i][j])
        else:
            messagebox.showerror("Error", "No solution exists.")
    # method to solve puzzle using backtracking        
    def solveSudoku(self, grid):
        for i in range(self.size):
            for j in range(self.size):
                if (grid[i][j] == 0):
                    for val in range(1, self.size+1):
                        if self.isValid(grid, i, j, val):
                            grid[i][j] = val
                            if self.solveSudoku(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True
    # method to check for valid value in game grid
    def isValid(self, grid, row, col, val):
        # check value already row or column
        for i in range(self.size):
            if (grid[row][i] == val or grid[i][col] == val):
                return False
        # value already present in box
        box_size = int(self.size ** 0.5)
        box_row = row - row % box_size
        box_col = col - col % box_size
        for i in range(box_size):
            for j in range(box_size):
                if (grid[box_row+i][box_col+j] == val):
                    return False
        return True
    # method to reset values
    def resetPuzzle(self):
        for i in range(self.size):
            for j in range(self.size):
                # remove all one by one
                self.entries[(i, j)].delete(0, tk.END)
                # reset grid
                self.grid[i][j] = 0
    # method to run the game
    def run(self):
        self.window.mainloop()
    
# main game function
def main():
    # intiate new window
    root = tk.Tk()
    root.title("Sudoku Solver")
    # function to create new puzzle
    def createSolver(size):
        root.destroy()
        solver = Sudoku(size)
        solver.run()
    # buttons for various puzzle sizes
    tk.Button(root, text="6x6", command=lambda: createSolver(6)).pack()
    tk.Button(root, text="9x9", command=lambda: createSolver(9)).pack()
    tk.Button(root, text="12x12", command=lambda: createSolver(12)).pack()
    # intiate game loop
    root.mainloop(0)
    
if __name__ == "__main__":
    main()