import os
import subprocess

def test_python_to_apk():
    print("Testing Python -> APK build pipeline...")
    test_file = "test_app.py"
    
    with open(test_file, "w") as f:
        f.write("print('Hello from an Ultra-Compiled Android APK!')")
    
    # Run the Ultra-Compiler pipeline via subprocess
    result = subprocess.run(
        ["python3", "-m", "src.main", test_file, "apk"], 
        capture_output=True, text=True
    )
    
    assert "Build Complete" in result.stdout
    assert os.path.exists("app-release.apk")
    print("Test passed: app-release.apk generated from Python.")
    
    os.remove(test_file)
