import sys
from tkinter import*

logger = Tk()
#name of the program is set as logger
logger.title('Logger+')
#sets title for program

logger.geometry("500x500")
#defines the default window wize at 500x500

helloLab = Label(text="Logger+")
helloLab.pack()
quitBut = Button(text="Quit", command = logger.quit)
quitBut.pack()
logger.mainloop()
