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
        for section in split_line:
            roll = section.split()

            val = int(roll[0])
            key = roll[1]
            
            if (color_finals[key] < val):
                is_valid = False
                break
        if (is_valid):
            index_sum += index
        is_valid = True
        index+=1
    return index_sum
        
def cube_conundrum_part2(input_file):
    leaderboard = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    curr_power = 0
    power_sums = 0
    for line in fileinput.input(files = input_file):
        leaderboard = {color: 0 for color in leaderboard}
        curr_power = 0

        split_line = re.split(':|,|;', line)
        split_line.pop(0)
        for section in split_line:
            roll = section.split()
            val = int(roll[0])
            key = roll[1]
            if(leaderboard[key] < val):
                leaderboard[key] = val

        values = list(leaderboard.values())
        curr_power = values[0] * values[1] * values[2]
        power_sums += curr_power
    return power_sums


if __name__ == "__main__":
    print(cube_conundrum_part1('actual_input.txt'))
    print(cube_conundrum_part2('actual_input.txt'))