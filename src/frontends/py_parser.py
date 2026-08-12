import ast

def parse_py_to_ast(file_path):
    """Uses Python's built-in AST module to parse Python source code."""
    print(f"[Frontend] Parsing Python file: {file_path}")
    with open(file_path, "r") as f:
        source_code = f.read()
    
    syntax_tree = ast.parse(source_code)
    return syntax_tree
