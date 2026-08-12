import sys
import os
from .frontends import parse_file
from .ir_core import generate_ir
from .backends import generate_binary
from .packagers import package_app

def main():
    if len(sys.argv) < 3:
        print("Error: Usage: ultra-compile <source_file> <target_format>")
        sys.exit(1)
    
    source_file = sys.argv[1]
    target_format = sys.argv[2]
    
    print("--- Ultra-Compiler Pipeline Started ---")
    print(f"Source: {source_file} | Target: {target_format}")
    
    # 1. Parse source into Universal AST/IR
    ast_data = parse_file(source_file)
    
    # 2. Convert to LLVM/Wasm Intermediate Representation
    ir_data = generate_ir(ast_data, target_format)
    
    # 3. Compile to target CPU architecture or Bytecode
    binary_data = generate_binary(ir_data, target_format)
    
    # 4. Package into APK, Wasm Web Shell, or Executable
    final_output = package_app(binary_data, target_format)
    
    print(f"--- Build Complete: {final_output} ---")

if __name__ == "__main__":
    main()
