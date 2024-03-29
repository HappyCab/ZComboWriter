from tkinter import *
import pyperclip

WINDOW_XSIZE = "800"
WINDOW_YSIZE = "450"
WINDOW_RESOLUTION = WINDOW_XSIZE + "x" + WINDOW_YSIZE

class ZComboWriter:
    def __init__(self, root):
        self.root = root
        self.root.title("ZCombo Writer")
        self.root.geometry(WINDOW_RESOLUTION)
        self.index = 0
        self.history = []
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
        
        self.get_images()
        self.display_bg()
        self.place_textbox()
        self.define_buttons()
        self.place_buttons()

    def enter_text(self, input):
        self.Combo.insert(self.index, input)
        self.index += len(input)
        
        ##if self.air == False:
        ##    if self.landpriority[input] < self.landpriority[self.lastmove]:
        ##        self.Combo.insert(self.index, " > ")
        ##        self.index += 3
        ##else:
        ##    if self.airpriority[input] < self.airpriority[self.lastmove]:
        ##        self.Combo.insert(self.index, " > ")
        ##        self.index += 3
        ##        
        ##
        ##if input == "SD" or input == "DR":
        ##    self.Combo.insert(self.index, input + " > ")
        ##    self.index += 5
        ##elif input == "Spark":
        ##    self.Combo.insert(self.index, input + " > ")
        ##    self.index += 8
        ##else:
        ##    self.Combo.insert(self.index, input)
        ##    self.index += 1
            
            
        self.history.append(input)
        
    def backspace(self):
        if self.index > 0:
            self.index -= len(self.history[-1])
            self.Combo.delete(self.index, 'end')
                                 
    def clear(self):
        self.index = 0
        self.Combo.delete(0, 'end')
        self.history = []
        
    def copy(self):
        combotext = self.Combo.get()
        pyperclip.copy(combotext)
        
    def get_images(self):
        self.imgLight = PhotoImage(file="img/inputs/light.png")
        self.imgMedium = PhotoImage(file="img/inputs/medium.png")
        self.imgHeavy = PhotoImage(file="img/inputs/heavy.png")
        self.imgSpecial = PhotoImage(file="img/inputs/special.png")
        self.imgAssist1 = PhotoImage(file="img/inputs/assist1.png")
        self.imgAssist2 = PhotoImage(file="img/inputs/assist2.png")
        self.imgSpark = PhotoImage(file="img/inputs/spark.png")
        self.imgBg = PhotoImage(file="img/misc/background.png")
        
    def display_bg(self):
        background_label = Label(root, image=self.imgBg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
    def place_textbox(self):
        self.Combo = Entry(self.root, width=100, borderwidth=5, state= NORMAL)
        self.Combo.grid(row=0, column=1, columnspan=8, padx=10, pady=10)

    def define_buttons(self):
        # Movement
        self.btn1 = Button(self.root, text="1", padx=10, pady=10, command=lambda: self.enter_text("1"))
        self.btn2 = Button(self.root, text="2", padx=10, pady=10, command=lambda: self.enter_text("2"))
        self.btn3 = Button(self.root, text="3", padx=10, pady=10, command=lambda: self.enter_text("3"))
        self.btn4 = Button(self.root, text="4", padx=10, pady=10, command=lambda: self.enter_text("4"))
        self.btn5 = Button(self.root, text="5", padx=10, pady=10, command=lambda: self.enter_text("5"))
        self.btn6 = Button(self.root, text="6", padx=10, pady=10, command=lambda: self.enter_text("6"))
        self.btn7 = Button(self.root, text="7", padx=10, pady=10, command=lambda: self.enter_text("7"))
        self.btn8 = Button(self.root, text="8", padx=10, pady=10, command=lambda: self.enter_text("8"))
        self.btn9 = Button(self.root, text="9", padx=10, pady=10, command=lambda: self.enter_text("9"))
        self.btnJump = Button(self.root, text="Jump", width=10, pady=10, command=lambda: self.enter_text("j"))
        
        # Face
        self.btnLight = Button(self.root, image=self.imgLight, command=lambda: self.enter_text("L"))
        self.btnMedium = Button(self.root, image=self.imgMedium, command=lambda: self.enter_text("M"))
        self.btnHeavy = Button(self.root, image=self.imgHeavy, command=lambda: self.enter_text("H"))
        self.btnSpecial = Button(self.root, image=self.imgSpecial, command=lambda: self.enter_text("S"))
        
        # Assist
        self.btnAssist1 = Button(self.root, image=self.imgAssist1, background="white", command=lambda: self.enter_text("A1"))
        self.btnAssist2 = Button(self.root, image=self.imgAssist2, background="white", command=lambda: self.enter_text("A2"))
        
        # Combo
        self.btnSuperDash = Button(self.root, text="Super Dash", width=10, pady=10, command=lambda: self.enter_text("SD"))
        self.btnDragonRush = Button(self.root, text="Dragon Rush", width=10, pady=10, command=lambda: self.enter_text("DR"))
        self.btnSpark = Button(self.root, image=self.imgSpark, command=lambda: self.enter_text("Spark"))
        self.btnLevel1 =  Button(self.root, text="Level 1", width=10, pady=10, command=lambda: self.enter_text("LVL1"))   
        self.btnLevel2 =  Button(self.root, text="Level 2", width=10, pady=10, command=lambda: self.enter_text("LVL2"))  
        self.btnLevel3 =  Button(self.root, text="Level 3", width=10, pady=10, command=lambda: self.enter_text("LVL3"))
        
        # Misc
        self.btnDelete = Button(self.root, text="Backspace", width=10, pady=10, command=self.backspace)
        self.btnClear = Button(self.root, text="Clear", width=10, pady=10, command=self.clear)
        self.btnDivider = Button(self.root, text="Divider '>'", width=10, pady=10, command=lambda: self.enter_text(" > "))
        self.btnCopy = Button(self.root, text="Copy", width=10, command=self.copy)
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
        self.btnJump.grid(row=1, column=4)

        # Place Face Buttons
        self.btnLight.grid(row=2, column=6)
        self.btnMedium.grid(row=1, column=7)
        self.btnHeavy.grid(row=2, column=8)
        self.btnSpecial.grid(row=3, column=7)
        
        #Place Assist 
        self.btnAssist1.grid(row=1, column=6)
        self.btnAssist2.grid(row=1, column=8)
        
        # Place Combo Buttons
        self.btnSuperDash.grid(row=2, column=4, pady=50)
        self.btnDragonRush.grid(row=3, column=4)
        self.btnSpark.grid(row=2, column=7, pady=50)
        
        #Place Supers
        self.btnLevel1.grid(row=1, column=5)
        self.btnLevel2.grid(row=2, column=5)
        self.btnLevel3.grid(row=3, column=5)
               
        # Place Misc Buttons
        self.btnDelete.grid(row=1, column=9)
        self.btnClear.grid(row=2, column=9)
        self.btnDivider.grid(row=3, column=9)
        self.btnCopy.grid(row=0, column=9)


if __name__ == "__main__":
    root = Tk()
    app = ZComboWriter(root)
    root.mainloop()