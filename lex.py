#Lexer Equipo 5
#Gerardo Gutierrez Paniagua
#Mateo Herrera Lavalle
#Jacobo Soffer Levy

#Importing required libraries
import sys
import copy
import ply.lex as lex
import ply.yacc as yacc
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt
from library import *

#Initializing global variables
parseGraph = nx.Graph()
draw = False #Flag to draw the parse tree
symbols = False # Flag to dump the symbol table
NODE_COUNTER = 0 #Counter to assign a unique id to each node

symbol_table = dict()

def add_node(attr):
    global parseGraph
    global NODE_COUNTER
    attr["counter"] = NODE_COUNTER
    parseGraph.add_node(NODE_COUNTER, **attr)
    NODE_COUNTER += 1

    return parseGraph.nodes[NODE_COUNTER - 1]

# Remove pre-existing edges to root node
def remove_duplicates(node: int):
    global parseGraph
    global parseRoot

    parseGraph.remove_edge(parseRoot["counter"], node)

parseRoot = add_node( {"type": "ROOT", "label": "ROOT"} )


symbol_table["e"] = 2.718281828459045
# symbol_table["print"] = print1
# symbol_table["printP"] = printP
symbol_table["max"] = max

symbol_table["load_image"] = load_image
symbol_table["save_image"] = save_image
symbol_table["gen_matrix"] = gen_matrix
symbol_table["gen_vector"] = gen_vector
symbol_table["show_image"] = show_image
# symbol_table["multiplot_show"] = multiplot_show

PLUS_OP = 1
MINUS_OP = 2
TIMES_OP = 3
DIVIDE_OP = 4

tokens = (
    "FUNCTION",
    "NUMBER",
    "VARIABLE",
    "SETTO",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "EXP",
    "LPAREN",
    "RPAREN",
    "COMMA",
    "STRING",
    "CONNECT",
    "LBRACE",
    "RBRACE",
    "SEMI",
    "DOT",
    "newline",
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_SETTO = r'='
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_CONNECT = r'\->'
t_FUNCTION = r'fun'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_DOT = r'\.'

def t_NUMBER(t):
    r'\d+\.?\d*'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t
    # try:
    #     t.value = float(t.value) if '.' in t.value else int(t.value)
    # except ValueError:
    #     print("Invalid number detected.")
    # return t

def t_VARIABLE(t):
    r'[a-zA-Z_]([a-zA-Z0-9_])*'
    return t

def t_STRING(t):
    r'\".*\"'
    t.value = t.value[1:-1]
    return t

# ------------- boilerplate ------------
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t'


def t_error(t):
    print("Error on analysis")
    t.lexer.skip(1)
# --------------- end  ----------------


lexer = lex.lex()

def p_top_level(p):
    '''
    top_level : top_level_expr
              | top_level_expr top_level
    '''
    p[0] = p[1]

def p_top_level_expr(p):
    '''
    top_level_expr : assignment newline
              | function_definition newline
              | expression newline
    '''
    p[0] = p[1]

def p_assignment_assign(p):
    '''
    assignment : VARIABLE SETTO expression
    '''
    node = add_node( {"type":"ASSIGN", "label":"=", "value":""} )
    node_variable = add_node( {"type":"VARIABLE_ASSIGN", "label":f"VAR_{p[1]}", "value":p[1]} )
    parseGraph.add_edge(node["counter"], node_variable["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    remove_duplicates(p[3]["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node

def p_assignment_flow(p):
    '''
    assignment : VARIABLE SETTO flow
    '''
    node = add_node( {"type":"ASSIGN", "label":"=", "value":""} )
    node_variable = add_node( {"type":"VARIABLE_ASSIGN", "label":f"VAR_{p[1]}", "value":p[1]} )
    parseGraph.add_edge(node["counter"], node_variable["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node

def p_flow_form(p):
    '''
    flow : VARIABLE CONNECT flow_functions
    '''
    ff = p[3][0]

    connections = parseGraph.neighbors(ff["counter"])

    for c in connections:
        c = parseGraph.nodes[c]
        if( c["type"] == "PENDING_NODE"):
            c["type"] = "VARIABLE"
            c["label"] = f"VAR_{p[1]}"
            c["value"] = p[1]
            break
    p[0] = p[3][-1]

def p_flow_functions(p):
    '''
    flow_functions : flow_function_call CONNECT flow_functions
    '''
    connections = parseGraph.neighbors(p[3][0]["counter"])

    for c in connections:
        c = parseGraph.nodes[c]
        if c["type"] == "PENDING_NODE":
            parseGraph.add_edge( c["counter"], p[1]["counter"] )
            break
    p[0] = [p[1]] + p[3]
    

def p_flow_function(p):
    '''
    flow_functions : flow_function_call
    '''
    p[0] = [p[1]]

def p_flow_function_call(p):
    '''
    flow_function_call : VARIABLE DOT LPAREN params RPAREN
    '''
    node = add_node( {"type":"FLOW_FUNCTION_CALL", "label":f"FF_{p[1]}", "value":p[1]} )
    pending_node = add_node( {"type":"PENDING_NODE", "label":"PENDING", "value":""} )
    parseGraph.add_edge(node["counter"], pending_node["counter"])

    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])
    
    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node

def p_assignment_expression(p):
    '''
    assignment : expression
    '''
    p[0] = p[1]

def p_expression_plus(p):
    '''
    expression : expression PLUS term
    '''
    node = add_node( {"type":"PLUS", "label":"+", "value":""} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    remove_duplicates(p[1]["counter"])
    remove_duplicates(p[3]["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node

def p_expression_minus(p):
    '''
    expression : expression MINUS term
    '''
    node = add_node( {"type":"MINUS", "label":"-", "value":""} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node

def p_expression_term(p):
    '''
    expression : term 
            | string
    '''
    p[0] = p[1]

def p_string(p):
    '''
    string : STRING
    '''
    p[0] = add_node( {"type":"STRING", "label":f"STR_{p[1]}", "value":p[1]} )

def p_term_times(p):
    '''
    term : term TIMES exponent
    '''
    node = add_node( {"type":"TIMES", "label":"*", "value":""} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node
    # p[0] = p[1] * p[3]

def p_term_divide(p):
    '''
        term : term DIVIDE exponent
    '''
    node = add_node( {"type":"DIVIDE", "label":"/", "value":""} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node
    # p[0] = p[1] / p[3]

def p_term_exponent(p):
    '''
    term : exponent
    '''
    p[0] = p[1]

def p_exponent_ext(p):
    '''
    exponent : factor EXP factor
    '''
    node = add_node( {"type":"POWER", "label":"POW", "value":""} )
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node
    # p[0] = pow(p[1], p[3]) 

def p_exponent_factor(p):
    '''
    exponent : factor
    '''
    p[0] = p[1]

def p_exponent_paren(p):
    '''
    exponent : LPAREN expression RPAREN
    '''
    node = add_node( {"type":"GROUP", "label":"{}", "value":""} )
    parseGraph.add_edge(node["counter"], p[2]["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])

    p[0] = node
    # p[0] = p[2]

def p_factor_num(p):
    '''
    factor : NUMBER
    '''
    node = add_node( {"type":"NUMBER", "label":f"NUM_{p[1]}", "value":p[1]} )
    parseGraph.add_edge(parseRoot["counter"], node["counter"])
    p[0] = node

def p_factor_id(p):
    '''
    factor : VARIABLE
    '''
    node = add_node( {"type":"VARIABLE", "label":f"VAR_{p[1]}", "value":p[1]} )
    parseGraph.add_edge(parseRoot["counter"], node["counter"])
    p[0] = node
    # p[0] = symbol_table[p[1]]

def p_factor_function_call(p):
    '''
    factor : function_call
    '''
    p[0] = p[1]

def p_function_call_no_params(p):
    '''
    function_call : VARIABLE DOT LPAREN RPAREN
    '''
    # node = add_node( {"type":"FUNCTION_CALL", "label":f"FUN_{p[1]}", "value":p[1]} )
    node = add_node( {"type":"FUNCTION_CALL", "label":f"FUN_{p[1]}", "value":p[1]} )
    parseGraph.add_edge(parseRoot["counter"], node["counter"])
    p[0] = node
    # p[0] = node
    # p[0] = symbol_table[p[1]]()

def p_function_call_params(p):
    # '''
    # function_call : VARIABLE LPAREN params RPAREN
    # '''
    # node = add_node( {"type":"FUNCTION_CALL", "label":f"FUN_{p[1]}", "value":p[1]} )
    # for n in p[3]:
    #     parseGraph.add_edge(node["counter"], n["counter"])def p_function_call_params(p):
    '''
    function_call : VARIABLE DOT LPAREN params RPAREN
    '''
    node = add_node( {"type":"FUNCTION_CALL", "label":f"FUN_{p[1]}", "value":p[1]} )
    for n in p[4]:
        if isinstance(n, dict) and "counter" in n:
            parseGraph.add_edge(node["counter"], n["counter"])

    parseGraph.add_edge(parseRoot["counter"], node["counter"])
    p[0] = node
    # p[0] = node
    # p[0] = symbol_table[p[1]]( *p[3] )

def p_params(p):
    '''
    params : params COMMA expression
            | expression
    '''
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_function_definition(p):
    '''
    function_definition : VARIABLE LPAREN args RPAREN LBRACE newline statements newline RBRACE
    '''
    local_graph = nx.Graph()
    root = {"type": "ROOT", "label": "ROOT", "counter": 0}
    local_graph.add_node(0, **root)

    for node in p[7]:
        local_graph.add_node(node["counter"], **node)
        local_graph.add_edge(root["counter"], node["counter"])
        children = parseGraph.neighbors(node["counter"])
        to_remove = []
        for c in children:
            if c == parseRoot["counter"] or c == node["counter"]:
                continue
            n = parseGraph.nodes[c]
            local_graph.add_node(n["counter"], **n)
            local_graph.add_edge(node["counter"], n["counter"])
            to_remove.append(n["counter"])

        for n in to_remove:
            parseGraph.remove_node(n)        
        parseGraph.remove_node(node["counter"])

    value = {
        'name': p[1],
        'args': p[3],
        'body': p[7],
        'graph': local_graph
    }

    node = add_node( {'type': 'FUNCTION_DEFINITION', 'label': f'FUNCD_{value["name"]}', 'value': value })
    parseGraph.add_edge(parseRoot["counter"], node["counter"])
    p[0] = node

def p_statements(p):
    '''
    statements : statement
               | statements newline statement
    '''
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''
    statement : assignment
    '''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_args(p):
    '''
    args : VARIABLE COMMA args
         | VARIABLE
         | empty
    '''
    if len(p) == 2 and p[1] == None:
        p[0] = []
    elif len(p) > 2:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_error(p):
    print("Syntax error found", p)

def execute_parse_tree(tree, symbols, reverse=False):
    # root = tree.nodes[0]
    root_id = 0
    res = (visit_node(tree, root_id, -1, symbols, reverse))
    if(type(res) == int or type(res) == float):
        print("TREE_RESULT: ", res)
    return res

def visit_node(tree, node_id, from_id, symbols, reverse):
    children = tree.neighbors(node_id)
    res = []
    for c in children:
        if( c != from_id):
            res.append(visit_node(tree, c, node_id, symbols, reverse))
    
    current_node = tree.nodes[node_id]
    # print(f"From Node {node_id}", res)

    if( current_node["type"] == "ROOT" ):
        return res[-1]
    
    if( current_node["type"] == "ASSIGN" ):
        symbols[res[0]] = res[1]
        return res[1]
    
    if( current_node["type"] == "VARIABLE_ASSIGN" ):
        return current_node["value"]

    if( current_node["type"] == "NUMBER" ):
        return current_node["value"]
    
    if( current_node["type"] == "STRING" ):
        return current_node["value"]

    if( current_node["type"] == "PLUS" ):
        return res[0] + res[1]

    if( current_node["type"] == "VARIABLE" ):
        return symbols[current_node["value"]]
    
    if( current_node["type"] == "MINUS" ):
        return res[0] - res[1]
    
    if( current_node["type"] == "POWER" ):
        return pow(res[0], res[1])
    
    if( current_node["type"] == "GROUP" ):
        return res[0]
    
    if( current_node["type"] == "PENDING_NODE" ):
        return res[0]
    
    if( current_node["type"] == "TIMES" ):
        return res[0] * res[1]
    
    if( current_node["type"] == "DIVIDE" ):
        return res[0] / res[1]
    
    if (current_node["type"] == "FUNCTION_DEFINITION"):
        symbols[current_node["value"]["name"]] = current_node["value"]
        return f'func<{current_node['value']['name']}>'

    if( current_node["type"] == "FUNCTION_CALL" or current_node["type"] == "FLOW_FUNCTION_CALL"):
        v = current_node["value"]
        if v in symbols:
            fn = symbols[v]
            
            if type(fn) is dict:
                s = copy.deepcopy(symbol_table)
                print(v)
                res = execute_parse_tree(fn["graph"], s, True)
                return res

            elif( callable(fn) ):
                try:
                    res = fn(*res)
                    return res
                except Exception as e:
                    print(f"Error calling function {v}" , e)
                    return "Error"
            else:
                print(f"Error function {v} IS NOT a function")
                return "Error"
        else:
            fn = search_cv2(v)
            if(fn is not None):
                if( callable(fn) ):
                    try:
                        res = fn(*res)
                        return res
                    except Exception as e:
                        print(f"Error calling function {v}" , e, v, "FN: ", fn, "RES: ", res)
                        return "Error"
                else:
                    print(f"Error function {v} IS NOT a function")
                    return "Error"
            else:
                print(f"Error {v} Is NOT on the symbol table")
                return "Error"
        

# initialize globals
parser = yacc.yacc()
parseGraph = nx.Graph()
NODE_COUNTER = 0

def repl():
    global parseGraph
    global NODE_COUNTER
    while True:

        try:
            data = input(">")
            if data == "exit":
                break
            if (data == "symbols"):
                print(symbol_table)
                continue

        except EOFError:
            break

        if not data: continue

        parseGraph = nx.Graph()
        NODE_COUNTER = 0
        root = add_node( {"type":"ROOT", "label":"ROOT"} )
        result = parser.parse(data)
        parseGraph.add_edge(root["counter"], result["counter"])

        labels = nx.get_node_attributes(parseGraph, "label")

        if(draw):
            # pos = graphviz_layout(parseGraph, prog="dot")
            # nx.draw(parseGraph, pos)
            # nx.draw(parseGraph, with_labels=True, font_weight="bold")
            # nx.draw(parseGraph, pos, labels=labels, with_labels=True)
            nx.draw(parseGraph, labels=labels, with_labels=True, font_weight="bold")
            plt.show()

        execute_parse_tree(parseGraph)
        # print(result)

    # print("Finished, accepted")

def parse_file(path):
    global parseGraph
    global NODE_COUNTER
    global parseRoot

    with open(path, 'r') as file:
        data = file.read()
        parseGraph = nx.Graph()
        parseRoot = add_node( {"type":"ROOT", "label":"ROOT"} )
        parser.parse(data)

        labels = nx.get_node_attributes(parseGraph, "label")
        if(draw):
            nx.draw(parseGraph, labels=labels, with_labels=True, font_weight="bold")
            plt.show()

        execute_parse_tree(parseGraph, symbol_table)
        if symbols:
            print(symbol_table)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            print('LEX Interpreter v0.0.1')
            print('Usage: python3 lex.py <file_path>.lx <flags>')
            print('Flags:')
            print('  * To visualize the AST set the `draw` flag when running the command.')
            print('  * To dump the symbol table set the `symblos` flag.')
            exit(0)
        if 'draw' in sys.argv:
            draw = True
        if 'symbols' in sys.argv:
            symbols = True
        parse_file(sys.argv[1])
    else:
        print("Error: an input file must be provided. Run `python3 lex.py help` for more information")
        #repl()