from automata import AnalizadorLexico


def leerArchivo(ruta):
    archivo = open(ruta, "r")
    lineas = archivo.read()    
    return lineas

if __name__ == "__main__":
    a = AnalizadorLexico()
    a.analizar(leerArchivo("pruebas.lfp"))
    a.imprimir()
    a.analisisSintactico()