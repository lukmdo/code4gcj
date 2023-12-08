package main

import "fmt"

func numberOfMatches(n int) int {
	var total int

	for n > 1 {
		if n%2 == 1 {
			total += (n - 1) / 2
			n = (n-1)/2 + 1
		} else {
			total += n / 2
			n = n / 2
		}
	}

	return total
}

func main() {
	fmt.Println(numberOfMatches(7))  // 6
	fmt.Println(numberOfMatches(14)) // 13

}
