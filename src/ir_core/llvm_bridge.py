import os

def generate_base_llvm_ir(module_name="ultra_module"):
    """Creates a universal LLVM IR module targeting Android ARM64 and writes it to disk."""
    print("[IR Core] Generating LLVM IR base...")
    os.makedirs("build_tmp", exist_ok=True)
    
    # Minimal valid LLVM IR text
    llvm_ir_code = """
    define i32 @main() {
        ret i32 0
    }
    """
    
    raw_path = "build_tmp/raw.ll"
    with open(raw_path, "w") as f:
        f.write(llvm_ir_code)
        
    return raw_path
