from tkinter import *

global index

root = Tk()
root.title("ZCombo Writer")



e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=1, columnspan=7, padx=10, pady=10)

#e.insert(0, "")

def enter_button(input):
    e.insert(index, "L")
    index += 1
def button_add():
    return
    
    
# Buttons

# Define Movement Buttons

btn1 = Button(root, text="1", padx=40, pady=20, command=button_add)
btn2 = Button(root, text="2", padx=40, pady=20, command=button_add)
btn3 = Button(root, text="3", padx=40, pady=20, command=button_add)
btn4 = Button(root, text="4", padx=40, pady=20, command=button_add)
btn5 = Button(root, text="5", padx=40, pady=20, command=button_add)
btn6 = Button(root, text="6", padx=40, pady=20, command=button_add)
btn7 = Button(root, text="7", padx=40, pady=20, command=button_add)
btn8 = Button(root, text="8", padx=40, pady=20, command=button_add)
btn9 = Button(root, text="9", padx=40, pady=20, command=button_add)


#Define Face Buttons

btnLight = Button(root, text="L", padx=40, pady=20, command=enter_button("L"))
btnMedium = Button(root, text="M", padx=40, pady=20, command=enter_button("M"))
btnHeavy = Button(root, text="H", padx=40, pady=20, command=enter_button)
btnSpecial = Button(root, text="S", padx=40, pady=20, command=button_add)
btnSuperDash = Button(root, text="SD", padx=40, pady=20, command=button_add)
btnDragonRush = Button(root, text="DR", padx=40, pady=20, command=button_add)

#Place Movement Buttons

btn1.grid(row=3, column=1)
btn2.grid(row=3, column=2)
btn3.grid(row=3, column=3)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=1, column=1)
btn8.grid(row=1, column=2)
btn9.grid(row=1, column=3)

#Place Face Buttons

btnLight.grid(row=1, column=6)
btnMedium.grid(row=2, column=5)
btnHeavy.grid(row=3, column=6)
btnSpecial.grid(row=2, column=7)
btnSuperDash.grid(row=1, column=7)
btnDragonRush.grid(row=1, column=5)

#Run Loop

root.mainloop()