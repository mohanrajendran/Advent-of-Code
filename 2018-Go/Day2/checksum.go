package main

import (
	"bufio"
	"fmt"
	"os"
)

type result struct {
	hasTwice  bool
	hasThrice bool
}

func processString(inp string) result {
	m := make(map[rune]int)

	for _, c := range inp {
		m[c] = m[c] + 1
	}

	var res result

	for _, count := range m {
		if count == 2 {
			res.hasTwice = true
		} else if count == 3 {
			res.hasThrice = true
		}
	}

	return res
}

func computeChecksum(inp []string) int {
	var twiceCount, thriceCount int

	for _, i := range inp {
		r := processString(i)
		if r.hasTwice {
			twiceCount++
		}
		if r.hasThrice {
			thriceCount++
		}
	}

	return twiceCount * thriceCount
}

func hammingDistance(a, b string) int {
	l := len(a)
	diff := 0

	for i := 0; i < l; i++ {
		if a[i] != b[i] {
			diff++
		}
	}

	return diff
}

func diff(a, b string) string {
	l := len(a)
	loc := -1

	for i := 0; i < l; i++ {
		if a[i] != b[i] {
			loc = i
			break
		}
	}

	return a[0:loc] + a[loc+1:l]
}

func computeDiffForMinDistance(inp []string) string {
	l := len(inp)
	for i := 0; i < l; i++ {
		for j := i + 1; j < l; j++ {
			if hammingDistance(inp[i], inp[j]) == 1 {
				return diff(inp[i], inp[j])
			}
		}
	}
	return ""
}

func main() {
	inp := readLines("input.txt")
	out1 := computeChecksum(inp)
	out2 := computeDiffForMinDistance(inp)

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
