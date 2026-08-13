import os
import subprocess

def ensure_gradle_environment(output_dir):
    """Ensures settings.gradle.kts, build.gradle.kts, and gradlew exist before building."""
    os.makedirs(output_dir, exist_ok=True)
    
    settings_file = os.path.join(output_dir, "settings.gradle.kts")
    if not os.path.exists(settings_file):
        with open(settings_file, "w") as f:
            f.write('rootProject.name = "UltraCompilerApp"\ninclude(":app")\n')

    build_gradle = os.path.join(output_dir, "build.gradle.kts")
    if not os.path.exists(build_gradle):
        with open(build_gradle, "w") as f:
            f.write('plugins {\n    id("com.android.application") version "8.2.0" apply false\n}\n')

    gradlew_path = os.path.join(output_dir, "gradlew")
    if not os.path.exists(gradlew_path):
        print("[Packager] Gradle wrapper missing. Generating wrapper...")
        subprocess.run(["gradle", "wrapper", "--project-dir", output_dir], check=True)

def assemble_apk(binary_path, output_dir, manifest_path):
    print(f"[Packager] Building APK for binary: {binary_path}")
    ensure_gradle_environment(output_dir)
    
    gradlew = os.path.join(output_dir, "gradlew")
    if os.path-exists(gradlew):
        os.chmod(gradlew, 0o755)
        subprocess.run([gradlew, "assembleDebug", "-p", output_dir], check=True)
    
    print("[Packager] APK compilation complete.")
    return os.path.join(output_dir, "app/build/outputs/apk/debug/app-debug.apk")
