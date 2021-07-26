package main 


import (
    "bufio"
    "fmt"
    // "io/ioutil"
    // "strings"
    "os"
    "strings"
    "strconv"
)

type password struct {
    lo int
    hi int
    letter string
    content string
}

func loadLines() []string {
    
    scanner := bufio.NewScanner(os.Stdin)

    var rawLines []string
    for scanner.Scan() {
        rawLines = append(rawLines, scanner.Text())
    }
    return rawLines
}

func parsePassword(rawPwd string) password {
    fields := strings.Split(rawPwd, " ") 

    dashPos := strings.Index(fields[0], "-")
    lo, _:= strconv.Atoi(string(fields[0][:dashPos]))
    hi, _ := strconv.Atoi(fields[0][dashPos+1:])

    letter := fields[1][0]

    content := fields[2]

    return password{lo, hi, string(letter), content}
}

func parsePasswords(rawLines []string) []password {
    var pwds []password
    for _, line := range rawLines {
        pwds = append(pwds, parsePassword(line))
    }
    return pwds
}

func (p password) countLetter() int {
    return strings.Count(p.content, p.letter)
}

func (p password) isValid() bool {
    count := p.countLetter()
    return p.lo <= count && count <= p.hi
}

func main() {
    rawLines := loadLines()
    pwds := parsePasswords(rawLines)

    var nValid int
    for _, p := range pwds {
        if p.isValid() {
            nValid++
        }
    }
    fmt.Println(nValid)
}
