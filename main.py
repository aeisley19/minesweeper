from tkinter import *;
import random as rand;

class Board:
    def __init__(self, master, width, height, mines):
        self.master = master;
        self.width = width;
        self.height = height;
        self.mines = mines;
 
    def init_board(self):
        matrix = [];

        buttons = [];

        for i in range(self.width):
            matrix.append([]);
            for j in range(self.width):
                sp = Space(self.master, i, j);
                matrix[i].append(sp);
                #buttons.append(Button(self.master, text="hi").grid(row=1, column=1));
                matrix[i][j].display();
        minepos_x = 0;
        minepos_y = 0;



    def set_mines(self, matrix):
        
        i = self.mines;
        while i > 0:
            minepos_x = rand.randint(0, self.width - 1);
            minepos_y = rand.randint(0, self.height - 1);

            if matrix[minepos_x][minepos_y].get_mine():
                pass;
            else:
                matrix[minepos_x][minepos_y].set_mine();
                i -= 1;
    
    def draw_board_tl(self):
        for i in range(self.width):
            for j in range(self.height):
                current_space = Space();

                if current_space.get_is_hidden():
                    print("*", end='', flush=True);

            print("\n");

class Space:
    def __init__(self, master, x, y):
        self.is_mine = False;
        self.is_flagged = False;
        self.is_hidden = True;
        self.near_mines = 0;
        self.position = [x, y];
        self.master = master;

    def set_mine(self):
        self.is_mine = True;

    def get_mine(self):
        return self.is_mine; 

    def set_is_hidden(self):
        self.is_hidden = False;

    def get_is_hidden(self):
        return self.is_hidden;

    def get_position(self):
        return self.position;

    def display(self):
        button = Button(self.master, text="");
        button.grid(row=self.position[0], column=self.position[1]);

def play():
    root = Tk();
    root.title("Mine Sweeper");
    root.geometry('350x450')

    b = Board(root, 9, 9, 9)
    b.init_board();

    root.mainloop();

play();
