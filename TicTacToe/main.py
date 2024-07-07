import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

#Creating a class called TicTacToeBoard to handle the display board of the game
class TicTacToeBoard(tk.Tk):
    
    #extending the "Tk" class to create a window and display a frame and the grid of cells
    def __init__(self,game):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self.geometry("500x500")
        self._cells ={} #empty directory to mark the position of the cell in the cell-grid
        self._game=game
        self.create_board()
        self.create_grid()


    #creating a display panel function for the board
    def create_board(self):
        display_frame=tk.Frame(self)
        display_frame.pack(fill=tk.X)
        self.display=tk.Label(master=display_frame,text="Are You  Ready for the battle of X and O's",font=font.Font(size=30,weight="bold"),padx=100,border=10,bd=5,justify="center")
        self.display.pack()
    
    #function to create a grid
    def create_grid(self):
        grid_frame=tk.Frame(master=self,highlightbackground="lightblue",highlightthickness=5)
        
        for row in range(3):
            grid_frame.rowconfigure(row,weight=1)
            grid_frame.columnconfigure(row,weight=1)
            for col in range(3):
                button=tk.Button(master=grid_frame, text="", font=font.Font(size=36,weight="bold"), highlightbackground="lightblue", highlightthickness=5,width=2, height=2)
                self._cells[button]=(row,col)
                button.bind("<ButtonPress-1>",self.play)
                button.grid(row=row,column=col,sticky=tk.E+tk.W)
                
        grid_frame.pack(fill=tk.X)
    
    
    #funtion to update the button status
    def _update_button(self,clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)
       
    #funciton to update the display
    def _update_display(self, msg,color="black"):
        self.display["text"]=msg
        self.display["fg"]=color
        
    #function to hightlight the cells
    def _hightlight_cells(self):
        for button,coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="green")
                
                
    
    #creating a funtion handle the game play by listening to the event
    def play(self,event):
        clicked_btn=event.widget
        row,col=self._cells[clicked_btn]
        move=Move(row,col,self._game.current_player.label)
        print(row,col)
        self._game._move_process(move)
        if self._game._is_valid_move(move):
            self._game._upadate_button(clicked_btn)
            
            if self._game_is_tied():
                self._update_display(msg="Tied Game!!",color="blue")
            elif self._game.has_winnner():
                self._highlight_cells()
                msg=f'Player "{self._game.current_player.label}" won!'
                color=self._game.current_player.color
                self._update_display(msg,color)
            else:
                self._game.toggle_player()
                msg=f"{self._game.current_player.label}'s turn"
                self._update_display(msg)
                
#creating a class for players
class Player(NamedTuple):
    label: str
    color: str

#creating a class for moves
class Move(NamedTuple):
    row: int
    col: int
    label: str=""  
    BOARD_SIZE = 3
    DEFAULT_PLAYERS=(Player(label="X",color="red"),
                     Player(label="O",color="yellow"))
        
        
        
#Creating a class called TicTacToeLogic to handle the games logic
class TicTacToeLogic():
    def __init__(self,players=Move.DEFAULT_PLAYERS,board_size=Move.BOARD_SIZE):
        self._players=cycle(players)
        self.board_size=board_size
        self.current_player=next(self._players)
        self.winner_combo=[]
        self._current_moves=[]
        self._has_winner=False
        self._winning_combos=[]
        self._setup_board()
    
    #defining the boardsetup 
    def _setup_board(self):
        self._current_moves=[
            [Move(row,col) for col in range(self.board_size)
             for row in range(self.board_size)]
        ]
        self._winning_combos=self._get_winning_combo()
        
    #defining the winning combinations
    def _get_winning_combo(self):
        rows=[[(move.row,Move.col) for move in row] for row in self._current_moves]
        columns=[[(move.row,move.col)for move in col]for col in self._current_moves]
        first_diagnol=[row[i] for i,row in enumerate(rows)]
        second_diagnol=[col[j] for j,col in enumerate(reversed(columns))]
        return rows+columns+[first_diagnol+second_diagnol]
    
    #funtion to toggle the players
    def _toggle_players(self):
        self.current_player=next(self._players)
        
    
    #funtion that checks if the move is valid or not
    def _is_valid_move(self,move):
        row,col=move.row,move.col
        no_winner= not self._has_winner()
        move_not_played= self._current_moves[row][col].label == ""
        return no_winner and move_not_played
    
    #function to process the move of the player
    def _move_process(self,move):
        row,col=move.row,move.col
        self._current_moves[row][col]=move
        for combo in self._winning_combos:
            results=set(self._current_moves(n,m).label for n,m in combo)
        
        is_win =(len(results)==1) and ("" not in results)
        
        if is_win:
            self._has_winner=True
            self.winner_combo=combo
            
        
    #returning the winner status 
    def has_winner(self):
        return self.has_winner
    
    
    #defining the situation for a tie
    def is_tied(self):
        no_winner= not self.has_winner
        played_moves=(move.label for row in self._current_moves for move in row) #this is a generator expression to store the combination of all the values at the label
        return no_winner and all(played_moves)
    
#the main function
def main():
    #creating an instance of the the ticTacToeBoard 
    game=TicTacToeLogic()
    board=TicTacToeBoard(game)
    board.mainloop()

if __name__=="__main__":
    main()