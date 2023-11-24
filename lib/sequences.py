#!/usr/bin/env python3

def print_fibonacci(length):
    fibonnaci_list = []
    if length > 0:
        fibonnaci_list.append(0)
        if length > 1:
            fibonnaci_list.append(1)
            if length > 2:
                for i in range(2, length):
                    fibonnaci_list.append(
                        fibonnaci_list[i - 1] + fibonnaci_list[i - 2])
    print(fibonnaci_list)

print_fibonacci(2)