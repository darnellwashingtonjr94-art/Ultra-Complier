import subprocess
import json
import os

def parse_c_to_ast(file_path):
    """
    Uses Clang to dump the AST of a C/C++ file into a universal JSON format,
    standardizing it for the Ultra-Compiler pipeline.
    """
    if not os.path.exists(file_path):
        return {"status": "error", "message": f"Source file not found: {file_path}"}
        
    print(f"[Frontend] Parsing C/C++ file: {file_path}")
    
    try:
        # Execute Clang and force AST output in JSON format
        # -fsyntax-only ensures it only parses and doesn't try to compile
        result = subprocess.run(
            ["clang", "-Xclang", "-ast-dump=json", "-fsyntax-only", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Load the raw Clang JSON output
        raw_ast = json.loads(result.stdout)
        
        # Map the heavy Clang AST to the Ultra-Compiler Universal IR format
        universal_ast = {
            "type": "Program",
            "source_language": "c_cpp",
            "body": raw_ast.get("inner", []),
            "metadata": {
                "original_file": file_path
            }
        }
        
        return universal_ast
        
    except subprocess.CalledProcessError as e:
        print(f"[Error] Clang parsing failed during AST generation:\n{e.stderr}")
        return {"type": "Error", "details": e.stderr}
        
    except json.JSONDecodeError:
        print("[Error] Failed to decode Clang AST JSON output.")
        return {"type": "Error", "details": "JSON Decode Failure"}
