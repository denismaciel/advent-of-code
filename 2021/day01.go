package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

const input = `199
200
208
210
200
207
240
269
260
263`

func loadInput() string {
	file, err := os.OpenFile("input/day01.txt", os.O_RDWR, 0644)
	if err != nil {
		fmt.Println("could not open file")
	}
	defer file.Close()
	content, err := io.ReadAll(file)
	return string(content)
}

func ProcessInput(rawInput string) []int {
	measure := strings.Split(rawInput, "\n")

	var output []int
	for _, x := range measure {
		i, err := strconv.Atoi(x)
		if err == nil {
			output = append(output, i)
		} else {
			fmt.Println(err)
		}
	}
	return output
}

func CountIncrease(measure []int) int {
	var acc int
	for i := range measure {
		if measure[i] < measure[i+1] {
			acc++
		}
		if i == len(measure)-2 {
			break
		}
	}
	return acc
}

func PartOne(input []int) {
	count := CountIncrease(input)
	fmt.Println(count)
}

func sum(array [3]int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func PartTwo(input []int) {
	var wins [][3]int

	for i := 1; i < len(input)-2; i++ {
		wins = append(wins, [3]int{input[i], input[i+1], input[i+2]})
	}
	var winSum []int
	for _, w := range wins {
		winSum = append(winSum, sum(w))
	}
	count := CountIncrease(winSum)
	fmt.Println(count)
}

func main() {
	puzzleInput := loadInput()
	processed := ProcessInput(puzzleInput)
	PartOne(processed)
	PartTwo(processed)
}
