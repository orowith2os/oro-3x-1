import random
print("Type any positive integer, then press Enter:")
list = int (input(""))
while (list != 1):
 if (list % 2 == 0): list = list / 2
 else: list = 3 * list + 1
 print(list)
