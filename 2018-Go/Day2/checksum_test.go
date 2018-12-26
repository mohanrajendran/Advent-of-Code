package main

import "testing"

var samples1 = struct {
	input  []string
	output int
}{
	[]string{"abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"}, 12,
}

var samples2 = struct {
	input  []string
	output string
}{
	[]string{"abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"}, "fgij",
}

func TestComputeChecksum(t *testing.T) {
	actual := computeChecksum(samples1.input)
	if actual != samples1.output {
		t.Error("Expected: ", samples1.output, ", got: ", actual)
	}
}

func TestComputeDiffForMinDistance(t *testing.T) {
	actual := computeDiffForMinDistance(samples2.input)
	if actual != samples2.output {
		t.Error("Expected: ", samples2.output, ", got: ", actual)
	}
}
