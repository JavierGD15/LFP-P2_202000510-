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

class Token_Error_sintactico(Token):
    def __init__(self, descripcion, tipo, fila, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna        

class opcionesD:
    def __init__(self, semestre, codigo, nombres,prerrequisitos):
        self.semestre = semestre
        self.codigo = codigo
        self.nombres = nombres
        self.prerrequisitos = prerrequisitos

class opcionesB:
    def __init__(self, instruccion, cadena):
        self.instruccion = instruccion
        self.cadena = cadena

class opcionesC:
    def __init__(self, instruccion, numeros):
        self.instruccion = instruccion
        self.numeros = numeros