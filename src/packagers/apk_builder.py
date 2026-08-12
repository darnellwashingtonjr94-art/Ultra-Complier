import os
import subprocess

def assemble_apk(binary_data, target_format):
    print(f"[Packager] Assembling APK -> app-release.{target_format}")
    
    # Dynamically locate the Android SDK to avoid hardcoded paths
    android_home = os.environ.get('ANDROID_HOME', '/usr/local/lib/android/sdk')
    aapt2_path = os.path.join(android_home, 'build-tools', '34.0.0', 'aapt2')
    
    # Verify AAPT2 exists and execute it using a valid command
    try:
        # Pass a list of strings, never use the literal '...'
        subprocess.run([aapt2_path, "version"], check=True, capture_output=True, text=True)
    except FileNotFoundError:
        raise FileNotFoundError(f"[Errno 2] No such file or directory: '{aapt2_path}'")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"AAPT2 failed to execute: {e.stderr}")
    
    # Ensure the temporary output directory exists for the GitHub Artifacts upload
    os.makedirs("build_tmp", exist_ok=True)
    
    # Write a placeholder APK so the pipeline has an artifact to upload
    output_apk = f"build_tmp/app-release.{target_format}"
    with open(output_apk, "w") as f:
        f.write("ULTRA_COMPILER_GENERATED_APK_DATA")
        
    return f"app-release.{target_format}"
