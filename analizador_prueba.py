import re

# Definir los patrones de los tokens
TOKEN_SPECIFICATION = [
    ('NUMBER',    r'\d+(\.\d*)?'),  # Números enteros o decimales
    ('IDENTIFIER',r'[A-Za-z_]\w*'), # Identificadores
    ('OP',        r'[+\-*/=]'),     # Operadores aritméticos
    ('NEWLINE',   r'\n'),           # Saltos de línea
    ('SKIP',      r'[ \t]+'),       # Espacios en blanco y tabulaciones
    ('MISMATCH',  r'.'),            # Cualquier otro carácter
]

# Crear el patrón de expresión regular para el lexer
token_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECIFICATION)

class Lexer:
    def __init__(self, code):
        self.code = code
        self.line_num = 1
        self.line_start = 0
        self.tokens = self.tokenize()

    def tokenize(self):
        tokens = []
        for mo in re.finditer(token_regex, self.code):
            kind = mo.lastgroup
            value = mo.group(kind)
            column = mo.start() - self.line_start
            if kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)
            elif kind == 'NEWLINE':
                self.line_num += 1
                self.line_start = mo.end()
                continue
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value} inesperado en la línea {self.line_num}')
            tokens.append((kind, value, self.line_num, column))
        return tokens

    def __iter__(self):
        return iter(self.tokens)

# Código de ejemplo
code = '''
x = 42;
y = x + 3.14
'''

lexer = Lexer(code)
for token in lexer:
    print(token)
