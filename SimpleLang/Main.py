import Lexical, Parsing, Codegen   # Here importing all

def main():

    with open("input.slang", "r") as file:
        code = file.read()
    


    tokens = Lexical.tokenize(code)
    print("\nTokens:", tokens)
    

    ast = Parsing.parse(tokens)
    print("\nAST:", ast)
    

    assembly_code = Codegen.generate_assembly(ast)
    print("\nGenerating Assembly Code:\n", assembly_code)
    


    with open("output.asm", "w") as asm_file:
        asm_file.write(assembly_code)

if __name__ == "__main__":
    main()


    