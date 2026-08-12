from llvmlite import ir

def generate_base_llvm_ir(module_name="ultra_module"):
    """Creates a universal LLVM IR module targeting Android ARM64."""
    print("[IR Core] Generating LLVM IR base...")
    module = ir.Module(name=module_name)
    # Set target architecture for Android hardware
    module.triple = "aarch64-none-linux-android"
    return module
