from tkinter import *
from tkinter.ttk import *
app=Tk()
app.title('Height Calculator')
app.geometry("1x1")
app.minsize(200,60)
enterHeightText=Label(app,text="Enter your height in cm!")
enterHeightText.pack(side=TOP)
enterHeight=Entry(app)
enterHeight.pack(side=LEFT,anchor=SW)
def getHeight():
    returnHeight=Toplevel(app)
    returnHeight.title("Height Calculator")
    returnHeight.geometry("1x1")
    returnHeight.minsize(200,60)
    giveHeight=Label(returnHeight,text=f"You are {str(enterHeight.get())} cm tall!")
    giveHeight.pack()

getHeight=Button(app,text="GO!",command=getHeight)
getHeight.pack(side=RIGHT,anchor=SE)
app.mainloop()
