import json

def generate_wasm_text(ast_nodes):
    """
    Translates generic AST nodes into WebAssembly Text Format (WAT).
    This acts as the bridge between the IR Core and the final WASM Bundler.
    """
    # Initialize the WASM module and import the environment print function
    wat_lines = [
        "(module", 
        '  (import "env" "print" (func $print (param i32)))'
    ]
    
    # Define the main exported function
    wat_lines.append('  (func $main (export "main")')
    
    # Dynamically parse the AST nodes
    if isinstance(ast_nodes, dict) and ast_nodes.get("type") == "Program":
        for node in ast_nodes.get("body", []):
            
            # Example translation: Variable Declarations / Expressions
            if node.get("type") == "ExpressionStatement":
                # In a full compiler, you'd traverse the expression tree to calculate values.
                # Here we map a basic numerical constant to the WASM stack.
                val = node.get("value", 0) 
                wat_lines.append(f"    i32.const {val}")
                wat_lines.append("    call $print")
                
            # Example translation: Return Statements
            elif node.get("type") == "ReturnStatement":
                wat_lines.append("    return")
                
    else:
        # Fallback for empty or invalid AST
        wat_lines.append("    ;; No executable AST nodes found")
        wat_lines.append("    i32.const 0")
        wat_lines.append("    call $print")

    # Close the function and the module
    wat_lines.append("  )")
    wat_lines.append(")")
    
    return "\n".join(wat_lines)
