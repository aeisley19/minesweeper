#from tkinter import ttk;
from tkinter import *;
import random as rand;

class Board:
    def __init__(self, master, width, height, mines):
        self.master = master;
        self.width = width;
        self.height = height;
        self.mines = mines;
        self.matrix = [];
 
    def init_board(self):
        for i in range(self.width):
            self.matrix.append([]);
            for j in range(self.height):
                sp = Space(self.master, i, j);
                self.matrix[i].append(sp);
                self.matrix[i][j].create_button(self.master, i, j);
    
    def set_mines(self):
        minepos_x = 0;
        minepos_y = 0;
        
        i = self.mines;
        while i > 0:
            minepos_x = rand.randint(0, self.width - 1);
            minepos_y = rand.randint(0, self.height - 1);

            if self.matrix[minepos_x][minepos_y].get_mine():
                pass;
            else:
                self.matrix[minepos_x][minepos_y].set_mine();
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
        self.button = None;

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

    def create_button(self, frame, x, y):
        self.button = Button(frame);
        self.button.grid(column=x, row=y);
        self.button.bind("<Button-1>", self.clicker);
    
    def clicker(self, event):
        print("clicked", self.position);
    
        if(self.is_mine):
            print("mine");
        
    def get_button(self):
        return self.button;

    def display(self):
        button = Button(self.master, text="");
        #button.grid(row=self.position[0], column=self.position[1]);

class Game:
    def play(self):
        root = Tk();
        root.title("Mine Sweeper");
        root.geometry('1440x720');
        root.resizable(False, False);
        root.configure(bg="black")

        game_frame = Frame(root, width=1000, height=500, borderwidth=10, relief=RIDGE);
        game_frame.place(x=600, y=200);
        
        b = Board(game_frame, 6, 6, 7)
        b.init_board();

        root.mainloop();


if __name__ == "__main__":
    game = Game();
    
    game.play();
