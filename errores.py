from dataclasses import dataclass

@dataclass
class Error:
    token: str
    lexema: str
    linea: int
    columna: int
    caracter: str

    def __post_init__(self):
        """
        Realiza validaciones y ajustes después de la inicialización de los atributos.
        """
        if not isinstance(self.token, str):
            raise TypeError("El token debe ser una cadena.")
        if not isinstance(self.lexema, str):
            raise TypeError("El lexema debe ser una cadena.")
        if not isinstance(self.linea, int):
            raise TypeError("La línea debe ser un entero.")
        if not isinstance(self.columna, int):
            raise TypeError("La columna debe ser un entero.")
        if not isinstance(self.caracter, str):
            raise TypeError("El carácter debe ser una cadena.")

        if self.caracter == " ":
            self.caracter = "Espacio en blanco"

    def toke(self):
        return f'{self.token}'
    def lex(self):
        return f'{self.lexema}'
    def fila(self):
        return f'{self.linea}'
    def colum(self):
        return f'{self.columna}'
    def carac(self):
        return f'{self.caracter}'

    def __str__(self):
        return f'Error: {self.token}, caracter: {self.lexema}, fila: ({self.linea},  columna: {self.columna}), caracter: {self.caracter}'
    
