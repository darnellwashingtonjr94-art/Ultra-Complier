plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.ultracompiler.app"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.ultracompiler.app"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }
}
