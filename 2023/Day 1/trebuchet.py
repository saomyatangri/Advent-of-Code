import fileinput
import re

def trebuchet(input_file):
    str2num = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    sum = 0
    for line in fileinput.input(files = input_file):
        # for key, val in str2num.items():
        #     line = line.replace(key, val)
        nums = re.findall("\d", line)
        finalnum = int(str(nums[0]) + str(nums[-1]))
        sum += finalnum
    return sum

if __name__ == "__main__":
    print(trebuchet('actual_input.txt'))