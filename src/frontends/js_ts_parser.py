import json

def parse_js_to_ast(file_path):
    """Stub: Calls a Node.js parser (like Esprima) to extract the JS AST."""
    print(f"[Frontend] Parsing JavaScript file: {file_path}")
    # In a full build, this would pipe to `node parser.js`
    base_ast = {
        "type": "Program",
        "body": [],
        "sourceType": "module"
    }
    return json.dumps(base_ast)
