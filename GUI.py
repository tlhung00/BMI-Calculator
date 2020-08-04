from tkinter import *

root = Tk()

#Variables
global weight
global height
weight_v = IntVar()
height_v = IntVar()

#BMI calculate function
def bmi():
    weight = w.get()
    height = h.get()
    bmi = (weight / ((height ** 2) / 1000))
    messagebox.showinfo("Result", f"Your bmi is: {bmi}")

#Input

#Weight input
weightLabel = Label(root, text="Weight")
weightLabel.pack()
w = Entry(root, textvariable=weight_v, width=30, borderwidth=5, bg="green")
w.pack()
#weight = w.get()

#Height input
heightLabel = Label(root, text="Height")
heightLabel.pack()
h = Entry(root, textvariable=height_v, width=30, borderwidth=5, bg="green")
h.pack()
#height = float(h.get())

#Calculate button
calc = Button(root, text="Calculate", command=bmi)
calc.pack()

root.title("BMI Calculator")
root.mainloop()