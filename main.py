import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x600")
        self.initialize_gui()

    def verify(self):
        
        if not "" in self.dic_butons.values():
            messagebox.showinfo(title="The end",message= "this is a draw ")
            self.destroy()

        if self.dic_butons[0] == "X" and self.dic_butons[1] == "X" and self.dic_butons[2] == "X":
            messagebox.showinfo(title="The end",message= "I win the X" )
            self.destroy()

        elif self.dic_butons[3] == "X" and self.dic_butons[4] == "X" and self.dic_butons[5] == "X":
            messagebox.showinfo(title="The end",message= "I win the X")
            self.destroy()  

        elif self.dic_butons[6] == "X" and self.dic_butons[7] == "X" and self.dic_butons[8] == "X":
            messagebox.showinfo(title="The end",message= "I win the X" )
            self.destroy()    

        elif self.dic_butons[0] == "X" and self.dic_butons[3] == "X" and self.dic_butons[6] == "X":
            messagebox.showinfo(title="The end",message= "I win the X" )
            self.destroy()    

        elif self.dic_butons[1] == "X" and self.dic_butons[4] == "X" and self.dic_butons[7] == "X":
            messagebox.showinfo(title="The end",message= "I win the X")
            self.destroy()

        elif self.dic_butons[2] == "X" and self.dic_butons[5] == "X" and self.dic_butons[8] == "X":
            messagebox.showinfo(title="The end",message= "I win the X" )
            self.destroy()

        elif self.dic_butons[0] == "X" and self.dic_butons[4] == "X" and self.dic_butons[8] == "X":
            messagebox.showinfo(title="The end",message= "I win the X")
            self.destroy()

        elif self.dic_butons[2] == "X" and self.dic_butons[4] == "X" and self.dic_butons[6] == "X":
            messagebox.showinfo(title="The end",message= "I win the X")
            self.destroy()



        if self.dic_butons[0] == "O" and self.dic_butons[1] == "O" and self.dic_butons[2] == "O":
            messagebox.showinfo(title="The end",message= "I win the O")
            self.destroy()

        elif self.dic_butons[3] == "O" and self.dic_butons[4] == "O" and self.dic_butons[5] == "O":
            messagebox.showinfo(title="The end",message= "I win the O" )
            self.destroy()  

        elif self.dic_butons[6] == "O" and self.dic_butons[7] == "O" and self.dic_butons[8] == "O":
            messagebox.showinfo(title="The end",message= "I win the O" )
            self.destroy()    

        elif self.dic_butons[0] == "O" and self.dic_butons[3] == "O" and self.dic_butons[6] == "O":
            messagebox.showinfo(title="The end",message= "I win the O" )
            self.destroy()    

        elif self.dic_butons[1] == "O" and self.dic_butons[4] == "O" and self.dic_butons[7] == "O":
            messagebox.showinfo(title="The end",message= "I win the O")
            self.destroy()

        elif self.dic_butons[2] == "O" and self.dic_butons[5] == "O" and self.dic_butons[8] == "O":
            messagebox.showinfo(title="The end",message= "I win the O" )
            self.destroy()

        elif self.dic_butons[0] == "O" and self.dic_butons[4] == "O" and self.dic_butons[8] == "O":
            messagebox.showinfo(title="The end",message= "I win the O" )
            self.destroy()

        elif self.dic_butons[2] == "O" and self.dic_butons[4] == "O" and self.dic_butons[6] == "O":
            messagebox.showinfo(title="The end",message= "I win the O")
            self.destroy()


    def pulse(self,identifier):
        idd = self.label_indicator.cget("text")
        self.list_butons[identifier].configure(state = "disabled")
        
        if idd == "O":
            self.label_indicator.configure(text = "X")
            self.list_butons[identifier].configure(text = idd)
            
            self.dic_butons[identifier] = idd
            self.verify()
        
        else:
            self.label_indicator.configure(text = "O")
            self.list_butons[identifier].configure(text = idd)
            
            self.dic_butons[identifier] = idd
            self.verify()

    def initialize_gui(self):
        self.list_butons = []
        self.dic_butons = {0:"", 1:"", 2:"", 3:"" ,4:""
        ,5:"" ,6:"" ,7:"" ,8:""}

        self.boton_one = ctk.CTkButton(self,text="1",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(0))
        self.boton_one.grid(row=0, column=0, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_one)

        self.boton_two = ctk.CTkButton(self,text="2",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(1))
        self.boton_two.grid(row=0, column=1, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_two)

        self.boton_three = ctk.CTkButton(self,text="3",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(2))
        self.boton_three.grid(row=0, column=2, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_three)

        self.boton_four = ctk.CTkButton(self,text="4",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(3))
        self.boton_four.grid(row=2, column=0, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_four)

        self.boton_five= ctk.CTkButton(self,text="5",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(4))
        self.boton_five.grid(row=2, column=1, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_five)

        self.boton_six= ctk.CTkButton(self,text="6",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(5))
        self.boton_six.grid(row=2, column=2, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_six)

        self.boton_seven= ctk.CTkButton(self,text="7",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(6))
        self.boton_seven.grid(row=4, column=0, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_seven)

        self.boton_eight= ctk.CTkButton(self,text="8",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(7))
        self.boton_eight.grid(row=4, column=1, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_eight)

        self.boton_nine = ctk.CTkButton(self,text="9",font=("Arial",18),width=80,height=80,command= lambda:self.pulse(8))
        self.boton_nine.grid(row=4, column=2, padx=(10, 5), pady=10, sticky=ctk.W)
        self.list_butons.append(self.boton_nine)

        self.label_indicator = ctk.CTkLabel(self,text = "X",font = ("Arial",60))
        self.label_indicator.grid(row = 25,column =0,padx=(10, 5), pady=10)



window = App()
window.mainloop()