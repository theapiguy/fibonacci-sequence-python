#!/usr/bin/env python3


#  C:\Users\keithr\PycharmProjects\testCode\src\fib.py
#  The Fibonacci Sequence is the series of numbers:
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#  The next number is found by adding up the two numbers before it:


print("The Fibonacci Sequence is the series of numbers, "
      "the next number is found by adding up the two numbers before it:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...")

upper_limit = 40
valid_int = False
while not valid_int:
    max_num = input(f"How many numbers of the Fibonacci Sequence would you like to generate (max of {upper_limit})?  ")
    if max_num.upper() == 'END' or max_num == '':
        print("Ending script.")
        exit(0)

    max_num = int(max_num)
    if max_num <= 2:
        print("Value must be greater than 2.")
    else:
        try:
            valid_int = True
        except ValueError:
            print("Please enter a valid integer.")

if max_num > upper_limit:
    print(f"You have exceeded the max of {upper_limit} numbers.")
    exit(0)

fib_list = []
for x in range(max_num):
    if not fib_list:
        #  Nothing exists, add 0
        fib_list.append(x)
    elif len(fib_list) == 1:
        #  0 exists, add 1
        fib_list.append(x)
    else:
        #  We have the first 2 numbers, now the main logic
        next_num = fib_list[x-2] + fib_list[x-1]
        fib_list.append(next_num)

fib_str = map(str, fib_list)
print()
print(f"Fibonacci Sequence", f"{','.join(fib_str)}", sep='\n')

