import re

# Expresión regular para cadenas entre comillas dobles
string_regex = r'\-*\d*\.\d+'

# Prueba
test_string = '-12.3 12.3 "Hola, mundo!", "123", "", "0b101", "Esto es una prueba" "hola",  "\n", 10e3, 1E-3, e, e-4, 12e, 0x13, 0XBA, 0Xt'
matches = re.findall(string_regex, test_string)

print(matches)  # ['"Hola, mundo!"', '"123"', '""', '"0b101"', '"Esto es una prueba"']
