
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BIN CCOMILLAS COMA CSINCOMILLAS EQ FL FLOAT GE GT HEX INT LBRACKET LE LT NCIENTIFICA NULL OCT PUNTOS RBRACKET TR\n        program :  ajson\n                | empty\n        \n        ajson :  LBRACKET object RBRACKET\n              | LBRACKET RBRACKET\n                \n        \n        object : pair COMA object\n               | pair COMA\n               | pair\n        \n        pair : clave PUNTOS value\n        \n        clave : CCOMILLAS\n              | CSINCOMILLAS\n        \n        value : num\n              | TR \n              | FL \n              | NULL \n              | CCOMILLAS \n              | ajson \n              | comparation\n        \n        num : FLOAT\n            | INT\n            | NCIENTIFICA\n            | BIN\n            | OCT\n            | HEX\n        \n        comparation : num LT num\n                    | num LE num\n                    | num GT num\n                    | num GE num\n                    | num EQ num\n        \n        empty : \n        '
    
_lr_action_items = {'LBRACKET':([0,13,],[4,4,]),'$end':([0,1,2,3,6,11,],[-29,0,-1,-2,-4,-3,]),'RBRACKET':([4,5,6,7,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,35,36,37,38,],[6,11,-4,-7,-3,-6,-5,-8,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'CCOMILLAS':([4,12,13,],[9,9,20,]),'CSINCOMILLAS':([4,12,],[10,10,]),'COMA':([6,7,11,15,16,17,18,19,20,21,22,23,24,25,26,27,28,34,35,36,37,38,],[-4,12,-3,-8,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'PUNTOS':([8,9,10,],[13,-9,-10,]),'TR':([13,],[17,]),'FL':([13,],[18,]),'NULL':([13,],[19,]),'FLOAT':([13,29,30,31,32,33,],[23,23,23,23,23,23,]),'INT':([13,29,30,31,32,33,],[24,24,24,24,24,24,]),'NCIENTIFICA':([13,29,30,31,32,33,],[25,25,25,25,25,25,]),'BIN':([13,29,30,31,32,33,],[26,26,26,26,26,26,]),'OCT':([13,29,30,31,32,33,],[27,27,27,27,27,27,]),'HEX':([13,29,30,31,32,33,],[28,28,28,28,28,28,]),'LT':([16,23,24,25,26,27,28,],[29,-18,-19,-20,-21,-22,-23,]),'LE':([16,23,24,25,26,27,28,],[30,-18,-19,-20,-21,-22,-23,]),'GT':([16,23,24,25,26,27,28,],[31,-18,-19,-20,-21,-22,-23,]),'GE':([16,23,24,25,26,27,28,],[32,-18,-19,-20,-21,-22,-23,]),'EQ':([16,23,24,25,26,27,28,],[33,-18,-19,-20,-21,-22,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'ajson':([0,13,],[2,21,]),'empty':([0,],[3,]),'object':([4,12,],[5,14,]),'pair':([4,12,],[7,7,]),'clave':([4,12,],[8,8,]),'value':([13,],[15,]),'num':([13,29,30,31,32,33,],[16,34,35,36,37,38,]),'comparation':([13,],[22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> ajson','program',1,'p_program','parser_class.py',14),
  ('program -> empty','program',1,'p_program','parser_class.py',15),
  ('ajson -> LBRACKET object RBRACKET','ajson',3,'p_ajson','parser_class.py',23),
  ('ajson -> LBRACKET RBRACKET','ajson',2,'p_ajson','parser_class.py',24),
  ('object -> pair COMA object','object',3,'p_object','parser_class.py',31),
  ('object -> pair COMA','object',2,'p_object','parser_class.py',32),
  ('object -> pair','object',1,'p_object','parser_class.py',33),
  ('pair -> clave PUNTOS value','pair',3,'p_pair','parser_class.py',38),
  ('clave -> CCOMILLAS','clave',1,'p_clave','parser_class.py',46),
  ('clave -> CSINCOMILLAS','clave',1,'p_clave','parser_class.py',47),
  ('value -> num','value',1,'p_value','parser_class.py',53),
  ('value -> TR','value',1,'p_value','parser_class.py',54),
  ('value -> FL','value',1,'p_value','parser_class.py',55),
  ('value -> NULL','value',1,'p_value','parser_class.py',56),
  ('value -> CCOMILLAS','value',1,'p_value','parser_class.py',57),
  ('value -> ajson','value',1,'p_value','parser_class.py',58),
  ('value -> comparation','value',1,'p_value','parser_class.py',59),
  ('num -> FLOAT','num',1,'p_num','parser_class.py',66),
  ('num -> INT','num',1,'p_num','parser_class.py',67),
  ('num -> NCIENTIFICA','num',1,'p_num','parser_class.py',68),
  ('num -> BIN','num',1,'p_num','parser_class.py',69),
  ('num -> OCT','num',1,'p_num','parser_class.py',70),
  ('num -> HEX','num',1,'p_num','parser_class.py',71),
  ('comparation -> num LT num','comparation',3,'p_comparation','parser_class.py',78),
  ('comparation -> num LE num','comparation',3,'p_comparation','parser_class.py',79),
  ('comparation -> num GT num','comparation',3,'p_comparation','parser_class.py',80),
  ('comparation -> num GE num','comparation',3,'p_comparation','parser_class.py',81),
  ('comparation -> num EQ num','comparation',3,'p_comparation','parser_class.py',82),
  ('empty -> <empty>','empty',0,'p_empty','parser_class.py',98),
]
