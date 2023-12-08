package main

import "fmt"

func minCostClimbingStairs(cost []int) int {
	dp := map[int]int{0: cost[0], 1: cost[1]}

	n := len(cost)
	for i := 2; i < n-1; i++ {
		dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
	}

	dp[n-1] = min(dp[n-3]+cost[n-1], dp[n-2])

	return dp[n-1]
}

func main() {
	fmt.Println(minCostClimbingStairs([]int{10, 15, 20}))                         // 15
	fmt.Println(minCostClimbingStairs([]int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1})) // 6
}
