import tkinter as tk;
import random as rand;

#window = tk.Tk();
#window.mainloop();

class board:
    def __init__(self, width, height, mines):
        self.width = width;
        self.height = height;
        self.mines = mines;
 
    def init_board(self):
        matrix = [];

        for i in range(self.width):
            matrix.append([]);
            for j in range(self.width):
                sp = space();
                matrix[i].append(sp);

        minepos_x = 0;
        minepos_y = 0;

        i = self.mines;
        while i > 0:
            minepos_x = rand.randint(0, self.width - 1);
            minepos_y = rand.randint(0, self.height - 1);

            if matrix[minepos_x][minepos_y].get_mine():
                pass;
            else:
                matrix[minepos_x][minepos_y].set_mine();
                i -= 1;

class space:
    def __init__(self):
        self.is_mine = False;
        self.flagged = False;
        self.near_mines = 0;

    def set_mine(self):
        self.is_mine = True;

    def get_mine(self):
        return self.is_mine; 

my_board = board(5, 5, 5);

my_board.init_board();
