import ply.lex as lex
import sys
"""
Errores: anotación cientifica
"""
reserved = ("TR", "FL", "NULL")

tokens = ("FLOAT" , "INT", "NCIENTIFICA", "BIN", "OCT", "HEX", "CCOMILLAS", "CSINCOMILLAS", "LBRACKET",
    'RBRACKET', 'LT','LE', 'GT', 'GE','EQ', "COMA", "PUNTOS") + reserved

reserved_map = {}
for r in reserved:
    reserved_map[r.upper()]= r
    reserved_map[r.lower()] = r

t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_COMA = r','
t_PUNTOS = r':'

def t_HEX(token):
    r"0[xX][0-9A-F]+"
    token.value = int(token.value, 16)  # Convierte a entero
    return token

def t_OCT(token):
    r"0[0-9]+"
    token.value = int(token.value, 8)  # Convierte a entero
    return token

def t_BIN(token):
    r'0[bB][01]+'
    token.value = int(token.value, 2)  # Convierte a entero
    return token


def t_NCIENTIFICA(token):
    r'\d+[eE]-*\d+'

    return token

def t_FLOAT(token):
    r'\-*\d*\.\d+'
    token.value = float(token.value)
    return token

def t_INT(token):
    r'\-*[1-9][0-9]*'
    token.value = int(token.value)
    return token
def t_CSINCOMILLAS(token):
    r'[A-Za-z_][A-Za-z_0-9]*'
    token.type = reserved_map.get(token.value.upper(), "CSINCOMILLAS")  # Check for reserved words
    return token

def t_CCOMILLAS(token):
    r'"[^"\n]*"'
    token.value = token.value[1:-1]  # Quita las comillas dobles
    return token

t_ignore = ' ' #para ignorar cualquier valor que coincida con el espacio vacío y con la tabulación
def t_newline(token):
    r'\n+' #el cambio de linea puede cambiar dependiendo del fichero por lo que hay que revisar el fichero
    token.lexer.lineno = token.value.count('\n') #aumenta la posicion del lexer en tantas unidades como saltos haya

def t_error(token):
    print("[Ex1][Lexer] Illegal character", token)
    token.lexer.skip(1) #se salta ese caracter

lexer = lex.lex()
file = open(sys.argv[1])
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)