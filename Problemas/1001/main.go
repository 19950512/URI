package main

import (
    "fmt"
)

func main() {
	var a int
	var b int

	fmt.Scanln(&a)
	fmt.Scanln(&b) 
	result := a + b
	fmt.Println("X =", result)
}