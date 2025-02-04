class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children or []
    
    def __repr__(self):
        return f"{self.type}({self.value}, {self.children})"

def parse(tokens):

    ast, i = [], 0

    while i < len(tokens):

        token_type, token_value = tokens[i]


        if token_type == "INT":  




            ast.append(ASTNode("DECLARATION", tokens[i + 1][1]))
            i += 2  
        elif token_type == "IDENTIFIER" and tokens[i + 1][0] == "ASSIGN":
            ast.append(ASTNode("ASSIGNMENT", token_value, [ASTNode("EXPR", tokens[i + 2][1])]))
            i += 4  


        elif token_type == "IF":


            condition = ASTNode("CONDITION", tokens[i + 2][1])

            
            body = ASTNode("BLOCK", None, [])
            i += 4  
            while tokens[i][0] != "RBRACE":


                if tokens[i][0] == "IDENTIFIER" and tokens[i + 1][0] == "ASSIGN":
                    body.children.append(ASTNode("ASSIGNMENT", tokens[i][1], [ASTNode("EXPR", tokens[i + 2][1])]))
                    i += 4  
                else:
                    i += 1
            ast.append(ASTNode("IF_STATEMENT", None, [condition, body]))
            i += 1  
        else:
            i += 1  
    return ast
