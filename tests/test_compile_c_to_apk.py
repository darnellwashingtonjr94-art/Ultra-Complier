import os
import subprocess

def test_c_to_apk():
    print("Testing C -> Native APK build pipeline...")
    test_file = "test_game.c"
    
    with open(test_file, "w") as f:
        f.write("int main() { return 0; }")
    
    result = subprocess.run(
        ["python3", "-m", "src.main", test_file, "apk"], 
        capture_output=True, text=True
    )
    
    assert "Build Complete" in result.stdout
    assert os.path.exists("app-release.apk")
    print("Test passed: Native APK generated via LLVM pipeline.")
    
    os.remove(test_file)
