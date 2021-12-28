from automata import AnalizadorLexico
from tkinter import *
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from tkinter.font import BOLD 
from automata import AnalizadorLexico
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
import pygame
import random
import mutagen

opcionesB = []
opcionesC = []
opcionesD = []

def leerArchivo(self):   
    global caja1, caja2    
    direcion = filedialog.askopenfilename(initialdir ='/', 
											title='Escoger Tu archivo de entrada', 
										filetype=(('lfp files', '*.lfp*'),('All files', '*.*')))
    archivo = open(direcion, 'r')    
    lineas = archivo.read()  
    
    caja1.insert(END, lineas)

def analizar (self):
    a = AnalizadorLexico()
    a.analizar(caja1.get("1.0",END))
    a.analisisSintactico()
    
    if a.listError == [] and a.listErrorSintactico == []:
        print("No hay errores")        
    else:
        a.imprimir()
    

def abrir (self):
    global caja1, caja2
    a = AnalizadorLexico()
    a.analizar(leerArchivo(self))
    a.analisisSintactico()
    

    
    if a.listError == [] and a.listErrorSintactico == []:
        print("No hay errores")
    else:
        a.imprimir()   
            



class UI(Frame): 
    #"""Docstring.""" 
    def __init__(self, parent=None): 
        Frame.__init__(self, parent) 
        self.parent = parent 
        
        self.init_ui()

    def init_ui(self):
        a = AnalizadorLexico()
        #BOTONES
        boton_buscar = Button(self.parent, text="Abrir", command= lambda: abrir(self))
        boton_buscar.place(x=690,y=10)
        boton_analizar = Button(self.parent, text="Analizar", command= lambda: analizar(self))
        boton_analizar.place(x=770,y=10)
        boton_reportes = Button(self.parent, text="Reportes", command= lambda: abrir(self))
        boton_reportes.place(x=870,y=10)



if __name__ == "__main__":
    global caja1, caja2
    ROOT = Tk()
    ROOT.geometry("1000x600")
    APP = UI(parent=ROOT)
    carnet = Label(ROOT, text="Proyecto 2 - 202000510", font=("Arial Bold", 12))
    carnet.place(x=20, y=10)
    caja1 = Text(ROOT, width=80, height=30)
    caja1.place(x=20, y=100)
    caja2 = Text(ROOT, width=35, height=30, state=DISABLED)
    caja2.place(x=700, y=100)
    APP.mainloop()
    ROOT.destroy()
    
