def generate_assembly(ast):

    asm_code = []

    for node in ast:
        if node.type == "DECLARATION":

            asm_code.append(f"{node.value} DB 0")  # Declaring a variable in memory space



        elif node.type == "ASSIGNMENT":

            asm_code.append(f"MOV {node.value}, {node.children[0].value}")   # Storing  value
        elif node.type == "IF_STATEMENT":

            condition, body = node.children
            asm_code.append(f"CMP {condition.value}, 30")   # Comparing value
            asm_code.append("JNZ END_IF")




            for stmt in body.children:

                asm_code.append(f"MOV {stmt.value}, {stmt.children[0].value}") # Here will execute body

            asm_code.append("END_IF:")
    
    return "\n".join(asm_code)