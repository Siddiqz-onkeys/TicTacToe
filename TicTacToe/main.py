import tkinter as tk
from tkinter import font


#Creating a class called TicTacToeBoard to handle the display board of the game
class TicTacToeBoard(tk.Tk):
    
    #extending the "Tk" class to create a window and display a frame and the grid of cells
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells ={} #empty directory to mark the position of the cell in the cell-grid
        self.create_board()
        self.create_grid()


    #creating a display panel function for the board
    def create_board(self):
        display_frame=tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display=tk.Label(master=display_frame,text="Are You  Ready for the battle of X and O's",font=font.Font(size=30,weight="bold"),padx=100,border=10,bd=5,justify="center")
        self.display.pack()
    
    #function to create a grid
    def create_grid(self):
        grid_frame=tk.Frame(master=self, relief="sunken",highlightbackground="lightblue",highlightthickness=5)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row,weight=1,minsize=50)
            self.columnconfigure(row,weight=1,minsize=50)
            for col in range(3):
                button=tk.Button(master=grid_frame, text="", font=font.Font(size=36,weight="bold"), highlightbackground="lightblue", highlightthickness=5,width=2, height=2)
                self._cells[button]=(row,col)
                button.grid(row=row,column=col,padx=15,pady=15,sticky="nsew")
                
        
        
        
        
        
#Creating a class called TicTacToeLogic to handle the games logic
class TicTacToeLogic():
    def __init__(self):
        print("TicTacToe Logic Center")


#the main function
def main():
    #creating an instance of the the ticTacToeBoard 
    board=TicTacToeBoard()
    board.mainloop()

if __name__=="__main__":
    main()