                                                                                               # SimpleLand-Compiler

This project is a simple compiler for a custom language called SimpleLang. It tokenizes, parses, and generates assembly code for a subset of imperative programming constructs.

#Features

Tokenization of keywords, identifiers, operators, and comments
Abstract Syntax Tree (AST) generation
Assembly code generation for variable declarations, assignments, and conditional statements

#File Structure

Lexcial.py - Handles tokenization of the source code
Parsing.py - Converts tokens into an Abstract Syntax Tree (AST)
Codegen.py - Translates the AST into assembly code
input.slang - Example SimpleLang source code
output.asm - Generated assembly code
Main.py - Entry point for the compiler

#Example SimpleLang Code

// Variable Declaration
int p;
int q;
int r;

// Assignment
p = 10;
q = 20;
r = p + q;

// Conditional Statement
if (r == 30) {
    r = r + 1;
}

#How It Works

The lexer reads the source code and tokenizes it.
The parser converts tokens into an Abstract Syntax Tree (AST).
The codegen module translates the AST into assembly instructions.
The generated assembly code is written to output.asm.


#Usage
#Prerequisites

Ensure you have Python installed.
Running the Compiler
python main.py
This will process input.slang and generate output.asm.

#Sample Output (Assembly Code)

p DB 0
q DB 0
r DB 0
MOV p, 10
MOV q, 20
MOV r, p + q
CMP r, 30
JNZ END_IF
MOV r, r + 1
END_IF:
