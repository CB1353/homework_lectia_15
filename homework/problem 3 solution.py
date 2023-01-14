import random
while True:
  print('''1.Roll the dice    2.Exit''')
  user = int(input("Choose a number:"))
  if user == 1:
    number_1 = random.randint(1,6)
    print(number_1)
    number_2 = random.randint(1,6)
    print(number_2)
    sum = number_1 + number_2
    print(sum)
  else:
    break