import subprocess
import os
import glob

def compile_to_arm64_so(ir_file, ndk_path, output_so):
    """Cross-compiles LLVM IR into an Android arm64-v8a native library."""
    print(f"[Backend] Generating ARM64 .so library: {output_so}")
    
    # Dynamically locate the Clang compiler inside the GitHub Android NDK installation path
    ndk_home = os.environ.get("ANDROID_NDK_HOME", ndk_path)
    toolchain_bin = os.path.join(ndk_home, "toolchains/llvm/prebuilt/linux-x86_64/bin")
    
    # Fallback search if path varies slightly by version
    clang_candidates = glob.glob(os.path.join(toolchain_bin, "*-linux-android*-clang"))
    if clang_candidates:
        clang_path = clang_candidates[0]
    else:
        clang_path = os.path.join(toolchain_bin, "aarch64-linux-android34-clang")

    os.makedirs(os.path.dirname(output_so), exist_ok=True)
    
    subprocess.run(
        [clang_path, "-shared", "-fPIC", ir_file, "-o", output_so], 
        check=True
    )
    return output_so
