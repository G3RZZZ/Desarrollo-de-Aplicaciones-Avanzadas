
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA CONNECT DIVIDE EXP LBRACKET LPAREN MINUS NUMBER PLUS RBRACKET RPAREN SETTO STRING TIMES VARIABLE\n    assignment : VARIABLE SETTO expression\n                | VARIABLE SETTO list\n    \n    assignment : VARIABLE SETTO flow\n    \n    flow : VARIABLE CONNECT flow_functions\n    \n    flow_functions : flow_function_call CONNECT flow_functions\n    \n    flow_functions : flow_function_call\n    \n    flow_function_call : VARIABLE LPAREN params RPAREN\n    \n    assignment : expression\n    \n    expression : expression PLUS term\n    \n    expression : expression MINUS term\n    \n    expression : term \n            | string\n    \n    string : STRING\n    \n    term : term TIMES exponent\n    \n        term : term DIVIDE exponent\n    \n    term : exponent\n    \n    exponent : factor EXP factor\n    \n    exponent : factor\n    \n    exponent : LPAREN expression RPAREN\n    \n    factor : NUMBER\n    \n    factor : VARIABLE\n    \n    factor : function_call\n    \n    function_call : VARIABLE LPAREN RPAREN\n    \n    function_call : VARIABLE LPAREN params RPAREN\n    \n    params : params COMMA expression\n            | expression\n    \n    list : LBRACKET contents RBRACKET\n    \n    contents : contents COMMA content\n            | content\n    \n    content : expression\n            | list\n    \n    list : LBRACKET RBRACKET\n    \n    expression : VARIABLE LBRACKET subscript RBRACKET\n    \n    subscript : NUMBER\n    \n    expression : VARIABLE LBRACKET subscript RBRACKET SETTO expression\n    \n    expression : VARIABLE LBRACKET expression COLON expression RBRACKET\n    '
    
_lr_action_items = {'VARIABLE':([0,9,12,13,14,15,16,17,18,19,26,40,47,49,54,55,58,59,],[2,21,22,21,21,34,34,34,34,34,21,50,21,21,21,21,21,50,]),'STRING':([0,9,12,13,14,26,47,49,54,55,58,],[7,7,7,7,7,7,7,7,7,7,7,]),'LPAREN':([0,2,9,12,13,14,15,16,17,18,21,22,26,34,47,49,50,54,55,58,],[9,14,9,9,9,9,9,9,9,9,14,14,9,14,9,9,58,9,9,9,]),'NUMBER':([0,9,12,13,14,15,16,17,18,19,26,47,49,54,55,58,],[10,10,10,29,10,10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,2,3,4,5,6,7,8,10,11,21,22,23,24,25,30,33,34,35,36,37,38,39,42,46,48,51,52,53,61,62,64,65,],[0,-21,-8,-11,-12,-16,-13,-18,-20,-22,-21,-21,-1,-2,-3,-23,-9,-21,-10,-14,-15,-17,-19,-32,-33,-24,-4,-6,-27,-35,-36,-5,-7,]),'SETTO':([2,46,],[12,55,]),'LBRACKET':([2,12,21,22,26,54,],[13,26,13,13,26,26,]),'EXP':([2,8,10,11,21,22,29,30,34,48,],[-21,19,-20,-22,-21,-21,-20,-23,-21,-24,]),'TIMES':([2,4,6,8,10,11,21,22,29,30,33,34,35,36,37,38,39,48,],[-21,17,-16,-18,-20,-22,-21,-21,-20,-23,17,-21,17,-14,-15,-17,-19,-24,]),'DIVIDE':([2,4,6,8,10,11,21,22,29,30,33,34,35,36,37,38,39,48,],[-21,18,-16,-18,-20,-22,-21,-21,-20,-23,18,-21,18,-14,-15,-17,-19,-24,]),'PLUS':([2,3,4,5,6,7,8,10,11,20,21,22,23,28,29,30,32,33,34,35,36,37,38,39,44,46,48,56,57,61,62,],[-21,15,-11,-12,-16,-13,-18,-20,-22,15,-21,-21,15,15,-20,-23,15,-9,-21,-10,-14,-15,-17,-19,15,-33,-24,15,15,15,-36,]),'MINUS':([2,3,4,5,6,7,8,10,11,20,21,22,23,28,29,30,32,33,34,35,36,37,38,39,44,46,48,56,57,61,62,],[-21,16,-11,-12,-16,-13,-18,-20,-22,16,-21,-21,16,16,-20,-23,16,-9,-21,-10,-14,-15,-17,-19,16,-33,-24,16,16,16,-36,]),'RPAREN':([4,5,6,7,8,10,11,14,20,21,30,31,32,33,34,35,36,37,38,39,46,48,57,61,62,63,],[-11,-12,-16,-13,-18,-20,-22,30,39,-21,-23,48,-26,-9,-21,-10,-14,-15,-17,-19,-33,-24,-25,-35,-36,65,]),'COLON':([4,5,6,7,8,10,11,21,28,29,30,33,34,35,36,37,38,39,46,48,61,62,],[-11,-12,-16,-13,-18,-20,-22,-21,47,-20,-23,-9,-21,-10,-14,-15,-17,-19,-33,-24,-35,-36,]),'COMMA':([4,5,6,7,8,10,11,21,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,48,53,57,60,61,62,63,],[-11,-12,-16,-13,-18,-20,-22,-21,-23,49,-26,-9,-21,-10,-14,-15,-17,-19,54,-32,-29,-30,-31,-33,-24,-27,-25,-28,-35,-36,49,]),'RBRACKET':([4,5,6,7,8,10,11,21,26,27,29,30,33,34,35,36,37,38,39,41,42,43,44,45,46,48,53,56,60,61,62,],[-11,-12,-16,-13,-18,-20,-22,-21,42,46,-34,-23,-9,-21,-10,-14,-15,-17,-19,53,-32,-29,-30,-31,-33,-24,-27,62,-28,-35,-36,]),'CONNECT':([22,52,65,],[40,59,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,],[1,]),'expression':([0,9,12,13,14,26,47,49,54,55,58,],[3,20,23,28,32,44,56,57,44,61,32,]),'term':([0,9,12,13,14,15,16,26,47,49,54,55,58,],[4,4,4,4,4,33,35,4,4,4,4,4,4,]),'string':([0,9,12,13,14,26,47,49,54,55,58,],[5,5,5,5,5,5,5,5,5,5,5,]),'exponent':([0,9,12,13,14,15,16,17,18,26,47,49,54,55,58,],[6,6,6,6,6,6,6,36,37,6,6,6,6,6,6,]),'factor':([0,9,12,13,14,15,16,17,18,19,26,47,49,54,55,58,],[8,8,8,8,8,8,8,8,8,38,8,8,8,8,8,8,]),'function_call':([0,9,12,13,14,15,16,17,18,19,26,47,49,54,55,58,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'list':([12,26,54,],[24,45,45,]),'flow':([12,],[25,]),'subscript':([13,],[27,]),'params':([14,58,],[31,63,]),'contents':([26,],[41,]),'content':([26,54,],[43,60,]),'flow_functions':([40,59,],[51,64,]),'flow_function_call':([40,59,],[52,52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignment","S'",1,None,None,None),
  ('assignment -> VARIABLE SETTO expression','assignment',3,'p_assignment_assign','lexer_lists.py',134),
  ('assignment -> VARIABLE SETTO list','assignment',3,'p_assignment_assign','lexer_lists.py',135),
  ('assignment -> VARIABLE SETTO flow','assignment',3,'p_assignment_flow','lexer_lists.py',145),
  ('flow -> VARIABLE CONNECT flow_functions','flow',3,'p_flow_form','lexer_lists.py',155),
  ('flow_functions -> flow_function_call CONNECT flow_functions','flow_functions',3,'p_flow_functions','lexer_lists.py',172),
  ('flow_functions -> flow_function_call','flow_functions',1,'p_flow_function','lexer_lists.py',186),
  ('flow_function_call -> VARIABLE LPAREN params RPAREN','flow_function_call',4,'p_flow_function_call','lexer_lists.py',192),
  ('assignment -> expression','assignment',1,'p_assignment_expression','lexer_lists.py',205),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','lexer_lists.py',211),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','lexer_lists.py',220),
  ('expression -> term','expression',1,'p_expression_term','lexer_lists.py',229),
  ('expression -> string','expression',1,'p_expression_term','lexer_lists.py',230),
  ('string -> STRING','string',1,'p_string','lexer_lists.py',236),
  ('term -> term TIMES exponent','term',3,'p_term_times','lexer_lists.py',242),
  ('term -> term DIVIDE exponent','term',3,'p_term_divide','lexer_lists.py',252),
  ('term -> exponent','term',1,'p_term_exponent','lexer_lists.py',262),
  ('exponent -> factor EXP factor','exponent',3,'p_exponent_ext','lexer_lists.py',268),
  ('exponent -> factor','exponent',1,'p_exponent_factor','lexer_lists.py',278),
  ('exponent -> LPAREN expression RPAREN','exponent',3,'p_exponent_paren','lexer_lists.py',284),
  ('factor -> NUMBER','factor',1,'p_factor_num','lexer_lists.py',293),
  ('factor -> VARIABLE','factor',1,'p_factor_id','lexer_lists.py',299),
  ('factor -> function_call','factor',1,'p_factor_function_call','lexer_lists.py',306),
  ('function_call -> VARIABLE LPAREN RPAREN','function_call',3,'p_function_call_no_params','lexer_lists.py',312),
  ('function_call -> VARIABLE LPAREN params RPAREN','function_call',4,'p_function_call_params','lexer_lists.py',322),
  ('params -> params COMMA expression','params',3,'p_params','lexer_lists.py',340),
  ('params -> expression','params',1,'p_params','lexer_lists.py',341),
  ('list -> LBRACKET contents RBRACKET','list',3,'p_list','lexer_lists.py',352),
  ('contents -> contents COMMA content','contents',3,'p_contents','lexer_lists.py',361),
  ('contents -> content','contents',1,'p_contents','lexer_lists.py',362),
  ('content -> expression','content',1,'p_content','lexer_lists.py',371),
  ('content -> list','content',1,'p_content','lexer_lists.py',372),
  ('list -> LBRACKET RBRACKET','list',2,'p_empty_list','lexer_lists.py',378),
  ('expression -> VARIABLE LBRACKET subscript RBRACKET','expression',4,'p_subscript_access','lexer_lists.py',384),
  ('subscript -> NUMBER','subscript',1,'p_subscript','lexer_lists.py',393),
  ('expression -> VARIABLE LBRACKET subscript RBRACKET SETTO expression','expression',6,'p_subscript_assignment','lexer_lists.py',399),
  ('expression -> VARIABLE LBRACKET expression COLON expression RBRACKET','expression',6,'p_slice_access','lexer_lists.py',412),
]
