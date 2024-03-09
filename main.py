import sys
from ajson_lexer import LexerClass
from ajson_parser import ParserClass

#l = LexerClass()
#l.test_with_file(sys.argv[1])
if len(sys.argv)==2:
    p = ParserClass()
    p.test_with_file(sys.argv[1])

elif sys.argv[2] == "lexer":
    l = LexerClass()
    l.test_with_file(sys.argv[1])

