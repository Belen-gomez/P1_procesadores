import ply.yacc as yacc
from ajson_lexer import LexerClass
import sys

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
        p[0] = p[1]
    


    def p_ajson(self, p):
        """
        ajson :  LBRACKET object RBRACKET
              | LBRACKET RBRACKET
                
        """
        if len(p) == 4:
            p[0] = p[2]
        

    def p_object(self, p):
        """
        object : pair COMA object
               | pair COMA
               | pair
        """
        if len(p) > 3:
            p[0] = {**p[1], **p[3]}
        else:
            p[0] = p[1]

    def p_pair(self, p):
        """
        pair : clave PUNTOS value
        """
        p[0] = {p[1]: p[3]}
        


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
              | array
        """
        if p[1] == "TR" or p[1] == "tr":
            p[0] = True
        elif p[1] == "FL" or p[1] == "fl":
            p[0] = False
        elif p[1] == "NULL" or p[1] == "null":
            p[0] = None
        else:
            p[0] = p[1]
    
    def p_array(self, p):
        """
        array : LCORCHETE array_values RCORCHETE
              | LCORCHETE RCORCHETE
        """
        if len(p) == 4:
            p[0] = p[2] 
    
    def p_array_values(self, p):
        """
        array_values : ajson COMA array_values
                     | ajson COMA
                     | ajson
        """
        if len(p) > 3:
            p[0] = [p[1]] + p[3]
        elif len(p) > 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]]

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
    
    def p_error(self, p):
        print("[parser] Parser error: "+ str(p) + " Valor: " + str(p.value)) # + p.value)
        
        
    
    def test(self, data):
        result = self.parser.parse(data)
        if not result:
            print(">> FICHERO AJSON VACIO " + str(sys.argv[1]))
        else:
            print(">> FICHERO AJSON " + str(sys.argv[1]))
            self.imprimir(result, prefix="")

    def imprimir(self, data, prefix=""):
        
        for key, value in data.items():
            new_key = f"{prefix}.{key}" if prefix else key
            if isinstance(value, dict):
                self.imprimir(value, new_key)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    self.imprimir(item, f"{new_key}.{i}")
            else:
                print("{ " + new_key + " : " + str(value) + " }")

    def test_with_file(self, path):
        file = open(path)
        content = file.read()
        self.test(content)