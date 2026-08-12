#include <jni.h>
#include <Python.h>
#include <android/log.h>

JNIEXPORT void JNICALL
Java_com_ultracompiler_python_PyLauncher_runPythonScript(JNIEnv* env, jobject obj, jstring script_path) {
    const char* path = (*env)->GetStringUTFChars(env, script_path, NULL);
    Py_Initialize();
    FILE* fp = fopen(path, "r");
    if (fp) {
        PyRun_SimpleFile(fp, path);
        fclose(fp);
    }
    Py_Finalize();
    (*env)->ReleaseStringUTFChars(env, script_path, path);
}
