from Token import Token
from Token import Token_Error, Token_Error_sintactico

class AnalizadorLexico:
    def __init__(self):
        self.listtoken = []
        self.listError = []
        self.listErrorSintactico = []

    def analizar(self, archivo):
        self.listtoken = []
        self.listError = []

        archivo += '@'
        linea = 1
        columna = 0
        indice = 0
        buffer = ""
        estado = 'A'

        while indice < len(archivo):
            caracter = archivo[indice]

            if estado == 'A':

                #Caracteres especiales
                if caracter == ';':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'PUNTOYCOMA', linea, columna))
                    buffer = ""                

                elif caracter == ':':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'DOSPUNTOS', linea, columna))
                    buffer = ""
                elif caracter == ',':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'COMA', linea, columna))
                    buffer = ""
                
                elif caracter == '[':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'CORCHETEIZQ', linea, columna))
                    buffer = ""
                elif caracter == ']':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'CORCHETEDER', linea, columna))
                    buffer = ""
                elif caracter == '(':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'PARENTESISIZQ', linea, columna))
                    buffer = ""
                elif caracter == ')':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'PARENTESISDER', linea, columna))
                    buffer = ""

                elif caracter == "'":
                    columna += 1
                    estado = 'C'

                #Palabras reservadas
                elif caracter.isalpha() and not caracter.isdigit():
                    buffer += caracter
                    columna += 1
                    estado = 'B'

                elif caracter.isdigit():
                    buffer += caracter
                    columna += 1
                    estado = 'D'

               #Espacios y enter
                elif caracter == '\n':
                        linea += 1
                        columna = 1
                        estado = 'A'
                elif caracter == ' ':
                        columna += 1
                        estado = 'A'
                elif caracter == '\t':
                        columna += 1
                        estado = 'A'

                #Caracter de finalización
                elif caracter == '@':
                    indice += 100
                else:
                    self.listError.append(Token_Error('Error lexico', caracter, linea, columna))
                    indice += 1


            #Analisis de palabras reservadas
            elif estado == 'B':
                if (caracter.isalpha() and not caracter.isnumeric()) or caracter == '_':
                    buffer += caracter
                    columna += 1
                    estado = 'B'
                else:
                    if buffer == 'nombre_de_red' or buffer == 'NOMBRE_DE_RED':                        

                        self.listtoken.append(Token(buffer,'Nombre de red', linea, columna))
                        estado = 'A'
                        buffer = ""    
                        indice -= 1                    

                    elif buffer == 'crearcurso' or buffer == 'CREARCURSO':                        

                        self.listtoken.append(Token(buffer,'Crear Curso', linea, columna))
                        estado = 'A'
                        buffer = ""
                        indice -= 1


                    elif buffer == 'consola' or buffer == 'CONSOLA':                        

                        self.listtoken.append(Token(buffer,'Consola', linea, columna))

                        estado = 'A'
                        buffer = ""
                        indice -= 1

                    elif buffer == 'consolaln' or buffer == 'CONSOLALN':                        

                        self.listtoken.append(Token(buffer,'Consolaln', linea, columna))

                        estado = 'A'
                        buffer = ""
                        indice -= 1

                    elif buffer == 'cursoPorSemestre' or buffer == 'CURSOPORSEMESTRE':                        

                        self.listtoken.append(Token(buffer,'cursoPorSemestre', linea, columna))

                        estado = 'A'
                        buffer = ""
                        indice -= 1

                    elif buffer == 'cursoPorCódigo' or buffer == 'CURSOPORCODIGO':                        

                        self.listtoken.append(Token(buffer,'cursoPorCódigo', linea, columna))

                        estado = 'A'
                        buffer = ""
                        indice -= 1

                    elif buffer == 'cursoPorNombre' or buffer == 'CURSOPORNOMBRE':                        

                        self.listtoken.append(Token(buffer,'cursoPorNombre', linea, columna))

                        estado = 'A'
                        buffer = ""
                        indice -= 1

                    elif buffer == 'cursoPrerrequisitos' or buffer == 'CURSOPREPRREQUISITOS':                        

                        self.listtoken.append(Token(buffer,'cursoPrerrequisitos', linea, columna))

                        estado = 'A'
                        buffer = ""
                        indice -= 1

                    elif buffer == 'cursosPostrrequisitos' or buffer == 'CURSOSPOSTREQUISITOS':                        

                        self.listtoken.append(Token(buffer,'cursosPostrrequisitos', linea, columna))

                        estado = 'A'
                        buffer = ""
                        indice -= 1

                    elif buffer == 'generarRed' or buffer == 'GENERARRED':                        

                        self.listtoken.append(Token(buffer,'generarRed', linea, columna))
                        estado = 'A'
                        buffer = ""   
                        indice -= 1                                                                 
                    
                    else:                        
                        self.listError.append(Token_Error(buffer + " No en lista de palabras reservadas",'ERROR TIPO LEXICO', linea, columna))                        
                        buffer = ""
                        estado = 'A'
                        indice -= 1
                    

            #Analisis de cadenas ''
            elif estado == 'C':
                if caracter == "'":                    
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'CADENA', linea, columna))
                    buffer = ""               

                else:
                    buffer += caracter
                    columna += 1
                    estado = 'C'

            #Analisis de numeros
            elif estado == 'D':
                if caracter.isdigit():
                    buffer += caracter
                    columna += 1
                    estado = 'D'
                else:
                    self.listtoken.append(Token(buffer,'NUMERO', linea, columna))
                    buffer = ""
                    estado = 'A'
                    indice -= 1
            indice += 1

    #Anlisis sintactico
    def analisisSintactico(self):
        
        estado = 'A'
        for i in self.listtoken:
            #Clasifiación B
            if i.lexema == 'nombre_de_red' or i.lexema == 'consola' or i.lexema == 'consolaln' or  i.lexema == 'cursoPorNombre'  or i.lexema == 'generarRed':
                estado = 'B'

            #Clasifiación C
            elif i.lexema == 'cursoPorSemestre' or i.lexema == 'cursoPorCódigo' or i.lexema == 'cursoPrerrequisitos' or i.lexema == 'cursosPostrrequisitos':
                estado = 'C'
            
            #Clasifiación D
            elif i.lexema == 'crearcurso':
                estado = 'D'
            
            #Analisis de estado B
            elif estado == 'B':
                if i.lexema == '(':
                    estado = 'B1'
                else:
                    self.listErrorSintactico.append(Token_Error_sintactico('Error sintactico', i.lexema, i.fila, i.columna))
                    break
            
            #Analisis de estado B1
            elif estado == 'B1':
                if i.lexema == "'":
                    estado = 'B2'
                else:
                    self.listErrorSintactico.append(Token_Error_sintactico('Error sintactico', i.lexema, i.fila, i.columna))
                    break
            elif estado == 'B2':
                if i.tipo == 'CADENA':
                    estado = 'B2'
                elif i.lexema == "'":
                    estado = 'B3'
                else:
                    self.listErrorSintactico.append(Token_Error_sintactico('Error sintactico', i.lexema, i.fila, i.columna))
                    break                
            elif estado == 'B3':
                if i.lexema == ')':
                    estado = 'B4'
                else:
                    self.listErrorSintactico.append(Token_Error_sintactico('Error sintactico', i.lexema, i.fila, i.columna))
                    break
            elif estado == 'B4':
                if i.lexema == ';':
                    estado = 'A'
                else:
                    self.listErrorSintactico.append(Token_Error_sintactico('Error sintactico', i.lexema, i.fila, i.columna))
                    break
        print("Errores Sintacticos:")
        for x in self.listErrorSintactico:
             print(x.descripcion, x.tipo, x.fila, x.columna)
                   


    def imprimir(self):
        print("Tokens:")
        for x in self.listtoken:
            print(x.tipo, x.lexema, x.fila, x.columna)
        print("Errores:")
        for x in self.listError:
             print(x.descripcion, x.tipo, x.fila, x.columna) 
