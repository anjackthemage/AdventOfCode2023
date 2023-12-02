# Solution for Advent of Code 2023 Day 1

import getopt
import sys

log_level = 2

number_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

number_list = list(number_dict.keys())

first2letters = [item[:2] for item in number_list]

def log(message, level=0):
    if level <= log_level:
        print(message)

def main():
    # So we can provide an input file.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:qv", [])
    except getopt.GetoptError as err:
        log((err), 2)
        sys.exit(2)
    
    input_file = None
    
    # declare global variable so we can updated it
    global log_level
    
    for opt, arg in opts:
        if opt in ("-i"):
            input_file = arg
        elif opt in ("-q"):
            log_level = 0
        elif opt in ("-v"):
            log_level = 4
    
    if input_file is None:
        log(("Error: No input file specified"), 2)
        sys.exit(1)
    
    # Stored the input in a file, so read it.
    with open(input_file, "r") as f:
        lines = f.readlines()
    
    total = 0
    for line in lines:
        log(("\n" + line), 2)
        letter_lookup = ""
        firstnum = -1
        lastnum = -1
        for index in range(len(line)):
            char = line[index]
            if char == "\n":
                continue
            log(("char: " + char + " index: " + str(index)), 3)
            # Parse though each line storing the first and last number we come across.
            if char.isdigit():
                log(("char is digit"), 3)
                if firstnum == -1:
                    firstnum = int(char)
                    log(("firstnum: " + str(firstnum)), 3)
                # This will always equal the last number read in a line.
                lastnum = int(char)
                log(("lastnum: " + str(lastnum)), 3)
            else:
                log(("char is not digit"), 3)
                if (index + 1) >= len(line):
                    continue
                letter_lookup = line[index:index + 2]
                log(("letter_lookup: " + letter_lookup), 3)
                if letter_lookup in first2letters:
                    word_test = ""
                    potential_word = number_list[first2letters.index(letter_lookup)]
                    log(("potential_word: " + potential_word), 3)
                    check_len = len(potential_word)  # Storing word length
                    if (index + check_len - 1) >= len(line):
                        log(("index + check_len >= len(line)"), 3)
                        continue
                    log(("word fits"), 3)
                    for charindex in range(index, index + check_len):
                        word_test += line[charindex]
                    log(("word_test: " + word_test), 3)
                    if word_test == potential_word:
                        log(("word_test == potential_word"), 3)
                        if firstnum == -1:
                            firstnum = number_dict[potential_word]
                            log(("firstnum: " + str(firstnum)), 3)
                        lastnum = number_dict[potential_word]
                        log(("lastnum: " + str(lastnum)), 3)
                    
        # Good ol' print debugging. (copilot autocompleted this comment from "Good ol'")
        log(("firstnum: " + str(firstnum) + " lastnum: " + str(lastnum)), 1)
        line_total = (firstnum * 10) + lastnum
        log(("line_total: " + str(line_total)), 1)
        total += line_total
        log(("total: " + str(total)), 1)
    # Et voila!
    log((total), 0)
                
    
if __name__ == "__main__":
    main()
