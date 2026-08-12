import subprocess

def link_native_binary(object_files, output_executable):
    """Links object files into a native executable for desktop targets."""
    print(f"[Packager] Linking native executable: {output_executable}")
    subprocess.run(["gcc", *object_files, "-o", output_executable], check=True)
    return output_executable
