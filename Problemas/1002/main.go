package main

import (
    "fmt"
)

func main() {
	var raio float64
	var pi = 3.14159
	fmt.Scanln(&raio)

	var area = (raio * raio) * pi

    fmt.Printf("A=%.4f\n", area)
}