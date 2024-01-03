from tkinter import *

class ZComboWriter:
    def __init__(self, root):
        self.root = root
        self.root.title("ZCombo Writer")
        self.index = 0
        self.lastmove = "DR"
        self.air = False
        # Move priority
        self.landpriority = {
            "L" : 2,
            "M" : 3,
            "j" : 4,
            "H" : 4,
            "S" : 4,
            "SD" : 0,
            "DR" : 0,
            "Spark": 0,
            "1" : 1,
            "2" : 1,
            "3" : 1,
            "4" : 1,
            "5" : 1,
            "6" : 1,
            "7" : 1,
            "8" : 1,
            "9" : 1
        }
        self.airpriority = {
            "L" : 2,
            "M" : 2,
            "2H" : 3,
            "j" : 3,
            "H" : 4,
            "SD" : 0,
            "DR" : 0,
            "Spark": 0,
            "1" : 1,
            "2" : 1,
            "3" : 1,
            "4" : 1,
            "5" : 1,
            "6" : 1,
            "7" : 1,
            "8" : 1,
            "9" : 1
        }            
          
        self.Combo = Entry(self.root, width=50, borderwidth=5)
        self.Combo.grid(row=0, column=1, columnspan=7, padx=10, pady=10)
        
        self.define_buttons()
        self.place_buttons()

    def enter_text(self, input):
        if self.air == False:
            if self.landpriority[input] < self.landpriority[self.lastmove]:
                self.Combo.insert(self.index, " > ")
                self.index += 3
        else:
            if self.airpriority[input] < self.airpriority[self.lastmove]:
                self.Combo.insert(self.index, " > ")
                self.index += 3
                
        
        if input == "SD" or input == "DR":
            self.Combo.insert(self.index, input + " > ")
            self.index += 5
        elif input == "Spark":
            self.Combo.insert(self.index, input + " > ")
            self.index += 8
        else:
            self.Combo.insert(self.index, input)
            self.index += 1
            
            
        self.lastmove = input
        
    def backspace(self):
        if self.index > 0:
            self.index -= 1
            self.Combo.delete(self.index, 'end')
                      
              
    def clear(self):
        self.index = 0
        self.Combo.delete(0, 'end')

    def define_buttons(self):
        # Movement
        self.btn1 = Button(self.root, text="1", padx=40, pady=20, command=lambda: self.enter_text("1"))
        self.btn2 = Button(self.root, text="2", padx=40, pady=20, command=lambda: self.enter_text("2"))
        self.btn3 = Button(self.root, text="3", padx=40, pady=20, command=lambda: self.enter_text("3"))
        self.btn4 = Button(self.root, text="4", padx=40, pady=20, command=lambda: self.enter_text("4"))
        self.btn5 = Button(self.root, text="5", padx=40, pady=20, command=lambda: self.enter_text("5"))
        self.btn6 = Button(self.root, text="6", padx=40, pady=20, command=lambda: self.enter_text("6"))
        self.btn7 = Button(self.root, text="7", padx=40, pady=20, command=lambda: self.enter_text("7"))
        self.btn8 = Button(self.root, text="8", padx=40, pady=20, command=lambda: self.enter_text("8"))
        self.btn9 = Button(self.root, text="9", padx=40, pady=20, command=lambda: self.enter_text("9"))
        
        # Face
        self.btnLight = Button(self.root, text="L", padx=40, pady=20, command=lambda: self.enter_text("L"))
        self.btnMedium = Button(self.root, text="M", padx=40, pady=20, command=lambda: self.enter_text("M"))
        self.btnHeavy = Button(self.root, text="H", padx=40, pady=20, command=lambda: self.enter_text("H"))
        self.btnSpecial = Button(self.root, text="S", padx=40, pady=20, command=lambda: self.enter_text("S"))
        self.btnSuperDash = Button(self.root, text="SD", padx=40, pady=20, command=lambda: self.enter_text("SD"))
        self.btnDragonRush = Button(self.root, text="DR", padx=40, pady=20, command=lambda: self.enter_text("DR"))
        self.btnSpark = Button(self.root, text="Spark", padx=40, pady=20, command=lambda: self.enter_text("Spark"))
        
        # Misc
        self.btnDelete = Button(self.root, text="←", padx=40, pady=20, command=self.backspace)
        self.btnClear = Button(self.root, text="Clear", padx=40, pady=20, command=self.clear)
        
    def place_buttons(self):
        # Place Movement Buttons
        self.btn1.grid(row=3, column=1)
        self.btn2.grid(row=3, column=2)
        self.btn3.grid(row=3, column=3)
        self.btn4.grid(row=2, column=1)
        self.btn5.grid(row=2, column=2)
        self.btn6.grid(row=2, column=3)
        self.btn7.grid(row=1, column=1)
        self.btn8.grid(row=1, column=2)
        self.btn9.grid(row=1, column=3)

        # Place Face Buttons
        self.btnLight.grid(row=1, column=7)
        self.btnMedium.grid(row=2, column=6)
        self.btnHeavy.grid(row=3, column=7)
        self.btnSpecial.grid(row=2, column=8)
        self.btnSuperDash.grid(row=1, column=8)
        self.btnDragonRush.grid(row=1, column=6)
        self.btnSpark.grid(row=3, column=8)
        
        # Place Misc Buttons
        self.btnDelete.grid(row=1, column=9)
        self.btnClear.grid(row=2, column=9)


if __name__ == "__main__":
    root = Tk()
    app = ZComboWriter(root)
    root.mainloop()