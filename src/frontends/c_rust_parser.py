import subprocess

def parse_c_to_ast(file_path):
    """Uses Clang to dump the AST of a C/C++ file into a readable format."""
    print(f"[Frontend] Parsing C/C++ file: {file_path}")
    result = subprocess.run(
        ["clang", "-Xclang", "-ast-dump", "-fsyntax-only", file_path],
        capture_output=True, text=True
    )
    return result.stdout
