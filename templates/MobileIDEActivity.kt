package com.ultracompiler.ide

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.io.File
import java.io.BufferedReader
import java.io.InputStreamReader

class MobileIDEActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme(colorScheme = darkColorScheme()) {
                Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                    IDEInterfaceScreen(applicationContext.filesDir)
                }
            }
        }
    }
}

@Composable
fun IDEInterfaceScreen(filesDir: File) {
    var codeInput by remember { mutableStateOf("print('Ultra-Compiler Mobile Execution Pipeline Active')") }
    var targetFormat by remember { mutableStateOf("apk") }
    var consoleOutput by remember { mutableStateOf("System initialized. Ready...") }
    val coroutineScope = rememberCoroutineScope()
    val scrollState = rememberScrollState()

    Column(modifier = Modifier.fillMaxSize().padding(16.dp)) {
        Text("Ultra-Compiler Mobile IDE", style = MaterialTheme.typography.titleLarge)
        Spacer(modifier = Modifier.height(8.dp))

        // Code Editor Window
        Box(
            modifier = Modifier
                .weight(1f)
                .fillMaxWidth()
                .background(Color(0xFF1E1E1E))
                .padding(12.dp)
        ) {
            BasicTextField(
                value = codeInput,
                onValueChange = { codeInput = it },
                textStyle = TextStyle(color = Color(0xFF4CAF50), fontSize = 14.sp),
                modifier = Modifier.fillMaxSize()
            )
        }

        Spacer(modifier = Modifier.height(8.dp))

        // Control Panel Row
        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
            Button(onClick = { targetFormat = if (targetFormat == "apk") "wasm" else "apk" }) {
                Text("Target: ${targetFormat.uppercase()}")
            }
            Button(onClick = {
                coroutineScope.launch {
                    consoleOutput = "Compiling code block to $targetFormat..."
                    val result = executePipeline(filesDir, codeInput, targetFormat)
                    consoleOutput = result
                }
            }) {
                Text("Compile & Build")
            }
        }

        Spacer(modifier = Modifier.height(8.dp))

        // Terminal Console Output Window
        Box(
            modifier = Modifier
                .height(130.dp)
                .fillMaxWidth()
                .background(Color.Black)
                .padding(8.dp)
                .verticalScroll(scrollState)
        ) {
            Text(text = consoleOutput, color = Color.White, fontSize = 12.sp)
        }
    }
}

suspend fun executePipeline(filesDir: File, codeContent: String, target: String): String = withContext(Dispatchers.IO) {
    try {
        val tempSource = File(filesDir, "temp_source.py")
        tempSource.writeText(codeContent)

        val processBuilder = ProcessBuilder("python3", "-m", "src.main", tempSource.absolutePath, target)
        processBuilder.directory(filesDir.parentFile)
        processBuilder.redirectErrorStream(true)
        
        val process = processBuilder.start()
        val reader = BufferedReader(InputStreamReader(process.inputStream))
        val output = StringBuilder()
        var line: String? = reader.readLine()
        while (line != null) {
            output.append(line).append("\n")
            line = reader.readLine()
        }
        process.waitFor()
        output.toString()
    } catch (e: Exception) {
        "Compilation Exception: ${e.localizedMessage}"
    }
}
