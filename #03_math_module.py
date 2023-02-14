# ========================== math Module ==========================

import math

# print(dir(math))

# print(math.factorial(5)) # 5 * 4 * 3 * 2 * 1

# print(math.pi)
# print(math.e)
# print(math.inf)

print(math.exp(2))

print(math.log(10))  # e ** 2.30 = 10
print(math.log(10, math.e))  # e ** 2.30 = 10
print(math.log(100, 10))  # 10 ** 2 = 100

print(math.log10(100)) # 10 ** 2 = 100

print(math.sqrt(100)) # 10 * 10 = 100

print(math.degrees(3.14))
print(math.degrees(math.pi))

print(math.radians(180))
print(math.radians(360))

print(math.sin(math.radians(90)))
print(math.cos(math.radians(90)))
print(math.tan(math.radians(90)))

print(math.copysign(10, 20))
print(math.copysign(10, -20))
print(math.copysign(-10, -20))
print(math.copysign(-10, 20))

print(math.ceil(9.1))
print(math.ceil(12.9))

print(math.floor(19.9))
print(math.floor(19.1))