package com.ultracompiler.ide

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import java.io.File

class MobileIDEActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme(colorScheme = darkColorScheme()) {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    MobileIDEScreen()
                }
            }
        }
    }
}

@Composable
fun MobileIDEScreen() {
    var codeInput by remember { mutableStateOf("// Write your code here (Python, C++, JS, Rust)\nprint('Hello from Ultra-Compiler IDE')") }
    var targetFormat by remember { mutableStateOf("apk") }
    var buildOutput by remember { mutableStateOf("Ready to compile...") }

    Column(modifier = Modifier.fillMaxSize().padding(16.dp)) {
        Text("Ultra-Compiler Mobile IDE", style = MaterialTheme.typography.titleLarge)
        Spacer(modifier = Modifier.height(8.dp))

        // Code Editor Box
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
                textStyle = TextStyle(color = Color.Green, fontSize = 14.sp),
                modifier = Modifier.fillMaxSize()
            )
        }

        Spacer(modifier = Modifier.height(8.dp))

        // Target Selector & Build Button
        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
            Button(onClick = { targetFormat = "apk" }) { Text("Target: APK") }
            Button(onClick = {
                buildOutput = "Compiling to $targetFormat via LLVM pipeline..."
                // Trigger local compilation backend logic here
            }) {
                Text("Compile & Build")
            }
        }

        Spacer(modifier = Modifier.height(8.dp))

        // Console Output Terminal
        Box(
            modifier = Modifier
                .height(120.dp)
                .fillMaxWidth()
                .background(Color.Black)
                .padding(8.dp)
        ) {
            Text(text = buildOutput, color = Color.White, fontSize = 12.sp)
        }
    }
}
