#!/usr/bin/env python3
# Created by : Samuel Nkongolo
# Date: Dec. 15, 2022
# This program prints the highest value of ten randomly
# generated numbers.


import random
import constants




def find_max_value(list_of_int):
    greatest_num = -1
    # Getting the size of the array outside the loop to save on memory.
    list_size = len(list_of_int)
    # Checking if the greatest number so far is bigger than the next one on the list.
    for counter in range(0, list_size):
        if list_of_int[counter] > greatest_num:
            greatest_num = list_of_int[counter]
    return greatest_num




def main():
    # Creating the list.
    list_of_rand = []
    for counter in range(0, constants.MAX_ARRAY_SIZE):
        rand_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        # Adding the random number to the list.
        list_of_rand.append(rand_num)
        # Displaying the contents of the list.
        print(f"{rand_num} added at position {counter}")
        # Calling and passing the array to the function that returns the greatest number.
        final_int = find_max_value(list_of_rand)


    # Output.
    print(f"\nThe greatest number is {final_int}")




if __name__ == "__main__":
    main()
