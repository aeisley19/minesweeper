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
        self.pressed_buttons = [];
 
    def init_board(self):
        for i in range(self.width):
            self.matrix.append([]);
            for j in range(self.height):
                sp = Space(self.master, self, i, j);
                self.matrix[i].append(sp);
                self.matrix[i][j].create_button(self.master, i, j);
        
        self.pressed_buttons = self.matrix; 
        self.set_mines();
    
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

    def get_spaces(self):
        return self.matrix;
    
class Space:
    def __init__(self, master, board, x, y):
        self.is_mine = False;
        self.is_flagged = False;
        self.pressed = False;
        self.adjacent_mines = 0;
        self.x = x;
        self.y = y;
        self.master = master;
        self.button = None;
        self.spaces = board.get_spaces();

    def set_mine(self):
        self.is_mine = True;
        self.set_adjacent_mine_count();

    def get_mine(self):
        return self.is_mine; 

    def increment_mine_count(self):
        self.adjacent_mines += 1;

    def get_mine_count(self):
        return self.adjacent_mines;

    def create_button(self, frame, x, y):
        self.button = Button(frame);
        self.button.grid(column=x, row=y);
        self.button.bind("<Button-1>", self.right_clicker);
    
    def right_clicker(self, event):
        if not self.pressed and not self.is_flagged:
            self.display();
 
    def get_button(self):
        return self.button;

    def display(self):
        if self.is_mine:
            self.game_over();
        else:
            self.display_space();

    def display_mine(self):
        self.button.config(bg="red");
        #self.button["state"] = "disabled";
    
    def game_over(self):
        for i in range(len(self.spaces)):
            for j in range(len(self.spaces[i])):
                self.spaces[i][j].get_button()["state"] = "disabled";

                if self.spaces[i][j].get_mine():
                    self.spaces[i][j].display_mine();
                    pass;
    
    def display_space(self):
            if self.button["state"] != "disabled":
                self.button["relief"] = "sunken"
                self.button["state"] = "disabled";
                print("mines" + str(self.adjacent_mines));
                


    def flag(self):
        self.button.config(bg="green");
        self.button["state"] = "disabled";

    def set_adjacent_mine_count(self):
        for i in range(-1, 1):
            for j in range(-1, 1):
                if i != 0 or j != 0:
                    self.spaces[self.x+i][self.y+j].increment_mine_count();

class Game:
    def play(self):
        root = Tk();
        root.title("Mine Sweeper");
        root.geometry('1440x720');
        root.resizable(False, False);
        root.config(bg="black")

        #main_frame = Frame(root, width=240, height=500, borderwidth=10, relief=RIDGE);
       # score_frame = Frame(main_frame, width=100, height=200, relief=RIDGE)
        game_frame = Frame(root, width=1000, height=500, borderwidth=10, relief=RIDGE);
        #main_frame.place(x=600, y=200);
        #score_frame.place(x=500, y=100);
        game_frame.place(x=500, y=100);
        
        b = Board(game_frame, 6, 6, 7);
        b.init_board();

        root.mainloop();


if __name__ == "__main__":
    game = Game();
    
    game.play();
