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
nombre = ""

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
    opcionesB.clear()
    opcionesC.clear()

    
    if a.listError == [] and a.listErrorSintactico == []:
        #agregamos la lista que vamos a crear

        for i in a.opcionesD:
            opcionesD.append((i.semestre, i.codigo, i.nombres, i.prerrequisitos))            
        for i in a.opcionesB:            
            opcionesB.append((i.instruccion, i.cadena))            
        for i in a.opcionesC:            
            opcionesC.append((i.instruccion, i.numeros))
        imprimir_opciones()    
    else:
        a.imprimir()
    
def imprimir_opciones():
    global caja1, caja2 
    caja2.delete("1.0",END)

    #pendiente si lo piden o no
    #caja2.insert(END,"*********************Cursos Agregados*********************")
    #for i in opcionesD:
        #caja2.insert(END, "Semestre: " + str(i[0]) + " Codigo: " + str(i[1]) + " Nombre: " + str(i[2]) + " Prerrequisitos: " + str(i[3]) + "\n")
        

    #caja2.insert(END,"**********************************************************")

    for i in opcionesB:
        if i[0] == "nombre_de_red":
            nombre = i[1]
        elif i[0] == "consola":
            caja2.insert(END, i[1])
        elif i[0] == "consolaln":
            caja2.insert(END,"\n"+i[1])
        elif i[0] == "cursoPorNombre":
            for x in opcionesD:
                if x[2] == i[1]:
                    caja2.insert(END,"\n"+ "Semestre: " + str(x[0]) + " Codigo: " + str(x[1]) + " Nombre: " + str(x[2]) + " Prerrequisitos: " + str(x[3]) + "\n")
        elif i[0] == "generarRed":
            caja2.insert(END,"\n"+"Generando Red...")
            generarRed()
            caja2.insert(END,"\n"+"Red Generada")
    
    for i in opcionesC:
        if i[0]=='cursoPorSemestre':
            caja2.insert(END,"************************Semestre"+i[1]+"*************************")
            for x in opcionesD:
                if x[0] == i[1]:
                    
                    caja2.insert(END,"\n"+ "Semestre: " + str(x[0]) + " Codigo: " + str(x[1]) + " Nombre: " + str(x[2]) + " Prerrequisitos: " + str(x[3]) + "\n")
        elif i[0]=='cursoPorCodigo':
            caja2.insert(END,"**********************************************************")
            for x in opcionesD:
                if x[1] == i[1]:
                    caja2.insert(END,"\n"+ "Semestre: " + str(x[0]) + " Codigo: " + str(x[1]) + " Nombre: " + str(x[2]) + " Prerrequisitos: " + str(x[3]) + "\n")
        elif i[0]=='cursosPostrrequisitos':
            caja2.insert(END,"**********************************************************")
            for x in opcionesD:
                for y in x[3]:
                    if y == i[1]:
                        caja2.insert(END,"\n"+ "Semestre: " + str(x[0]) + " Codigo: " + str(x[1]) + " Nombre: " + str(x[2]) + " Prerrequisitos: " + str(x[3]) + "\n")               
        elif i[0]=='cursoPrerrequisitos':
            caja2.insert(END,"**********************************************************")
            for x in opcionesD:
                if x[1] == i[1]:
                    caja2.insert(END,"\n"+ "Semestre: " + str(x[0]) + " Codigo: " + str(x[1]) + " Nombre: " + str(x[2]) + " Prerrequisitos: " + str(x[3]) + "\n")

        else:
            caja2.insert(END,"\n"+"Instruccion no reconocida")

def abrir (self):
    global caja1, caja2
    a = AnalizadorLexico()
    a.analizar(leerArchivo(self))
    a.analisisSintactico()
    semestre = 0
    codigo = 0
    nombre = ""
    prerrquisitos = []

            
def generarRed():
    global nombre
    print(nombre)
    pygame.init()
    pygame.display.set_caption(nombre)
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))
    pygame.display.flip()
    pygame.display.update()
    pygame.time.wait(1000)
    pygame.quit()



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
    ROOT.geometry("1030x600")
    APP = UI(parent=ROOT)
    carnet = Label(ROOT, text="Proyecto 2 - 202000510", font=("Arial Bold", 12))
    carnet.place(x=20, y=10)
    caja1 = Text(ROOT, width=65, height=30)
    caja1.place(x=20, y=100)
    caja2 = Text(ROOT, width=58, height=30)
    caja2.place(x=550, y=100)
    APP.mainloop()
    ROOT.destroy()
    
