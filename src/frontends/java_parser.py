import subprocess

def parse_java_to_bytecode(file_path, output_dir):
    """Compiles Java directly to standard bytecode (.class)."""
    print(f"[Frontend] Parsing Java file: {file_path}")
    subprocess.run(["javac", file_path, "-d", output_dir], check=True)
    return output_dir
