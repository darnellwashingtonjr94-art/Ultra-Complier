from .arm64_gen import compile_to_arm64_so
from .dex_gen import compile_classes_to_dex
from .c_transpiler import transpile_ast_to_c

def generate_binary(ir_data, target_format):
    if target_format == "apk":
        # If the pipeline sent Java bytecode path
        if isinstance(ir_data, str) and ir_data.endswith("classes"):
            return compile_classes_to_dex(ir_data, "/opt/android-sdk", "build_tmp/dex")
        else:
            return compile_to_arm64_so("build_tmp/opt.ll", "/opt/android-ndk", "build_tmp/lib/libmain.so")
    elif target_format == "c":
        return transpile_ast_to_c(ir_data, "build_tmp/output.c")
        
    return ir_data
