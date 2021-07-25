package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func loadData() map[int]bool {
	data, _ := ioutil.ReadFile("./input/day01.txt")
	scanner := bufio.NewScanner(strings.NewReader(string(data)))

	nums := map[int]bool{}
	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		nums[num] = true
	}
	return nums
}

func part1(nums map[int]bool) {
	for num1 := range nums {
		num2 := 2020 - num1
		if nums[num2] {
			fmt.Println(num1, num2, num1*num2)
			break
		}
	}
}

func part2(nums map[int]bool) {

outer:
	for num1 := range nums {
		for num2 := range nums {
			num3 := 2020 - num1 - num2
			if nums[num3] {
				fmt.Println(num1, num2, num3, num1*num2*num3)
				break outer
			}

		}
	}
}

func main() {
	nums := loadData()
	part1(nums)
	part2(nums)
}
