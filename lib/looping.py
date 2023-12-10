#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print ("Happy New Year!")

def square_integers(int_list):
    squared_list = [num ** 2 for num in int_list]
    return squared_list


def fizzbuzz():
    for num in range(1, 101):
        # Check if num is a multiple of both 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        # Check if num is a multiple of 3
        elif num % 3 == 0:
            print("Fizz")
        # Check if num is a multiple of 5
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()