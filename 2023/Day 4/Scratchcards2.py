import fileinput
import numpy as np

def scratchcards(input_file):
    frequencies = np.ones(206)
    frequencies[0] = 0
    card_num = 0
    
    #I felt like using one-based indexing for the scratchcards. Felt easier to wrap my head around it since that's how they're written in the problem.
    for line in fileinput.input(files = input_file):
        card_num += 1
        pair = line.split("|")
        winning_numbers = np.array(pair[0].split())
        our_numbers = np.array(pair[1].split())
        
        winning_numbers = winning_numbers[2:]
        our_winning_nums = np.intersect1d(winning_numbers, our_numbers)
        matching_nums = our_winning_nums.size

        if matching_nums != 0:
            frequencies[card_num+1:card_num+matching_nums+1] += 1*frequencies[card_num]
    
    return int(frequencies.sum())


if __name__ == "__main__":
    print(scratchcards('actual_input.txt'))
