from .llvm_bridge import generate_base_llvm_ir
from .wasm_bridge import generate_wasm_text
from .optimizer import optimize_llvm_ir

def generate_ir(ast_data, target_format):
    if target_format in ["apk", "native", "arm64"]:
        ir_module = generate_base_llvm_ir()
        # Mocking writing to disk and optimizing
        return optimize_llvm_ir("build_tmp/raw.ll", "build_tmp/opt.ll")
        
    elif target_format == "wasm":
        return generate_wasm_text(ast_data)
        
    else:
        # Pass-through for Java bytecode heading to DEX
        return ast_data
