#include <android/native_activity.h>
#include <android/log.h>

#define LOG_TAG "UltraCompilerNative"
#define LOGI(...) __android_log_print(ANDROID_LOG_INFO, LOG_TAG, __VA_ARGS__)

void ANativeActivity_onCreate(ANativeActivity* activity, void* savedState, size_t savedStateSize) {
    LOGI("NativeActivity initialized by Ultra-Compiler harness.");
    // Native UI event loop or engine loop connects here
}
