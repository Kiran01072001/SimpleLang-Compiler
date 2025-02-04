
import re 

# Regular Expressions in Python Module

TOKEN_TYPES = {
    "INT": r'\bint\b',
    "IF": r'\bif\b',
    "NUMBER": r'\b\d+\b',
    "IDENTIFIER": r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    "ASSIGN": r'=',
    "PLUS": r'\+',
    "EQUAL": r'==',
    "LBRACE": r'\{',
    "RBRACE": r'\}',
    "SEMICOLON": r';',
    "LPAREN": r'\(',
    "RPAREN": r'\)',
    "COMMENT": r'//.*'
}

def tokenize(code):

    code = re.sub(TOKEN_TYPES["COMMENT"], '', code) # It will remove comments
      
    tokens = []  # Taking Empty List

    
    while code:

        code = code.lstrip()  # It will remove spaces

        for token_type, pattern in TOKEN_TYPES.items():

            match = re.match(pattern, code)

            if match:
                tokens.append((token_type, match.group()))

                code = code[len(match.group()):].lstrip()  # Removing matched part
                break
        else:


            raise SyntaxError(f"Unexpected token: {code[0]}")

    return tokens
                              
    
    







