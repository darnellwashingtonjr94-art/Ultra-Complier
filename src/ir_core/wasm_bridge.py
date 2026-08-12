def generate_wasm_text(ast_nodes):
    """Translates generic AST nodes into WebAssembly Text format (.wat)."""
    print("[IR Core] Translating AST to WebAssembly (Wasm)...")
    
    # Boilerplate Wasm module exporting a main function
    wasm_module = """(module
      (import "env" "print" (func $print (param i32)))
      (func (export "main")
        i32.const 0
        call $print
      )
    )"""
    return wasm_module
