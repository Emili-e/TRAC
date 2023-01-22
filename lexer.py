from ply import lex
import Parser
# --- Tokenizer

# All tokens must be named in advance.
tokens = ( 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
           'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
           'COL', 'SCOL', 'COM', 'ASSIGN',
           'QUOT',
           'NAME', 'NUMBER' )

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

t_COL = r'\:'
t_SCOL = r'\;'
t_COM = r'\,'
t_ASSIGN = r'\='

t_QUOT = r'\"'

t_NAME = r'[a-zA-Z_][a-zA-Z0-9._]*'

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)



# Build the lexer object
# lexer = lex.lex()

# Data to test
# f = open("code#.cs", "r")
# data = f.read()

# Give the lexer some input
# lexer.input(data)

# Tokenize
def lexing(data, socket):
    lexer = lex.lex()
    lexer.input(data)
    

    lexing = []
    while True:
        tok = lexer.token()
        lexing = lexing + [tok]
        if not tok: break # No more input
    lexing.pop()
    #print(lexing)
    # retire le dernier élément None
    print(Parser.variableIdentifier(lexing, socket))
    return lexing

# lexing : liste dont les éléments sont : LexToken(TYPE,'value',line,col)
# - lexing[index].type --> type du token (nom du token)
# - lexing[index].value --> valeur du token
# - lexing[index].lineno --> le numero de ligne courant