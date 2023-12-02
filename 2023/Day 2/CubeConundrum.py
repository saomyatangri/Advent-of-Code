import fileinput
import re

def cube_conundrum_part1(input_file):
    color_finals = {
        "red": 12, 
        "green": 13,
        "blue": 14,  
    }

    index = 1
    index_sum = 0
    is_valid = True
    for line in fileinput.input(files = input_file):
        split_line = re.split(':|,|;', line)
        split_line.pop(0)
        print(split_line)
        for section in split_line:
            roll = section.split()

            val = int(roll[0])
            key = roll[1]
            
            if (color_finals[key] < val):
                print(key + " is illegal, val = " + str(val) + "\tcurrsum: " + str(index_sum))
                is_valid = False
                break
        if (is_valid):
            print()
            index_sum += index
        is_valid = True
        index+=1
    return index_sum
        



if __name__ == "__main__":
    print(cube_conundrum_part1('actual_input.txt'))