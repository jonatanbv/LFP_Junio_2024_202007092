from enum import Enum
from dataclasses import dataclass, field
from tokens import Token
from errores import Error

class Estado(Enum):
    INICIAL = 0
    IDENTIFICADOR = 1
    ASIGNACION = 2
    STRING = 3
    SIGNO = 4
    ACEPTACION = 20
    PUNTO = 5
    TRES_PUNTOS = 6

@dataclass
class Lexer:
    entrada: str
    tokens: list = field(default_factory=list)
    errores: list = field(default_factory=list)

    def isCaracterValido(self, caracter):
        return caracter in [';', '[', ']', ':', ',', '{', '}', '>', '.']

    def estado0(self, caracter, linea, columna):
        if caracter.isalpha():
            return Estado.IDENTIFICADOR
        elif caracter == "-":
            return Estado.ASIGNACION
        elif caracter == "'":
            return Estado.STRING
        elif self.isCaracterValido(caracter):
            return Estado.SIGNO
        elif caracter == '.':
            return Estado.PUNTO
        elif ord(caracter) in (32, 10, 9):
            return Estado.INICIAL
        else:
            self.errores.append(Error("N/A", "N/A", linea, columna, caracter))
            return Estado.INICIAL

    def analizar(self):
        linea, columna = 1, 1
        lexema = ""
        estado = Estado.INICIAL
        estado_anterior = Estado.INICIAL

        for caracter in self.entrada:
            
            if estado == Estado.INICIAL:
                estado = self.estado0(caracter, linea, columna)
                if estado != Estado.INICIAL:
                    lexema += caracter

            elif estado == Estado.IDENTIFICADOR:
                if caracter.isalpha():
                    lexema += caracter
                else:
                    if lexema in ["nombre", "nodos", "conexiones"]:
                        self.tokens.append(Token("Palabra reservada", lexema, linea, columna - len(lexema)))
                    else:
                        self.errores.append(Error("Simbolo incorrecto", lexema, linea, columna, "N/A"))
                    lexema = ""
                    estado = self.estado0(caracter, linea, columna)
                    if estado != Estado.INICIAL:
                        lexema += caracter

            elif estado == Estado.ASIGNACION:
                if caracter == ">":
                    lexema += caracter
                    estado = Estado.ACEPTACION
                    estado_anterior = Estado.ASIGNACION
                else:
                    self.errores.append(Error("Asignación", lexema, linea, columna, caracter))
                    estado = Estado.INICIAL
                    lexema = ""
                    
            elif estado == Estado.PUNTO:
                if caracter == '.':
                    estado = Estado.TRES_PUNTOS
                    lexema += caracter
                else:
                    self.errores.append(Error("Punto", lexema, linea, columna, caracter))
                    estado = Estado.INICIAL
                    lexema = ""

            elif estado == Estado.TRES_PUNTOS:
                if caracter == '.':
                    lexema += caracter
                    self.tokens.append(Token("Tres puntos", lexema, linea, columna - len(lexema) + 1))
                    estado = Estado.INICIAL
                    lexema = ""
                else:
                    self.errores.append(Error("Tres puntos", lexema, linea, columna, caracter))
                    estado = Estado.INICIAL
                    lexema = ""

            elif estado == Estado.STRING:
                if caracter == "'":
                    lexema += caracter
                    estado = Estado.ACEPTACION
                    estado_anterior = Estado.STRING
                elif caracter == "\n":
                    self.errores.append(Error("String", lexema, linea, columna, caracter))
                    estado = Estado.INICIAL
                    lexema = ""
                
                else:
                    lexema += caracter

            elif estado == Estado.SIGNO:
                self.tokens.append(Token("Signo", lexema, linea, columna - len(lexema)))
                lexema = ""
                estado = self.estado0(caracter, linea, columna)
                if estado != Estado.INICIAL:
                    lexema += caracter

            elif estado == Estado.ACEPTACION:
                if estado_anterior == Estado.ASIGNACION:
                    self.tokens.append(Token("Asignación", lexema, linea, columna - len(lexema)))
                elif estado_anterior == Estado.STRING:
                    self.tokens.append(Token("String", lexema, linea, columna - len(lexema)))
                lexema = ""
                estado_anterior = Estado.INICIAL
                estado = self.estado0(caracter, linea, columna)
                if estado != Estado.INICIAL:
                    lexema += caracter

            if ord(caracter) == 10:
                linea += 1
                columna = 1
            elif ord(caracter) == 9:
                columna += 4
            else:
                columna += 1
