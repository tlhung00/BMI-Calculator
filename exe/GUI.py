from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")

#Variables
global weight
global height
weight_v = IntVar()
height_v = IntVar()

#BMI calculate function
def bmi():
    weight = float(w.get())
    height = float(h.get())
    bmi = weight / (height ** 2)
    messagebox.showinfo("Result", f"Your bmi is: {bmi}")

#Input

#Weight input
weightLabel = Label(root, text="Weight in kg")
weightLabel.pack()
w = Entry(root, textvariable=weight_v, width=10, borderwidth=5)
w.pack()
#weight = w.get()

#Height input
heightLabel = Label(root, text="Height in m")
heightLabel.pack()
h = Entry(root, textvariable=height_v, width=10, borderwidth=5)
h.pack()
#height = float(h.get())

#Calculate button
calc = Button(root, text="Calculate", command=bmi)
calc.pack()


root.mainloop()