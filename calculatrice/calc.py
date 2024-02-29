from tkinter import *

gui = Tk()

gui.tittle("simple calculator")


gui.geometry("300x300")

tittlelabel = label(gui, text="Simple Calculator", font=("Arial", 20, "bold"))

tittlelabel.grid(columnspan=4, pady=28)

gui.mainloop()
