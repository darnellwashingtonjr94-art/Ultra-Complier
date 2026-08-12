import subprocess
import os

def compile_to_arm64_so(ir_file, ndk_path, output_so):
    """Cross-compiles LLVM IR into an Android arm64-v8a native library."""
    print(f"[Backend] Generating ARM64 .so library: {output_so}")
    
    clang_path = os.path.join(
        ndk_path, 
        "toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android34-clang"
    )
    
    subprocess.run(
        [clang_path, "-shared", "-fPIC", ir_file, "-o", output_so], 
        check=True
    )
    return output_so
