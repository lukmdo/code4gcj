package main

import "fmt"

func climbStairs(n int) int {
	mem1 := []int{1, 2}
	mem2 := make([]int, 2)

	for i := 0; i < n-1; i++ {
		mem2 = []int{mem1[1], mem1[0] + mem1[1]}
		mem1, mem2 = mem2, mem1
	}

	return mem1[0]
}

func main() {
	fmt.Println(climbStairs(1))
	fmt.Println(climbStairs(2))
	fmt.Println(climbStairs(3))
	fmt.Println(climbStairs(4))
}
