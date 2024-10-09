import random
from tkinter import *
from tkinter import ttk

def GetRandomNum():
    global RandomNum
    RandomNum = random.randint(1, 100)
    print(f"Got the number : {RandomNum}")

def CheckGuess(RandomInt = 0):
    print("Checking the guess")
    try:
        inp1 = Text1.get(1.0, "end-1c")
        Guess = int(inp1)
        print(f"Got the guess : {Guess}")
        if(Guess == RandomNum):
            Label1.config(text = f"{Guess} is Correct ! Got a New number.")
            GetRandomNum()
        elif(Guess > RandomNum):
            Label1.config(text = f"{Guess} > Number")
        else:
            Label1.config(text = f"{Guess} < Number")
    except:
        Label1.config(text = f"Isn't a number")
        print("Exception")
    
GetRandomNum()

root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
Text1 = Text(frm, height=1, width = 5)
Text1.grid(column=0, row=0)
Label1 = Label(frm, text = "")
Label1.grid(column=3, row=1)
GuessButton = Button(frm, text="Guess", command=CheckGuess).grid(column=1, row=0)
root.wm_title = "rng_game.py"
root.mainloop()
