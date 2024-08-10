from tkinter import *
from PIL import Image, ImageTk

def click(event):
    global scvalue
    text = event.widget.cget("text")#.cget use for capturing butten text
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()#it force to update

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
ico = Image.open('calculation.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.geometry("410x630")
root.title(" CALCULATOR ")
root.maxsize(410,630)




scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 italic",background="light blue",relief=GROOVE)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="black")
b = Button(f, text="9", padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8",padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind( "<Button-1>", click)

f.pack()


f = Frame(root, bg="black")
b = Button(f, text="6", padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind( "<Button-1>", click)

b = Button(f, text="5", padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind( "<Button-1>", click)

f.pack()


f = Frame(root, bg="black")
b = Button(f, text="3", padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind( "<Button-1>", click)

b = Button(f, text="1", padx=28, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")
b = Button(f, text="+", padx=28, pady=18, font="cursive 16 italic")
b.pack(side=LEFT, padx=16, pady=5)
b.bind( "<Button-1>", click)

b = Button(f, text="-", padx=28, pady=18, font="cursive 17 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind( "<Button-1>", click)

b = Button(f, text="=", padx=28, pady=18, font="cursive 16 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")
b = Button(f, text="*", padx=26, pady=18, font="cursive 18 italic")
b.pack(side=LEFT, padx=18, pady=9)
b.bind( "<Button-1>", click)

b = Button(f, text="%", padx=26, pady=18, font="cursive 15 italic")
b.pack(side=LEFT, padx=19, pady=5)
b.bind( "<Button-1>", click)

b = Button(f, text="/", padx=28, pady=18, font="cursive 17 italic")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="black")
b = Button(f, text="C", padx=70, pady=18, font="cursive 7 italic",background="red")
b.pack(side=LEFT, padx=15, pady=3)
b.bind( "<Button-1>", click)

b = Button(f, text="0", padx=11, pady=18, font="cursive 7 bold")
b.pack(side=LEFT, padx=13, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=11, pady=16, font="cursive 8 bold")
b.pack(side=LEFT, padx=9, pady=2)
b.bind( "<Button-1>", click)

b = Button(f, text=".", padx=11, pady=16, font="cursive 9 bold")
b.pack(side=LEFT, padx=10, pady=2)
b.bind( "<Button-1>", click)

f.pack()


root.mainloop()
