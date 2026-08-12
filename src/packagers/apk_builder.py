import os
import subprocess

# In apk_builder.py
android_home = os.environ.get('ANDROID_HOME', '/opt/android-sdk')
aapt2_path = os.path.join(android_home, 'build-tools', '34.0.0', 'aapt2')

# Then use aapt2_path in your subprocess call
subprocess.run([aapt2_path, "compile", ...])
