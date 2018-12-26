package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func addFrequencies(inp []string) int64 {
	var sum int64

	for _, v := range inp {
		i, err := strconv.ParseInt(v, 10, 64)
		if err == nil {
			sum += i
		}
	}

	return sum
}

func addFrequenciesFindUnique(inp []string) int64 {
	m := make(map[int64]bool)
	m[0] = true

	found := false
	var result int64
	var sum int64

	for !found {
		for _, v := range inp {
			i, err := strconv.ParseInt(v, 10, 64)
			if err == nil {
				sum += i
			}

			if m[sum] {
				found = true
				result = sum
				break
			} else {
				m[sum] = true
			}
		}
	}

	return result
}

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
