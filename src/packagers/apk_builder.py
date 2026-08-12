import subprocess
import os
import zipfile

def assemble_apk(build_dir, manifest_path, sdk_path, output_apk):
    """Assembles, aligns, and signs a runnable Android APK."""
    print(f"[Packager] Assembling APK -> {output_apk}")
    aapt2 = os.path.join(sdk_path, "build-tools", "34.0.0", "aapt2")
    zipalign = os.path.join(sdk_path, "build-tools", "34.0.0", "zipalign")
    apksigner = os.path.join(sdk_path, "build-tools", "34.0.0", "apksigner")
    android_jar = os.path.join(sdk_path, "platforms", "android-34", "android.jar")

    unaligned_apk = os.path.join(build_dir, "app-unaligned.apk")

    # 1. Compile manifest and package assets
    subprocess.run([
        aapt2, "link", "-o", unaligned_apk, 
        "--manifest", manifest_path, 
        "-I", android_jar, 
        os.path.join(build_dir, "dex", "classes.dex")
    ], check=True)

    # 2. Inject native shared libraries into APK
    with zipfile.ZipFile(unaligned_apk, 'a') as zip_ref:
        for root, _, files in os.walk(os.path.join(build_dir, "lib")):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, build_dir)
                zip_ref.write(filepath, arcname)

    # 3. Memory-align and Cryptographically sign
    aligned_apk = os.path.join(build_dir, "app-aligned.apk")
    subprocess.run([zipalign, "-v", "4", unaligned_apk, aligned_apk], check=True)
    subprocess.run([
        apksigner, "sign", 
        "--ks", "templates/debug.keystore", 
        "--ks-pass", "pass:android", 
        "--out", output_apk, aligned_apk
    ], check=True)

    return output_apk
