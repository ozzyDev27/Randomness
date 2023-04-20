from tkinter import *
app=Tk()
app.title('Height Calculator')
app.geometry("1x1")
app.minsize(200,60)
enterHeightText=Label(app,text="Enter your height in cm!")
enterHeightText.pack(side=TOP)
enterHeight=Entry(app)
enterHeight.pack(side=LEFT,anchor=SW)
def getHeight():
    pass
getHeight=Button(app,text="GO!",command=getHeight,bg="#ffffff")
getHeight.pack(side=RIGHT,anchor=SE)
app.mainloop()
