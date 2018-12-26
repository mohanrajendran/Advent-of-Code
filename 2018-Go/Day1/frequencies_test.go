package main

import "testing"
import "strings"

var samples1 = []struct {
	input  string
	output int64
}{
	{"+1, +1, +1", 3},
	{"+1, +1, -2", 0},
	{"-1, -2, -3", -6},
}

var samples2 = []struct {
	input  string
	output int64
}{
	{"+1, -1", 0},
	{"+3, +3, +4, -2, -4", 10},
	{"-6, +3, +8, +5, -6", 5},
	{"+7, +7, -2, -7, -4", 14},
}

func parse(s string, t *testing.T) []string {
	return strings.Split(s, ", ")
}

func TestAddFrequencies(t *testing.T) {
	for _, sample := range samples1 {
		in := parse(sample.input, t)
		exp := sample.output
		act := addFrequencies(in)

		if exp != act {
			t.Error("Expected: ", exp, ", got: ", act)
		}
	}
}

func TestAddFrequenciesFindUnique(t *testing.T) {
	for _, sample := range samples2 {
		in := parse(sample.input, t)
		exp := sample.output
		act := addFrequenciesFindUnique(in)

		if exp != act {
			t.Error("Expected: ", exp, ", got: ", act)
		}
	}
}
