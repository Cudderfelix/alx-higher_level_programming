#!/usr/bin/python3

""" Function that removes all C and C from String """

def no_c(my_string):
    string_length = len(my_string)

    i = 0
    new_string = my_string[:]

    for char in range(string_length):
        if (my_string[char] == 'c' or my_string[char] == 'c'):
            new_string = new_string[:(char -i)] + my_string[(char + 1):]
            i += 1
    return (new_string)
