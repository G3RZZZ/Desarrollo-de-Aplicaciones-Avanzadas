
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA CONNECT DIVIDE DOT EXP FUNCTION LBRACE LPAREN MINUS NUMBER PLUS RBRACE RPAREN SEMI SETTO STRING TIMES VARIABLE newline\n    top_level : top_level_expr\n              | top_level_expr top_level\n    \n    top_level_expr : assignment newline\n              | function_definition newline\n              | expression newline\n    \n    assignment : VARIABLE SETTO expression\n    \n    assignment : VARIABLE SETTO flow\n    \n    flow : VARIABLE CONNECT flow_functions\n    \n    flow_functions : flow_function_call CONNECT flow_functions\n    \n    flow_functions : flow_function_call\n    \n    flow_function_call : VARIABLE DOT LPAREN params RPAREN\n    \n    assignment : expression\n    \n    expression : expression PLUS term\n    \n    expression : expression MINUS term\n    \n    expression : term \n            | string\n    \n    string : STRING\n    \n    term : term TIMES exponent\n    \n        term : term DIVIDE exponent\n    \n    term : exponent\n    \n    exponent : factor EXP factor\n    \n    exponent : factor\n    \n    exponent : LPAREN expression RPAREN\n    \n    factor : NUMBER\n    \n    factor : VARIABLE\n    \n    factor : function_call\n    \n    function_call : VARIABLE DOT LPAREN params RPAREN\n    \n    params : params COMMA expression\n            | expression\n            | empty\n    \n    function_definition : VARIABLE LPAREN args RPAREN LBRACE newline statements newline RBRACE\n    \n    statements : statement\n               | statements newline statement\n    \n    statement : assignment\n    empty :\n    args : VARIABLE COMMA args\n         | VARIABLE\n         | empty\n    '
    
_lr_action_items = {'VARIABLE':([0,2,7,16,17,18,19,20,21,22,26,27,28,37,42,43,54,56,57,59,67,],[6,6,25,-3,-4,-5,25,25,31,34,25,25,25,25,48,34,25,48,61,25,61,]),'STRING':([0,2,7,16,17,18,21,37,54,57,59,67,],[11,11,11,-3,-4,-5,11,11,11,11,11,11,]),'LPAREN':([0,2,6,7,16,17,18,19,20,21,23,26,27,37,54,55,57,59,67,],[7,7,22,7,-3,-4,-5,7,7,7,37,7,7,7,7,59,7,7,7,]),'NUMBER':([0,2,7,16,17,18,19,20,21,26,27,28,37,54,57,59,67,],[13,13,13,-3,-4,-5,13,13,13,13,13,13,13,13,13,13,13,]),'$end':([1,2,15,16,17,18,],[0,-1,-2,-3,-4,-5,]),'newline':([3,4,5,6,8,9,10,11,12,13,14,25,29,30,31,32,33,38,39,40,41,49,50,52,53,60,61,62,63,64,65,68,69,70,],[16,17,18,-25,-15,-16,-20,-17,-22,-24,-26,-25,-13,-14,-25,-6,-7,-23,-18,-19,-21,-8,-10,57,-27,-9,-25,67,-32,-34,-12,-11,-31,-33,]),'PLUS':([5,6,8,9,10,11,12,13,14,24,25,29,30,31,32,38,39,40,41,46,53,58,61,65,],[19,-25,-15,-16,-20,-17,-22,-24,-26,19,-25,-13,-14,-25,19,-23,-18,-19,-21,19,-27,19,-25,19,]),'MINUS':([5,6,8,9,10,11,12,13,14,24,25,29,30,31,32,38,39,40,41,46,53,58,61,65,],[20,-25,-15,-16,-20,-17,-22,-24,-26,20,-25,-13,-14,-25,20,-23,-18,-19,-21,20,-27,20,-25,20,]),'SETTO':([6,61,],[21,21,]),'EXP':([6,12,13,14,25,31,53,61,],[-25,28,-24,-26,-25,-25,-27,-25,]),'TIMES':([6,8,10,12,13,14,25,29,30,31,38,39,40,41,53,61,],[-25,26,-20,-22,-24,-26,-25,26,26,-25,-23,-18,-19,-21,-27,-25,]),'DIVIDE':([6,8,10,12,13,14,25,29,30,31,38,39,40,41,53,61,],[-25,27,-20,-22,-24,-26,-25,27,27,-25,-23,-18,-19,-21,-27,-25,]),'DOT':([6,25,31,48,61,],[23,23,23,55,23,]),'RPAREN':([8,9,10,11,12,13,14,22,24,25,29,30,34,35,36,37,38,39,40,41,43,45,46,47,51,53,58,59,66,],[-15,-16,-20,-17,-22,-24,-26,-35,38,-25,-13,-14,-37,44,-38,-35,-23,-18,-19,-21,-35,53,-29,-30,-36,-27,-28,-35,68,]),'COMMA':([8,9,10,11,12,13,14,25,29,30,34,37,38,39,40,41,45,46,47,53,58,59,66,],[-15,-16,-20,-17,-22,-24,-26,-25,-13,-14,43,-35,-23,-18,-19,-21,54,-29,-30,-27,-28,-35,54,]),'CONNECT':([31,50,68,],[42,56,-11,]),'LBRACE':([44,],[52,]),'RBRACE':([67,],[69,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'top_level':([0,2,],[1,15,]),'top_level_expr':([0,2,],[2,2,]),'assignment':([0,2,57,67,],[3,3,64,64,]),'function_definition':([0,2,],[4,4,]),'expression':([0,2,7,21,37,54,57,59,67,],[5,5,24,32,46,58,65,46,65,]),'term':([0,2,7,19,20,21,37,54,57,59,67,],[8,8,8,29,30,8,8,8,8,8,8,]),'string':([0,2,7,21,37,54,57,59,67,],[9,9,9,9,9,9,9,9,9,]),'exponent':([0,2,7,19,20,21,26,27,37,54,57,59,67,],[10,10,10,10,10,10,39,40,10,10,10,10,10,]),'factor':([0,2,7,19,20,21,26,27,28,37,54,57,59,67,],[12,12,12,12,12,12,12,12,41,12,12,12,12,12,]),'function_call':([0,2,7,19,20,21,26,27,28,37,54,57,59,67,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'flow':([21,],[33,]),'args':([22,43,],[35,51,]),'empty':([22,37,43,59,],[36,47,36,47,]),'params':([37,59,],[45,66,]),'flow_functions':([42,56,],[49,60,]),'flow_function_call':([42,56,],[50,50,]),'statements':([57,],[62,]),'statement':([57,67,],[63,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> top_level","S'",1,None,None,None),
  ('top_level -> top_level_expr','top_level',1,'p_top_level','lexJ.py',141),
  ('top_level -> top_level_expr top_level','top_level',2,'p_top_level','lexJ.py',142),
  ('top_level_expr -> assignment newline','top_level_expr',2,'p_top_level_expr','lexJ.py',148),
  ('top_level_expr -> function_definition newline','top_level_expr',2,'p_top_level_expr','lexJ.py',149),
  ('top_level_expr -> expression newline','top_level_expr',2,'p_top_level_expr','lexJ.py',150),
  ('assignment -> VARIABLE SETTO expression','assignment',3,'p_assignment_assign','lexJ.py',156),
  ('assignment -> VARIABLE SETTO flow','assignment',3,'p_assignment_flow','lexJ.py',171),
  ('flow -> VARIABLE CONNECT flow_functions','flow',3,'p_flow_form','lexJ.py',186),
  ('flow_functions -> flow_function_call CONNECT flow_functions','flow_functions',3,'p_flow_functions','lexJ.py',203),
  ('flow_functions -> flow_function_call','flow_functions',1,'p_flow_function','lexJ.py',217),
  ('flow_function_call -> VARIABLE DOT LPAREN params RPAREN','flow_function_call',5,'p_flow_function_call','lexJ.py',223),
  ('assignment -> expression','assignment',1,'p_assignment_expression','lexJ.py',238),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','lexJ.py',244),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','lexJ.py',259),
  ('expression -> term','expression',1,'p_expression_term','lexJ.py',274),
  ('expression -> string','expression',1,'p_expression_term','lexJ.py',275),
  ('string -> STRING','string',1,'p_string','lexJ.py',281),
  ('term -> term TIMES exponent','term',3,'p_term_times','lexJ.py',287),
  ('term -> term DIVIDE exponent','term',3,'p_term_divide','lexJ.py',303),
  ('term -> exponent','term',1,'p_term_exponent','lexJ.py',319),
  ('exponent -> factor EXP factor','exponent',3,'p_exponent_ext','lexJ.py',325),
  ('exponent -> factor','exponent',1,'p_exponent_factor','lexJ.py',341),
  ('exponent -> LPAREN expression RPAREN','exponent',3,'p_exponent_paren','lexJ.py',347),
  ('factor -> NUMBER','factor',1,'p_factor_num','lexJ.py',359),
  ('factor -> VARIABLE','factor',1,'p_factor_id','lexJ.py',367),
  ('factor -> function_call','factor',1,'p_factor_function_call','lexJ.py',376),
  ('function_call -> VARIABLE DOT LPAREN params RPAREN','function_call',5,'p_function_call','lexJ.py',382),
  ('params -> params COMMA expression','params',3,'p_params','lexJ.py',392),
  ('params -> expression','params',1,'p_params','lexJ.py',393),
  ('params -> empty','params',1,'p_params','lexJ.py',394),
  ('function_definition -> VARIABLE LPAREN args RPAREN LBRACE newline statements newline RBRACE','function_definition',9,'p_function_definition','lexJ.py',416),
  ('statements -> statement','statements',1,'p_statements','lexJ.py',452),
  ('statements -> statements newline statement','statements',3,'p_statements','lexJ.py',453),
  ('statement -> assignment','statement',1,'p_statement','lexJ.py',462),
  ('empty -> <empty>','empty',0,'p_empty','lexJ.py',467),
  ('args -> VARIABLE COMMA args','args',3,'p_args','lexJ.py',472),
  ('args -> VARIABLE','args',1,'p_args','lexJ.py',473),
  ('args -> empty','args',1,'p_args','lexJ.py',474),
]
