from tkinter import *
import tkinter.messagebox

def beenClicked():
    radioValue = relStatus.get()
    tkinter.messagebox.showinfo("Haonan love u", radioValue)

def changeLabel():
    name = "Thanks for click" + yourName1.get()
    yourName1.delete(0,END)
    yourName1.insert(0, "botton has been pressed")

def showButton1():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "1 has been pressed")

def showButton2():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "2 has been pressed")

def showButton3():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "3 has been pressed")

def showButton4():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "4 has been pressed")

def showButton5():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "5 has been pressed")

def showButton6():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "6 has been pressed")

def showButton7():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "7 has been pressed")

def showButton8():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "8 has been pressed")

def showButton9():
    name = InputName.get()
    InputName.delete(0,END)
    InputName.insert(0, "9 has been pressed")

app = Tk()
app.title("GUI Example")
#app.geometry('450*300+200+200')

labelText = StringVar()
labelText.set("Input Box")
label1 = Label(app, textvariable=labelText, height=4)
label1.pack()

labelText = StringVar()
labelText.set("Output Box")
label2 = Label(app, textvariable=labelText, height=4)
label2.pack()


checkBoxVal = IntVar()
checkBox1 = Checkbutton(app, variable=checkBoxVal, text='happy')
checkBox1.pack()

# 输入框
inputName = StringVar(None)
InputName = Entry(app, textvariable=inputName)
InputName.pack()

custName1 = StringVar(None)
yourName1 = Entry(app, textvariable=custName1)
yourName1.pack()


relStatus = StringVar()
relStatus.set(None)
radio1 = Radiobutton(app, text="Single", value="Single", variable = relStatus, command=beenClicked).pack()
radio1 = Radiobutton(app, text="Married", value="Married", variable = relStatus, command=beenClicked).pack()

button1 = Button(app, text="1", width=10, command=showButton1,bg='green')
button1.grid(row=0, column=0)
button1.pack(side='left', padx=0,pady=0)

button2 = Button(app, text="2(abc)", width=10, command=showButton2,bg='green')
#button2.grid(row=0, column=5)
button2.pack(side='left', padx=0,pady=0)

button3 = Button(app, text="3(def)", width=5)
#button3 = Button(app, text="3(def)", width=10, command=showButton3,bg='green')
button3.bind('<Button-1>', showButton3)             # bind left mouse clicks
button3.bind('<Double-1>', showButton4)              # bind double left clicks
button3.pack(side='left', padx=0,pady=30)

button4 = Button(app, text="4(ghi)", width=10, command=showButton4,bg='green')
button4.pack(side='left', padx=0,pady=10)

button5 = Button(app, text="5(jkl)", width=10, command=showButton5,bg='green')
button5.pack(side='left', padx=0,pady=10)

button6 = Button(app, text="6(mno)", width=10, command=showButton6,bg='green')
button6.pack(side='left', padx=0,pady=10)

button7 = Button(app, text="7(pqrs)", width=10, command=showButton7,bg='green')
button7.pack(side='left', padx=0,pady=10)

button8 = Button(app, text="8(tuv)", width=10, command=showButton8,bg='green')
button8.pack(side='left', padx=0,pady=10)

button9 = Button(app, text="9(wxyz)", width=10, command=showButton9,bg='green')
button9.pack(side='left', padx=0,pady=10)

app.mainloop()

#from Tkinter import *

#def hello(event):
#    print 'Double Click to exit'

#def quit(event):

#    print 'You double clicked...'
#    import sys; sys.exit()

#widget = Button(None, text='Hello event world')
#botton3.pack()
#widget.mainloop()











