# Solution for Advent of Code 2023 Day 1

import getopt
import sys

def main():
    # So we can provide an input file.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:", [])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    
    input_file = None
    
    for opt, arg in opts:
        print(opt, arg )
        if opt in ("-i"):
            input_file = arg
    
    if input_file is None:
        print("Error: No input file specified")
        sys.exit(1)
    
    # Stored the input in a file, so read it.
    with open(input_file, "r") as f:
        lines = f.readlines()
    
    total = 0
    for line in lines:
        firstnum = ""
        lastnum = ""
        for char in line:
            # Parse though each line storing the first and last number we come across.
            if char.isdigit():
                if firstnum == "":
                    firstnum = char
                # This will always equal the last number read in a line.
                lastnum = char
        # Good ol' print debugging. (copilot autocompleted this comment from "Good ol'")
        print(firstnum + lastnum)
        total += int(firstnum + lastnum)
    # Et voila!
    print(total)
                
    
if __name__ == "__main__":
    main()
