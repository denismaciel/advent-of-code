package main

import (
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

type Instruction struct {
	direction string
	size      int
}

type Ride struct {
	x int
	y int
}

func (r *Ride) move(i Instruction) {
	if i.direction == "down" {
		r.y = r.y + i.size	
	} else if i.direction == "up" {
		r.y = r.y - i.size	
	} else if i.direction == "forward" {
		r.x = r.x + i.size	
	} else {
		log.Fatal("Unknown direction")
	}
}

type Ride2 struct {
	x int
	y int
	aim int
}

func (r *Ride2) move(i Instruction) {
	if i.direction == "down" {
		r.aim = r.aim + i.size	
	} else if i.direction == "up" {
		r.aim = r.aim - i.size	
	} else if i.direction == "forward" {
		r.x = r.x + i.size	
		r.y = r.y + i.size * r.aim
	} else {
		log.Fatal("Unknown direction")
	}
}

func main() {
	file, err := os.OpenFile("input/day02.txt", os.O_RDWR, 0644)
	if err != nil {
		fmt.Println("could not open file")
	}
	defer file.Close()
	contentBytes, err := io.ReadAll(file)
	lines := strings.Split(string(contentBytes), "\n")

	var instructions []Instruction
	
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		words := strings.Split(line, " ")
		direction := words[0]
		size, _ := strconv.Atoi(words[1])
		instructions = append(instructions, Instruction{direction: direction, size: size})
	}
	
	ride := Ride{0, 0}
	ride2 := Ride2{0, 0, 0}
	for _, i := range instructions {
		ride.move(i)
		ride2.move(i)
	}
	fmt.Println(ride.x, ride.y, ride.x * ride.y)
	fmt.Println(ride2.x, ride2.y, ride2.x * ride2.y)
}
