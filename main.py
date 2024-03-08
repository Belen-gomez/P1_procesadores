import sys
from lexer_class import LexerClass
from ajson_parser import ParserClass

#l = LexerClass()
#l.test_with_file(sys.argv[1])

p = ParserClass()
p.test_with_file(sys.argv[1])
