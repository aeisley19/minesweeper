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
        matrix = [[0] * self.width] * self.width

        #for i in range(self.width):
            #for j in range(self.width):
                #self.matrix = [i][j];

        print(matrix);
class space:
    def __init__(self, is_flag, is_mine):

        self.is_flag = is_flag;
        self.is_mine = is_mine;

my_board = board(5, 5);

my_board.init_board();
