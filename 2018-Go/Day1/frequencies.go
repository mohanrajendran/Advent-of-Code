package main

import (
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
