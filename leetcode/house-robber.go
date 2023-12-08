package main

import "fmt"

func rob(nums []int) int {
    //var total int

    var mem1 []int = []int{0, 0}
    var mem2 []int = []int{0, 0}

    for _, v := range nums {
        if mem1[1] > mem1[0]+v {
            mem2 = []int{mem1[1], v}
        } else {
            mem2 = []int{mem1[1], mem1[0] + v}
        }
        mem2 = []int{mem1[1], max(mem1[0]+v, mem1[1])}
        mem1, mem2 = mem2, mem1
    }

    return mem1[1]
}

func main() {
    fmt.Println(rob([]int{1, 2, 3, 1}))    //4
    fmt.Println(rob([]int{2, 7, 9, 3, 1})) // 12
}
