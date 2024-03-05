import sys
from lexer_class import LexerClass
from parser_class import ParserClass

#l = LexerClass()
#l.test_with_file(sys.argv[1])

p = ParserClass()
p.test_with_file(sys.argv[1])
