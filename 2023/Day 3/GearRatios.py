import fileinput
import re
def read_file(input_file):
    with open(input_file, 'r') as file:
        two_d_array = [list(line.strip()) for line in file]
    return two_d_array
    

def gear_ratios(input_file):
    input = read_file(input_file)
    i = 0
    total_sum = 0
    while i < len(input):
        j = 0
        while j < len(input[0]):

            #get whole number
            temp_str = ""
            temp_j = j
            while (temp_j < len(input[0]) and input[i][temp_j].isdigit()):
                temp_str += input[i][temp_j]
                temp_j+=1
            
            #determine what's on the edges
            if (temp_str != ""):
                is_valid = check_edges(input, i, j, temp_j)
                j = temp_j
                if (is_valid):
                    total_sum += int(temp_str)
            j+=1
        i+=1
    return total_sum

def check_edges(input, i, j, temp_j):
    while (j < len(input[0]) and j < temp_j):
        if (i-1 > 0 and j-1 > 0 and not input[i-1][j-1].isdigit() and not input[i-1][j-1] == "."):
            return True
        if (j-1 > 0 and not input[i][j-1].isdigit() and not input[i][j-1] == "."):
            return True
        if (i+1 < len(input) and j-1 > 0 and not input[i+1][j-1].isdigit() and not input[i+1][j-1] == "."):
            return True
        if (i-1 > 0 and not input[i-1][j].isdigit() and not input[i-1][j] == "."):
            return True
        if (i+1 < len(input) and not input[i+1][j].isdigit() and not input[i+1][j] == "."):
            return True
        if (i-1 > 0 and j+1 < len(input[0]) and not input[i-1][j+1].isdigit() and not input[i-1][j+1] == "."):
            return True
        if (j+1 < len(input[0]) and not input[i][j+1].isdigit() and not input[i][j+1] == "."):
            return True
        if (i+1 < len(input) and j+1 < len(input[0]) and not input[i+1][j+1].isdigit() and not input[i+1][j+1] == "."):
            return True
        j+=1
    return False

if __name__ == "__main__":
    print(gear_ratios('actual_input.txt'))