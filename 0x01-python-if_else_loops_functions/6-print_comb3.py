#!/usr/bin/python3
for num in range(0, 90):
    if num % 10 > num / 10:
        if num != 89:
            print(f"{num:02d}, ", end='')
        else:
            print(f"{num:02d}")
