from tkinter import*
Window = Tk()
Window.title("Calculator")

operator = ""
text_Input = StringVar()

# GUI Window
e = Entry(Window, font=('arial', 20, 'bold'),insertwidth=4, bd=30, bg="powder blue",
          textvariable=text_Input).grid(row=0, column=0, columnspan=4, ipadx=30, ipady=5, padx=2, pady=3)
Window.configure(bg='powder blue')

# Function for the buttons
def button_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def button_clear():
    global operator
    operator = ""
    text_Input.set("")

def button_equal():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

# Put buttons on screen
button_C = Button(Window, text="C", padx=168, height=1, font=('arial', 20, 'bold'), command=button_clear)
button_1 = Button(Window, text="1", width=5, height=1,padx=4,font=('arial', 20, 'bold'), command=lambda: button_click(1))
button_2 = Button(Window, text="2", width=5, height=1,padx=4,font=('arial', 20, 'bold'), command=lambda: button_click(2))
button_3 = Button(Window, text="3", width=5, height=1,padx=4,font=('arial', 20, 'bold'), command=lambda: button_click(3))
button_4 = Button(Window, text="4", width=5, height=1,padx=4,font=('arial', 20, 'bold'), command=lambda: button_click(4))
button_5 = Button(Window, text="5", width=5, height=1,padx=4,font=('arial', 20, 'bold'), command=lambda: button_click(5))
button_6 = Button(Window, text="6", width=5, height=1,padx=4,font=('arial', 20, 'bold'), command=lambda: button_click(6))
button_7 = Button(Window, text="7", width=5, height=1,padx=4,font=('arial', 20, 'bold'), command=lambda: button_click(7))
button_8 = Button(Window, text="8", width=5, height=1,padx=4, font=('arial', 20, 'bold'), command=lambda: button_click(8))
button_9 = Button(Window, text="9", width=5, height=1,padx=4,font=('arial', 20, 'bold'), command=lambda: button_click(9))
button_0 = Button(Window, text="0", width=8, height=1,font=('arial', 20, 'bold'), command=lambda: button_click(0))
button_Divide = Button(Window, text="/", width=5, height=1, padx=4, pady=2, font=('arial', 20, 'bold'), command=lambda: button_click("/"))
button_Multiply = Button(Window, text="*", width=5, height=1, padx=4,pady=2, font=('arial', 20, 'bold'), command=lambda: button_click("*"))
button_Addition = Button(Window, text="+", width=8, height=1,font=('arial', 20, 'bold'), command=lambda: button_click("+"))
button_Subtraction = Button(Window, text="-", width=5, height=1, padx=4,font=('arial', 20, 'bold'), command=lambda: button_click("-"))
button_Decimal = Button(Window, text=".", padx=46, height=1,font=('arial', 20, 'bold'), command=lambda: button_click("."))
button_Equal = Button(Window, text="=", padx=170, height=1,font=('arial', 20, 'bold'), command=button_equal)



# adjust the button to their places
button_C.grid(row=1, column=0, columnspan=4, ipadx=33, ipady=5, padx=2, pady=3)

button_1.grid(row=5, column=0, ipadx=5, ipady=2, padx=1, pady=3)
button_2.grid(row=5, column=1, ipadx=5, ipady=2)
button_3.grid(row=5, column=2, ipadx=5, ipady=2)
button_Subtraction.grid(row=5, column=3, ipadx=5, ipady=2, padx=1, pady=3)

button_4.grid(row=4, column=0, ipadx=5, ipady=2, padx=1, pady=3)
button_5.grid(row=4, column=1, ipadx=5, ipady=2)
button_6.grid(row=4, column=2, ipadx=5, ipady=2)
button_Multiply.grid(row=4, column=3, ipadx=5, ipady=1, padx=1, pady=3)

button_7.grid(row=3, column=0, ipadx=5, ipady=2, padx=1, pady=3)
button_8.grid(row=3, column=1, ipadx=5, ipady=2)
button_9.grid(row=3, column=2, ipadx=5, ipady=2)
button_Divide.grid(row=3, column=3, ipadx=5, ipady=1, padx=1, pady=3)

button_0.grid(row=6, column=0, columnspan=2, ipadx=4, ipady=2, padx=2, pady=3, sticky=W)
button_Decimal.grid(row=6, column=1, columnspan=2, ipadx=5, ipady=2)
button_Addition.grid(row=6, column=2, columnspan=2, ipadx=5, ipady=2, padx=2, pady=3, sticky=E)

button_Equal.grid(row=7, column=0, columnspan=4, ipadx=33, ipady=5, padx=2, pady=3)



Window.mainloop()