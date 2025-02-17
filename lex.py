import ply.lex as lex

# Defines the list of token names
tokens = (
    'KEYWORD',
    'IDENTIFIER',
    'CONSTANT',
    'ARITH_OP',
    'LOGIC_OP',
    'SEPARATOR',
    'COMMENT',
)

# Regular expressions for tokens
t_LOGIC_OP = r'[&|]|\|\||=='
t_SEPARATOR = r'[;(){}]'
t_ARITH_OP = r'[+\-*/%=]'

# Defines a function to match keywords and identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in ('int', 'float', 'if', 'else', 'exit', 'while', 'read', 'write', 'return'):
        t.type = 'KEYWORD'
    return t

# Defines a function to match constants
def t_CONSTANT(t):
    r'[0-9]+(\.[0-9]+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Defines a rule to ignore whitespace
t_ignore = ' \t'

# Defines a rule to handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Defines a rule to match and capture comments
def t_COMMENT(t):
    r'/\*.*?\*/'
    t.lexer.lineno += t.value.count('\n')
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Builds the lexer
lexer = lex.lex()

# Tests the lexer with example input
if __name__ == "__main__":
    with open('Cminus.txt', 'r') as file:
        data = file.read()

    lexer.input(data)

    for token in lexer:
        print(f"({token.type}, '{token.value}')")
