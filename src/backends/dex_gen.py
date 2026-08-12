import subprocess
import os
import glob

def compile_classes_to_dex(class_dir, sdk_path, output_dir):
    """Converts Java .class bytecode into Android Dalvik (DEX) format."""
    print(f"[Backend] Converting bytecode to DEX in {output_dir}")
    
    d8_path = os.path.join(sdk_path, "build-tools", "34.0.0", "d8")
    class_files = glob.glob(os.path.join(class_dir, "*.class"))
    
    subprocess.run([d8_path, *class_files, "--output", output_dir], check=True)
    return os.path.join(output_dir, "classes.dex")
