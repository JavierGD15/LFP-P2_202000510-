from automata import AnalizadorLexico
from tkinter import *
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from tkinter.font import BOLD 
from automata import AnalizadorLexico
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
import os

opcionesB = []
opcionesC = []
opcionesD = []
nombre1 = ""

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
    global caja1, caja2,nombre1
    caja2.delete("1.0",END)

    #pendiente si lo piden o no
    #caja2.insert(END,"*********************Cursos Agregados*********************")
    #for i in opcionesD:
        #caja2.insert(END, "Semestre: " + str(i[0]) + " Codigo: " + str(i[1]) + " Nombre: " + str(i[2]) + " Prerrequisitos: " + str(i[3]) + "\n")
        

    #caja2.insert(END,"**********************************************************")

    for i in opcionesB:
        if i[0] == "nombre_de_red":
            nombre1 = i[1]
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
            print(i[1])
            generarRed(i[1])
            
    
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


    

def generarRed(nombre):
    global nombre1,caja2
    g = open(nombre, "w")   
    if opcionesD != []:
        g.write("digraph G{\n")
        g.write('rankdir="LR"\n')
        g.write('label="'+nombre+'"')
        g.write("node[shape=record, style=filled]\n")
        for i in opcionesD:
            g.write("\"" + str(i[1]) + "\"" + "[label=\"" +"Codigo: "+ str(i[1])+"|"+"Nombre: "+ str(i[2]) + "\"]\n")
        for i in opcionesD:
            for j in i[3]:
                g.write("\"" + str(j) + "\"" + "->" + "\"" + str(i[1]) + "\"" + "\n")
        g.write("}")
        g.close()
        os.system("dot -Tpng " + nombre1 + " -o " + nombre1 + ".png")
        os.system("start " + nombre1 + ".png")
        caja2.insert(END,"\n"+"Red Generada")
      
        
    else:
        caja2.insert(END,"\n"+"No hay cursos para generar")


def arbol(self):
    a = AnalizadorLexico()
    a.analizar(caja1.get("1.0",END))
    a.analisisSintactico()
    




class UI(Frame): 
    #"""Docstring.""" 
    def __init__(self, parent=None): 
        Frame.__init__(self, parent) 
        self.parent = parent 
        self.parent.title("Generador de Mallas Curriculares")
        self.init_ui()

    def init_ui(self):
        a = AnalizadorLexico()
        #BOTONES
        boton_buscar = Button(self.parent, text="Abrir", command= lambda: abrir(self))
        boton_buscar.place(x=690,y=10)
        boton_analizar = Button(self.parent, text="Analizar", command= lambda: analizar(self))
        boton_analizar.place(x=770,y=10)
        boton_reportes = Button(self.parent, text="Reportes", command= lambda: imprimirReportes())
        boton_reportes.place(x=870,y=10)

def imprimirReportes():
    #guardar tokens en pdf
    global caja1, caja2
    caja2.insert(END,"\n"+"Generando PDF...")
    
    a = AnalizadorLexico()
    a.analizar(caja1.get("1.0",END))
    a.analisisSintactico()
 
    
#Generacion de reportes Lexicos
    g = open("reporteErrores.html", "w")
    
    
    mensaje  = '<html><head><title>Reporte de Errores</title></head><body><table border="1"><tr><th>Linea</th><th>Columna</th><th>Descripcion</th><th>Tipo</th></tr>'
    g.write(mensaje)
    cuerpo = ""
    fin = "</head></body></html>"

    for i in a.listError:
        cuerpo += "<tr><td>" + str(i.fila) + "</td><td>" + str(i.columna) + "</td><td>" + str(i.descripcion) + "</td><td>" + str(i.tipo) +"</td></tr>"
        
        g.write(cuerpo)
    g.write(fin)
    g.close()

#Generacion de reportes sintacticos
    g = open("reporteErroresSintácticos.html", "w")
    
    
    mensaje  = '<html><head><title>Reporte de Errores Sintácticos</title></head><body><table border="1"><tr><th>Fila</th><th>Columna</th><th>Descripcion</th><th>Tipo</th></tr>'
    g.write(mensaje)
    cuerpo = ""
    fin = "</head></body></html>"

    for i in a.listErrorSintactico:
        cuerpo += "<tr><td>" + str(i.fila) + "</td><td>" + str(i.columna) + "</td><td>" + str(i.descripcion) + "</td><td>" + str(i.tipo) +"</td></tr>"
        
        g.write(cuerpo)
    g.write(fin)
    g.close()

#Generacion de tokens
    g = open("reporteTokens.html", "w")
    
    
    mensaje  = '<html><head><title>Reporte de Tokens</title></head><body><table border="1"><tr><th>Fila</th><th>Columna</th><th>Lexema</th><th>Tipo</th></tr>'
    g.write(mensaje)
    cuerpo = ""
    fin = "</head></body></html>"

    for i in a.listtoken:
        cuerpo = "<tr><td>" + str(i.fila) + "</td><td>" + str(i.columna) + "</td><td>" + str(i.lexema) + "</td><td>" + str(i.tipo) +"</td></tr>"
        print(i.tipo, i.lexema, i.fila, i.columna)
        g.write(cuerpo)
    g.write(fin)
    g.close()
    caja2.insert(END,"\n"+"Generado con exito")

if __name__ == "__main__":
    global caja1, caja2
    ROOT = Tk()
    ROOT.geometry("1030x600")
    APP = UI(parent=ROOT)
    carnet = Label(ROOT, text="Proyecto 2 - 202000510", font=("Arial Bold", 12))
    carnet.place(x=20, y=10)
    ingresar = Label(ROOT, text="Ingrese el código que desea analizar:", font=("Arial Bold", 12))
    ingresar.place(x=20, y=75)
    resultado = Label(ROOT, text="Resultado:", font=("Arial Bold", 12))
    resultado.place(x=750, y=75)
    

    caja1 = Text(ROOT, width=65, height=30)
    caja1.place(x=20, y=100)
    caja2 = Text(ROOT, width=58, height=30)
    caja2.place(x=550, y=100)
    APP.mainloop()
    ROOT.destroy()
    
