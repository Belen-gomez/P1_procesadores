import ply.lex as lex
import sys

class LexerClass:
    """
    Clase que define el lexer para el lenguaje ajson
    """
    reserved = ("TR", "FL", "NULL") #palabras reservadas

    tokens = ("FLOAT" , "INT", "NCIENTIFICA", "BIN", "OCT", "HEX", "CCOMILLAS", "CSINCOMILLAS", "LBRACKET",
        'RBRACKET', 'LCORCHETE', 'RCORCHETE', 'LT','LE', 'GT', 'GE','EQ', "COMA", "PUNTOS") + reserved  #tokens que se pueden usar

    def __init__(self):
        self.reserved_map = {}
        for r in self.reserved: #se añaden las palabras reservadas al mapa, tanto en mayusculas como en minusculas
            self.reserved_map[r.upper()] = r
            self.reserved_map[r.lower()] = r
        self.lexer = lex.lex(module=self)


    t_LBRACKET = r'\{'
    t_RBRACKET = r'\}'
    t_LCORCHETE = r'\['
    t_RCORCHETE = r'\]'
    t_LT = r'<'
    t_GT = r'>'
    t_LE = r'<='
    t_GE = r'>='
    t_EQ = r'=='
    t_COMA = r','
    t_PUNTOS = r':'

    def t_HEX(self, t):
        r"0[xX][0-9A-F]+"
        t.value = int(t.value, 16)  # Convierte a entero
        return t

    def t_OCT(self, t):
        r"0[0-9]+"
        t.value = int(t.value, 8)  # Convierte a entero
        return t

    def t_BIN(self, t):
        r'0[bB][01]+'
        t.value = int(t.value, 2)  # Convierte a entero
        return t

    def t_NCIENTIFICA(self, t):
        r'\d+[eE]-*\d+'
        t.value = float(t.value) # Convierte a float
        return t

    def t_FLOAT(self, t):
        r'\-*\d*\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\-*[1-9][0-9]*'
        t.value = int(t.value)
        return t

    def t_CSINCOMILLAS(self, t):
        r'[A-Za-z_][A-Za-z_0-9]*'
        t.type = self.reserved_map.get(t.value.upper(), "CSINCOMILLAS")  # Busca en el mapa de palabras reservadas
        return t

    def t_CCOMILLAS(self, t):
        r'"[^"\n]*"'
        t.value = t.value[1:-1]  # Quita las comillas dobles
        return t

    t_ignore = ' ' #para ignorar cualquier valor que coincida con el espacio vacío y con la tabulación
    def t_newline(self, t):
        r'\n+' #el cambio de linea puede cambiar dependiendo del fichero por lo que hay que revisar el fichero
        t.lexer.lineno += t.value.count('\n') #aumenta la posicion del lexer en tantas unidades como saltos haya

    def t_error(self, t):
        print("[Lexer] Illegal character", t)
        t.lexer.skip(1) #se salta ese caracter

    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token.type, token.value)

    def test_with_file(self, path):
        with open(path) as file:
            content = file.read()
            self.test(content)


