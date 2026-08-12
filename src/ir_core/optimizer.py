import subprocess

def optimize_llvm_ir(ir_file_path, output_path):
    """Runs LLVM's 'opt' tool for dead-code elimination and shrinking."""
    print(f"[Optimizer] Running O3 optimizations on {ir_file_path}")
    subprocess.run(["opt", "-O3", ir_file_path, "-o", output_path], check=True)
    return output_path
