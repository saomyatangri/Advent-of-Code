import fileinput
import numpy as np

def scratchcards(input_file):
    total_score = 0
    for line in fileinput.input(files = input_file):
        pair = line.split("|")
        winning_numbers = np.array(pair[0].split())
        our_numbers = np.array(pair[1].split())
        
        #Drop "Card x:" from list
        winning_numbers = winning_numbers[2:]
        our_winning_nums = np.intersect1d(winning_numbers, our_numbers)

        if our_winning_nums.size != 0:
            score = 2**(len(our_winning_nums)-1)
            total_score += score
    return total_score


if __name__ == "__main__":
    print(scratchcards('actual_input.txt'))
