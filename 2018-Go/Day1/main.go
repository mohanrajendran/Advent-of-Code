package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	inp := readLines("input.txt")
	out1 := addFrequencies(inp)
	out2 := addFrequenciesFindUnique(inp)

	fmt.Println("Part 1:- ", out1)
	fmt.Println("Part 2:- ", out2)
}

func readLines(path string) []string {
	file, err := os.Open(path)
	if err != nil {
		return nil
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}
