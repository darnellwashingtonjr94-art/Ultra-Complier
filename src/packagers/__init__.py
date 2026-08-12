from .apk_builder import assemble_apk
from .wasm_bundler import bundle_wasm_app
from .native_linker import link_native_binary
import os

def package_app(binary_path, target_format):
    os.makedirs("build_tmp/lib/arm64-v8a", exist_ok=True)
    
    if target_format == "apk":
        return assemble_apk(
            "build_tmp", 
            "templates/AndroidManifest.xml", 
            "/opt/android-sdk", 
            "app-release.apk"
        )
    elif target_format == "wasm":
        return bundle_wasm_app(binary_path, "build_tmp/web")
    elif target_format == "native":
        return link_native_binary([binary_path], "output.bin")
        
    return binary_path
