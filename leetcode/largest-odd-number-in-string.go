package main

import (
	"fmt"
)

func largestOddNumber(num string) string {
	var n int = len(num)
	var odd_digs = map[byte]struct{}{
		'1': {},
		'3': {},
		'5': {},
		'7': {},
		'9': {},
	}

	for i := 1; i <= n; i++ {
		if _, ok := odd_digs[num[n-i]]; ok {
			return num[:n-i+1]
		}
	}

	return ""
}

func largestOddNumber2(num string) string {
	var n int = len(num)

	for i := 1; i <= n; i++ {
		if (num[n-i]-'0')%2 != 0 {
			return num[:n-i+1]
		}
	}

	return ""
}

func main() {
	fmt.Println(largestOddNumber("52"))    // "5"
	fmt.Println(largestOddNumber("4206"))  // ""
	fmt.Println(largestOddNumber("35427")) // "35427"
}
