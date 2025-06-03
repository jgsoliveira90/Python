import random as rd

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

people_chosed = rd.choice(friends)
number = rd.randint(0,4)
print(people_chosed)
print(friends[number])
