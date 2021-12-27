class Token:
    def __init__(self, lexema, tipo, fila, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getinfo (self):
        print("Lexema: " + self.lexema + " Tipo: " + self.tipo + " Fila: " + str(self.fila) + " Columna: " + str(self.columna))

class Token_Error(Token):
    def __init__(self, descripcion, tipo, fila, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        