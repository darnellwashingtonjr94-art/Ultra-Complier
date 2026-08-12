package main

/*
#cgo LDFLAGS: -landroid -llog
*/
import "C"
import "fmt"

//export Java_com_ultracompiler_go_GoLauncher_initGoRuntime
func Java_com_ultracompiler_go_GoLauncher_initGoRuntime() {
	fmt.Println("[Go Runtime] Initialized on Android via JNI")
}

func main() {}
