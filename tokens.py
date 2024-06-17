class Token:
    def __init__(self, nombre, lexema, linea, columna):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena.")
        if not isinstance(lexema, str):
            raise TypeError("El lexema debe ser una cadena.")
        if not isinstance(linea, int):
            raise TypeError("La línea debe ser un entero.")
        if not isinstance(columna, int):
            raise TypeError("La columna debe ser un entero.")
        
        self._nombre = nombre
        self._lexema = lexema
        self._linea = linea
        self._columna = columna

    def __str__(self):
        
        return f'nombre: {self._nombre}, tipo: {self._lexema}, (Linea: {self._linea}, Columna: {self._columna})'
    def nombre(self):
        return f'{self._nombre}'
    def lexema(self):
        return f'{self._lexema}'
    def fila(self):
        return f'{self._linea}'
    def columna(self):
        return f'{self._columna}'



