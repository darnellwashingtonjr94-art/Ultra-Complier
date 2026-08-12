import os
from .c_rust_parser import parse_c_to_ast
from .py_parser import parse_py_to_ast
from .js_ts_parser import parse_js_to_ast
from .java_parser import parse_java_to_bytecode

def parse_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.c', '.cpp', '.rs']:
        return parse_c_to_ast(file_path)
    elif ext == '.py':
        return parse_py_to_ast(file_path)
    elif ext in ['.js', '.ts']:
        return parse_js_to_ast(file_path)
    elif ext in ['.java', '.kt']:
        # Java skips standard AST and goes straight to JVM bytecode
        os.makedirs("build_tmp/classes", exist_ok=True)
        return parse_java_to_bytecode(file_path, "build_tmp/classes")
    else:
        raise ValueError(f"Unsupported extension for Ultra-Compiler: {ext}")
