# ========================== random Module ==========================

import random

# print(dir(random))

# print(random.random())

# print(random.randint(1, 10))
# print(random.randint(1, 3))
# print(random.randint(10, 3)) # error

# print(random.randrange(10))
# print(random.randrange(5, 10))
# print(random.randrange(1, 10, 3))

# print(random.choice([1, 2, 3, 4]))

# print(random.sample( [1, 2, 3, 4, 5], 3 ))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# random.shuffle(l)

# print(l)

c = ["R", "B", "O", "A"]

c1 = random.choice(c)
c.remove(c1)

c2 = random.choice(c)
c.remove(c2)

f_m = f"{c1} vs {c2}"

c3 = random.choice(c)
c.remove(c3)

c4 = random.choice(c)
c.remove(c4)

s_m = f"{c3} vs {c4}"

print(f_m)
print(s_m)