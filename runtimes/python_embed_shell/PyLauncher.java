package com.ultracompiler.python;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;

public class PyLauncher extends Activity {
    // Loads the C lib we built in Script #17
    static {
        System.loadLibrary("pyrunner");
    }

    // JNI Bridge hook
    public native void runPythonScript(String scriptPath);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.i("UltraCompiler", "Booting Embedded Python Runtime...");
        
        // Locate bundled Python script in APK assets
        String scriptPath = getApplicationInfo().dataDir + "/assets/main.py";
        runPythonScript(scriptPath);
    }
}
