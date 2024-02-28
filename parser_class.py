import ply.yacc as yacc
from lexer_class import LexerClass

class ParserClass:
    tokens = LexerClass.tokens

    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.lexer = LexerClass().lexer