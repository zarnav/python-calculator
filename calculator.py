from tkinter import *


# main window
root = Tk()
root["bg"] = "OliveDrab1"
root.title("Simple Calculator")


#create an entry text field

e = Entry(root, width=35, bg="cyan", borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# create the function which calculates
def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)
    
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_percent():
    first_number = e.get()
    global f_num
    global math
    math = "percent"
    f_num = first_number
    e.delete(0, END)

def button_clear():
    e.delete(0, END)

def button_dot():
    pass

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

    if math == "multiply":
        e.insert(0, f_num * int(second_number))

    if math == "percent":
        e.insert(0, float(f_num) * (float(second_number) / 100))


# creating buttons
button0 = Button(root, bd=5, bg="green", text="0", padx=30, pady=30, command=lambda: button_click(0))
button1 = Button(root, bd=5, bg="green", text="1", padx=30, pady=30, command=lambda: button_click(1))
button2 = Button(root, bd=5, bg="green", text="2", padx=30, pady=30, command=lambda: button_click(2))
button3 = Button(root, bd=5, bg="green", text="3", padx=30, pady=30, command=lambda: button_click(3))
button4 = Button(root, bd=5, bg="green", text="4", padx=30, pady=30, command=lambda: button_click(4))
button5 = Button(root, bd=5, bg="green", text="5", padx=30, pady=30, command=lambda: button_click(5))
button6 = Button(root, bd=5, bg="green", text="6", padx=30, pady=30, command=lambda: button_click(6))
button7 = Button(root, bd=5, bg="green", text="7", padx=30, pady=30, command=lambda: button_click(7))
button8 = Button(root, bd=5, bg="green", text="8", padx=30, pady=30, command=lambda: button_click(8))
button9 = Button(root, bd=5, bg="green", text="9", padx=30, pady=30, command=lambda: button_click(9))

buttonadd = Button(root, bd=5, bg="orange", text="+", padx=26, pady=30, command=button_add)
buttonsub = Button(root, bd=5, bg="orange", text="-", padx=28, pady=30, command=button_sub)
buttonequal = Button(root, bd=5, bg="orange", text="=", padx=29, pady=30, command=button_equal)
buttonpercent = Button(root, bd=5, bg="orange", text="%", padx=28, pady=30, command=button_percent)
buttonmultiply = Button(root, bd=5, bg="orange", text="*", padx=28, pady=30, command=button_multiply)
buttondivide = Button(root, bd=5, bg="orange", text="/", padx=28, pady=30, command=button_divide)
buttonclear = Button(root, bd=5, bg="pink", text="CE", padx=26, pady=10, command=button_clear)
buttondot = Button(root, bd=5, bg="tomato", text=".", padx=30, pady=10, command=button_dot)

buttonadd.grid(row=2, column=3)
buttonsub.grid(row=3, column=3)
buttonequal.grid(row=5, column=2)
buttonpercent.grid(row=5, column=0)
buttonmultiply.grid(row=5, column=3)
buttondivide.grid(row=4, column=3)
buttonclear.grid(row=1, column=0)
buttondot.grid(row=1, column=1)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button0.grid(row=5, column=1)

# this is the main loop of the app
root.mainloop()
