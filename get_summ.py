#!/usr/bin/python3.6

def get_summ(one, two, delimiter='&'):
    return str(one).upper() + str(delimiter).upper() + str(two).upper()

sum_string = get_summ("Learn", "python")
print(sum_string)
