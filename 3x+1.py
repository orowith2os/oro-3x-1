list = random.randint(0,1000000000000)
while (list > 1):
  if (list % 2 == 0): list = list / 2
  else: list = 3 * list + 1
  print(list)
  print()
