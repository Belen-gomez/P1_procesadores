import ply.yacc as yacc
from lexer_class import LexerClass

class ParserClass:
    tokens = LexerClass.tokens

    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.lexer = LexerClass().lexer

    
    def p_program(self, p):
        """
        program :  ajson
                | empty
        """




    def p_ajson(self, p):
        """
        ajson :  LBRACKET object RBRACKET
              | LBRACKET RBRACKET
                
        """
        if len(p) == 4:
            pass
        

    def p_object(self, p):
        """
        object : pair COMA object
               | pair COMA
               | pair
        """

    def p_pair(self, p):
        """
        pair : clave PUNTOS value
        """
        p[0] = p[1] + " : " + str(p[3])
        print("{ " + p[0] + " }")


    def p_clave(self, p):
        """
        clave : CCOMILLAS
              | CSINCOMILLAS
        """
        p[0] = p[1]

    def p_value(self, p):
        """
        value : num
              | TR 
              | FL 
              | NULL 
              | CCOMILLAS 
              | ajson 
              | comparation
        """
        p[0] = p[1]
      

    def p_num(self, p):
        """
        num : FLOAT
            | INT
            | NCIENTIFICA
            | BIN
            | OCT
            | HEX
        """
        p[0] = p[1]

    
    def p_comparation(self, p):
        """
        comparation : num LT num
                    | num LE num
                    | num GT num
                    | num GE num
                    | num EQ num
        """
        if p[2] == "<":
            p[0] = p[1] < p[3]
        elif p[2] == "<=":
            p[0] = p[1] <= p[3]
        elif p[2] == ">":
            p[0] = p[1] > p[3]
        elif p[2] == ">=":
            p[0] = p[1] >= p[3]
        elif p[2] == "=":
            p[0] = p[1] == p[3]
        

    def p_empty(self, p):
        """
        empty : 
        """
        pass

    def test(self, data):
        self.parser.parse(data)

    def test_with_file(self, path):
        file = open(path)
        content = file.read()
        self.test(content)