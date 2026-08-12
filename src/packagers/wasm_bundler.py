import os

def bundle_wasm_app(wasm_file, output_dir):
    """Wraps a WebAssembly module in an HTML/JS launcher page."""
    print(f"[Packager] Bundling Wasm application in {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    
    html_content = """<!DOCTYPE html>
<html>
<head><title>Ultra-Compiler Wasm App</title></head>
<body>
  <script>
    WebAssembly.instantiateStreaming(fetch('app.wasm')).then(obj => {
      obj.instance.exports.main();
    });
  </script>
</body>
</html>"""
    
    with open(os.path.join(output_dir, "index.html"), "w") as f:
        f.write(html_content)
    return os.path.join(output_dir, "index.html")
