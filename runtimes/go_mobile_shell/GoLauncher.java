package com.ultracompiler.go;

import android.app.Activity;
import android.os.Bundle;

public class GoLauncher extends Activity {
    // Loads the Go shared library compiled in Script #18
    static {
        System.loadLibrary("main"); 
    }

    public native void initGoRuntime();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        initGoRuntime();
    }
}
