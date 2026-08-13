import os
import subprocess
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Ultra-Compiler API Bridge")

# Define the expected incoming data structure
class CodePayload(BaseModel):
    language: str
    source_code: str
    target_format: str = "wasm"  # Defaulting to WebAssembly for the web shell

@app.post("/api/compile")
async def compile_code(payload: CodePayload):
    # Map languages to their correct file extensions
    ext_map = {
        "python": ".py", 
        "cpp": ".cpp", 
        "java": ".java", 
        "javascript": ".js"
    }
    
    file_ext = ext_map.get(payload.language, ".txt")
    temp_filepath = f"temp_workspace/temp_source{file_ext}"
    
    os.makedirs("temp_workspace", exist_ok=True)
    
    # 1. Write the web editor's code to a temporary physical file
    with open(temp_filepath, "w") as f:
        f.write(payload.source_code)
        
    try:
        # 2. Execute the Ultra-Compiler main orchestrator via subprocess
        # This matches the CLI expected by your bin/ultra-compile entrypoint
        result = subprocess.run(
            ["python3", "-m", "src.main", temp_filepath, payload.target_format],
            capture_output=True,
            text=True,
            check=True
        )
        output_log = result.stdout
        
    except subprocess.CalledProcessError as e:
        output_log = f"Compilation Error:\n{e.stderr}\n{e.stdout}"
        
    finally:
        # 3. Clean up the temporary workspace
        if os.path.exists(temp_filepath):
            os.remove(temp_filepath)
            
    # 4. Return the compiler's output back to the browser console
    return {"status": "complete", "terminal_output": output_log}

if __name__ == "__main__":
    # Runs the server on port 8080 (matching the Dockerfile configuration)
    uvicorn.run(app, host="0.0.0.0", port=8080)
