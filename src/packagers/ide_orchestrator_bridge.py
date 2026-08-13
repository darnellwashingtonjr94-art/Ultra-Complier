import sys
import os
import json
import subprocess

def run_ide_compilation(source_file_path, target_format="apk"):
    """
    Directly bridges the Mobile IDE input to the Ultra-Compiler main pipeline.
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    main_script = os.path.join(project_root, "src", "main.py")
    
    if not os.path.exists(source_file_path):
        return {"status": "error", "message": f"Source file not found: {source_file_path}"}
    
    try:
        # Execute the main compilation orchestrator pipeline
        result = subprocess.run(
            [sys.executable, main_script, source_file_path, target_format],
            capture_output=True,
            text=True,
            check=True
        
        return {
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "stdout": e.stdout,
            "stderr": e.stderr
        }

if __name__ == "__main__":
    if len(sys.argv) > 2:
        output = run_ide_compilation(sys.argv[1], sys.argv[2])
        print(json.dumps(output))
