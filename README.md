# Compilers
## Description
```
The project will consist of implementing a compiler
that compiles code written in (a subset of) the C language. The compiler will output LLVM IR code and MIPS assembly code.

Concretely, you will construct a grammar and lexer specification, which is then turned into
Python code using the ANTLR tool. The rest of the project will consist of developing
custom code written in Python 3. This custom code will take the parse tree and turn it
into an abstract syntax tree (AST). This AST will then be used to generate code in the
LLVM IR language and in the MIPS assembly language. At various stages of the project
you will also have to develop utilities to provide insight into the internals of the compiler,
such as visualising the AST tree.
```
University Project compilers 2022-2023 <br>
Done by Marceli Wilczynski && Elias El Bouzidi <br>

## Table of Contents
1. [Installation](#Installation)
2. [Documentation](#Documentation)
3. [Project 1](#Project1)
4. [Project 2](#Project2)
5. [Project 3](#Project3)
6. [Mips](#Mips)

## Documentation
## Main.py
```
> Main.py
  > def main(argv)
This function takes sys.argv as argument and will do/produce the following code on runtime.
1. Produce AST and store it in AST object
2. Check for syntax errors
3. Check for semantic errors
4. Apply Constant propagation and constant folding on AST object
5. Create a .dot file constructed from the AST object
6. Create a symboltable for the AST object
7. Create a .ll file constructed from LLVM object which will convert our C to LLVM code
```
---------
## AST
```
> AST.py
    > Class AST
    > Class Node

Node is a class used by our AST(Abstract Syntax Tree) to store data in a tree form.
```
---------
## SemanticAnalysis
```
> SemanticAnalysisVisitor.py
 > Class SemanticAnalysisVisitor
 This class is a visitor for our AST to catch semantic errors. In project 2 in this readme can u find which errors should this class catch.
```
---------
## Tests
```
> runTests.py
This file has 3 functions. runCorrect(), runAll(), main_test()
main_test() acts like main function
runCorrect() runs all correct tests in /testen/correctTests folder and producses .ll and .dot files for the given test files in the same directory!
runAll() runs all tests in /testen folder (CURRENTLY NOT WORKING BECAUSE WE DONT KNOW IF WE NEED TO HAVE AUTOMATED TESTS FOR ERRORS)

To see if the tests are good look in /TestenExpectedOutput folder in the same folder name as in /testen there should be files with expected output.


How to run correct tests?
1. Go to runTests.py
2. def main_test():
    runCorrect()
3. run runTests.py

How to run single test? (Good for error tests)
1. Go to main.py
2. if __name__ == '__main__':
    main("namefile.c")
3. run main.py


```
-------
## SymbolTable
```
> SymbolTable.py
 > class SymbolTable
This class will store all the necessery info needed from our AST in a list of dictionaries. We use list so it can later on support scopes.
Example:
    int a = 5;
    Our symbol table dictionary will look like that:
    [{'a': [int, [None, None], 5]}] (1 dict because only 1 scope)
    Where 'a' (key) is the name of the variable. Our value of the key (array) will store the 
    [datatype, [const/ptr, amount ptrs], value, arraySize] so in this example
    we have [int, [none, none], 5] because int is the datatype of a and it's not a const or a ptr so the list [None, None] will remain the same and 5 is the value of the variable

Here is more complex example:
    int main(){
        int a = 10;
        const int* b = &a;
        char c = 'c';
        const float tempVar = 33.4;
        int arr[2] = {1,2};
    }
    [main: [
    {'a': ['int', [None, None], 10], 
    'b': ['int', [const pointer, 1], &a], 
    'c': ['char', [None, None], 'c'], 
    'tempVar': ['float', ['const', None], 33.4],
    'arr': ['int', [None, None], {1,2}, 2]}
    ]]
```
## Project1
----------
### 2 Expression Parser
#### 2.1 Grammar
Construct a grammar for simple mathematical expressions, operating only on int literals.
Every expression should end with a semicolon. Input files can contain multiple expressions.
The following operators must be supported:
### Implemented Functionality
```
• (mandatory) Binary operations +, -, *, and /.
• (mandatory) Binary operations >, <, and ==.
• (mandatory) Unary operators + and -.
• (mandatory) Brackets to overwrite the order of operations.
• (mandatory) Logical operators &&, ||, and !.
• (mandatory) Ignore whitespace in code.
• (mandatory) Constant folding.
• (mandatory) Construction and using the ast.
• (optional) Modulo operator %.
• (optional) Comparison operators >=, <=, and !=.
```
All of the above are implementend in our compiler   .

#### 2.2 Abstract Syntax Tree
You should construct an explicit AST from the Concrete Syntax Tree (CST) generated
by ANTLR. Define your own datastructure in Python to construct the AST, such that you
do not depend on ANTLR classes.
```
Our AST.py consist of AST class which constructs AST.
```
#### 2.3 Visualization
To show your AST structure, provide a listener or visitor for your AST that prints the
tree in the Graphviz dot format.
```
See our printDot function of our AST
```
#### 2.4 Constant Folding
```
See our constanFolding function of our AST
```
---------
## Project2
### Implemented Functionality
```
• (mandatory) Types. (char, float, int)
• (mandatory) The const keyword must be supported, next to the types char, int, and float.
• (mandatory) Variables.There should be support for variables. This includes variable declarations, variable definitions, assignment statements, and identifiers appearing in expressions. You
must also provide support for const variables.
• (mandatory) Pointer Operations. Support for the unary operators * and &.
• (mandatory) Basic pointer operations: address (&var), dereference (*var).
• (mandatory) Constant propagation
• (mandatory) Construction and usage of the symbol table
• (mandatory) Syntax errors + error message
• (mandatory) Semantic errors + error message:
    ∗ Usage of uninitialised and undeclared variables
    ∗ Redeclarations and redefinitions of existing variables
    ∗ Operations and assignments with incompatible types
    ∗ Assignment to an rvalue expression
    ∗ Re-assignment of const variables


```
All of the above are implementend in our grammar.

### 1.2 Abstract Syntax Trees
```
Our tree is updated for the new grammar.
```

### 1.3 Visualization
```
Our printDot function produces the correct .dot file for our AST.
```
### 1.4 Consant Propagation
```
Our constant propagation works with new AST
```
## 2 Eror Analysis
### 2.1 Syntax errors
The compiler is allowed to stop when it encounters a syntax error. An indication of the
location of the syntax error should be displayed, but diagnostic information about the type
of error is optional (and non-trivial).

### 2.2 Semantic Errors
For semantical errors, it is necessary to output more specific information about the encountered error. 
Our program should detec those semantic errors:
```
• Use of an undefined or uninitialized variable.
• Redeclaration or redefinition of an existing variable.
• Operations or assignments of incompatible types.
• Assignment to an rvalue.
• Assignment to a const variable.
```
We created a file that tests all of this types "runTest.py" look more in Documentation.

## Project3
### Implemented Functionality
Extended functionality
```
• (mandatory) Comments.
    - (optional) Instead of simply ignoring comments, you can increase the readability
      of the generated LLVM code by retaining the comments from the input code
      during the compilation process. The comments will thus be stored in the AST.
      Such comments can then be put into the LLVM code.
• (mandatory) Support for single line comments and multi line comments.
• (mandatory) Outputting to the standard output using printf.
```
## Project4
### Implemented Functionality
```
• (mandatory): 
    – if and else statements
    – while loops
    – for loops
    – break statements
    – continue statements
    – Anonymous scopes
    – Symbol table for anonymous scopes
```
## Project5
### Implemented Functionality
```
• (mandatory): 
    – Function scopes
    – Symbol table for function scopes
    – Local and global variables
    – Functions:
        ∗ Definition and declaration
        ∗ Calling
        ∗ Parameters (primitives and pointers, pass-by-value, pass-by-reference)
        ∗ Return values
        ∗ Functions with void return
    – Type checking for return statements
    – Type checking for forward declarations
    – No dead code after return, break, and continue
• (optional): 
    – No code is generated for if-clauses that are never true
```
## Project6
### Implemented Functionality
```
• (mandatory): 
    – One-dimensional static arrays
    – printf
    – scanf
    – #include <stdio.h> statement (only for printf and scanf)
```

Example inputfile:
```
/*
* My program
*/
int x = 5*(3/10 + 9/10);
float y = x*2/( 2+1 * 2/3 +x) +8 * (8/4);
float result = x + y; //calculate the result
printf(result); //show the result
```
Should produce a .dot file with correct AST.

#### 1.2 Abstract Syntax Tree
```
We updated our tree for the new grammar.
```
#### 1.3 Visualization
```
Our printDot function produces new AST tree
```
### 2 Code Generation: LLVM
```
Our LLVM class in LLVM.py produces LLVM code from our C test file in a .ll format
see example in main.py how to use it.
>main.py
    llvm = LLVM(argv, symbolTable) //make llvm object that will store llvm data
    llvm.look_for_value(ast) // check for needed values in symboltable
    llvm.generate_LLVM() // generate llvm files
----------
```
## MIPS
```
Every single mandatory and optional functionality we implemented in LLVM we also implemented in MIPS.

U can see our code for Mips in Mips.py.

To run our MIPS see MIPS object in main.py

```
