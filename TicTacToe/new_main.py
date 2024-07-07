from itertools import cycle
import tkinter as tk
from typing import NamedTuple


root=tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("500x600")


# Tic Tac Toe board setup
class ticTacToe_setUp:
    #constructrr function to set the label 
    def __init__(self) -> None:
        self.label=tk.Label(root, text="The battle of X's and O's", font=('Arial',30))
        self.label.pack()
        self.cells={}
        self.gridOfCells(3)
        
        self.default_players=(Player(label="X",color="red"),
                              Player(label="O",color="yellow"))
        self.players=cycle(self.default_players)
        self.current_player=next(self.players)
        self.count=0
        self.haswinner=False
        self._moves_made={(row,col):" " for col in range(3) for row in range(3)}
        self.winningmoves()
        
        

        
    
    #function to create the game board and buttons
    def gridOfCells(self,n):
        self.buttonFrame=tk.Frame(root)
        for col in range(n):
            self.buttonFrame.columnconfigure(col,weight=1)
        
        for rows in range(n):
            for cols in range(n):
                btn=tk.Button(self.buttonFrame,text="",font=('Arial',18),width=15,height=5,bg="white")
                self.cells[btn]=(rows,cols)   
                btn.bind("<ButtonPress-1>",self.play)
                btn.grid(row=rows,column=cols,pady=2,sticky=tk.E+tk.W)        
        
                        
        self.buttonFrame.pack(fill="x",padx=10,pady=20)
        
    
    #funtion to set the moves that define a win
    def winningmoves(self):
        # the winning combinations are all the row +all the cols + Diagnol 1 + Diagnol 2
        rows=[[(row,col) for col in range(3)] for row in range(3)]
        cols=[[(col,row) for col in range(3)] for row in range(3)]
        diagnol1=[[(row,row) for row in range(3)]for row in range(3)]
        diagnol2=[[(row,2-row) for row in range(3)]for row in range(3)]
        self.winning_combos=rows+cols+diagnol1+diagnol2
        
        
    
    #funtion to maintain the history of moves made buy the players
    def moves_made(self,row,col,button):
        # stores all the moves made by both the players"
        self._moves_made[(row,col)]=button["text"]
        
        
    #function to declare a winner
    def isWinner(self):
        if self.count >=5:
            #print("entered")
            for combo in self.winning_combos:
                results=""
                for (r,c) in combo:
                    results+=self._moves_made[(r,c)]                  
                if results=="XXX" or results=="OOO":
                    self.disable_buttons()
                    txt=results[0]+" Has won this round"
                    self.update_diaplay(txt)
                    return True       
        else:
            return False
                
    #fubnction to diabl;e all the buttons at once after the winner is identified
    def disable_buttons(self):
        global root
        for child in root.winfo_children():
            if isinstance(child, tk.Button):
                child.config(state="disabled")
    
    #function to update the diaplay and stop the execution
    def update_diaplay(self,txt):
        self.label=tk.Label(root,text=txt)
        self.label.place(relx=0.5,rely=0.5,anchor="center")
                
    #function to check for a tie
    def tie_game(self):
        #print("called")
        state=True
        for coords in self._moves_made:
            if self._moves_made[coords]==" ":
                state=False
        if state==True and not self.isWinner():
            self.disable_buttons()
            txt="This round is tied"
            self.update_diaplay(txt)

            
        
        
    #funtion to check if the move is valid or not
    def move_is_valid(self,button):
        
        if not self.isWinner() and button["text"]=="":
            return True
        else:
            return False
        
    
        
    
    #funtion to handle the gameplay
    def play(self,event):
        ## contains the sequence and flow of the game that should be maintained
        #1. checks if the move is valid ---- valid if the move has'nt been played yet and the winner is not yet declared
        #2. if the move is valid --- check for the existence of a winning combination
        #                        --- if the combination exists winner is declared
        #                        --- else rotates the player and the next player should play 
        #       ---- this cycle should be repeated ---
        # should give the option for a new game.
        self.clicked_btn=event.widget
        self.row_,self.col_=self.cells[self.clicked_btn]
        #self.current_player=next(self.players)
        if self.move_is_valid(self.clicked_btn):     
            self.clicked_btn["text"]=self.current_player.label
            self.clicked_btn["state"]="disabled"
            self.clicked_btn["bg"]=self.current_player.color
            self.moves_made(self.row_,self.col_,self.clicked_btn)
            #print(self._moves_made)
            self.current_player=next(self.players)
            self.count+=1
            self.isWinner()
            self.tie_game()
        
        
       
        
        

# class to define the attributes of a player        
class Player(NamedTuple):
        label: str
        color: str
            
            
    


#class to define the attributes of a move
class Move(NamedTuple):
    row: int
    col:int
    label: str=""
    board_size=3
    
    
    
    
#start of the main function
game=ticTacToe_setUp()



tk.mainloop()
        