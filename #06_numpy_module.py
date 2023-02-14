# ========================== numpy Module ==========================
import numpy as np

# print(np.__version__)

# print(dir(np))

# numpy => Numeric Python

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# b = np.array(a)

# print(a)
# print(b)
# print(type(a))
# print(type(b))

# ndarray => n-dimensional array

# a = [1, 2, 3, 8, False, "yehya", [1, 2, 3]]

# b = np.array(a)

# print(b)

# print(np.sin(90))
# print(np.sin(np.deg2rad(90)))
# print(np.cos(np.deg2rad(90)))
# print(np.tan(np.deg2rad(90)))
# print(np.sin(np.rad2deg(3.14)))

# print(np.round(9.6))
# print(np.round(9.66, 1))
# print(np.ceil(9.1))
# print(np.floor(9.9))
# print(np.mod(20, 7))
# print(np.power(10, 3))
# ============================================================================

# a = [1, 2, 3, 4, 5, 6, 7]
# b = np.array(a)

# print(a)
# print(b)
# print(type(a))
# print(type(b))

# print(len(a))
# print(len(b))
# print(b.shape)
# print(b.ndim)

# a = np.empty( (3, 2) )
# print(a)
# print(a.shape)
# print(a.ndim)

# print(dir(np.random))

# a = np.random.uniform(1, 10)
# a = np.random.uniform(1, 10, 5)
# a = np.random.uniform(1, 10,  (3, 2) )
# print(a)
# print(a.shape)
# print(a.ndim)


# a = np.random.random()
# a = np.random.random(2)
# a = np.random.random( (2, 3) )
# print(a)
# print(a.shape)
# print(a.ndim)

# a = np.random.normal(0, 1, 5)
# a = np.random.normal(0, 1,  (3, 2) )
# print(a)
# print(a.shape)
# print(a.ndim)

# a = np.random.rand( 5 )
# a = np.random.rand( 5, 3 )
# print(a)
# print(a.shape)
# print(a.ndim)

# a = np.random.randint(5, 10)
# a = np.random.randint(5, 20, (4, 2))
# print(a)
# print(a.shape)
# print(a.ndim)

# a = np.random.randint(0, 20, 10)
# b = a.reshape(5, 2)
# b = a.reshape(2, 5)
# print(a)
# print(a.shape)
# print(a.ndim)

# print(b)
# print(b.shape)
# print(b.ndim)

# a = np.zeros( (3, 2) )
# print(a)

# a = np.ones( (3, 2) )
# print(a)

# a = np.eye(5)
# print(a)

# a = np.full( (4, 3), 10 )
# print(a)

# a = [1, 2, 3, 4, 5]
# b = np.diag(a)
# print(b)

# a = np.linspace(1, 10)
# a = np.linspace(1, 10, 5)
# print(a)

# a = [1, 2, 3, 4, 5, 6]

# b = np.array(a)

# c = np.reshape(b, (3, 2))

# print(b)
# print(c)

# ==============================================================================

# a = np.random.randint(0, 10, (4, 3))
# b = np.count_nonzero(a)
# print(a)
# print("==============================================")
# print(b)

# a = np.random.randint(0, 10, (4, 3))
# b = np.count_nonzero(a>3)
# b = np.count_nonzero(a<8)
# b = np.count_nonzero(a==3)
# print(a)
# print("==============================================")
# print(b)


# a = np.random.randint(0, 10, (4, 3))
# b = np.count_nonzero(a>3, axis=0)
# c = np.count_nonzero(a>6, axis=1)
# print(a)
# print("==============================================")
# print(b)
# print("==============================================")
# print(c)


# a = np.random.randint(0, 10, (4, 3))
# b = np.any(a>3)
# c = np.any(a>3, axis=0)
# d = np.any(a>3, axis=1)
# print(a)
# print("==============================================")
# print(b)
# print("==============================================")
# print(c)
# print("==============================================")
# print(d)

# a = np.random.randint(0, 10, (4, 3))
# b = np.all(a>3)
# c = np.all(a>3, axis=0)
# d = np.all(a>3, axis=1)
# print(a)
# print("==============================================")
# print(b)
# print("==============================================")
# print(c)
# print("==============================================")
# print(d)

# a = np.random.randint(1, 10, (4, 3))
# b = np.random.randint(1, 10, (4, 3))
# # e = np.random.randint(1, 10, (3, 3))
# # d = a + e # error 

# c = a + b
# d = np.add(a, b)

# c = a - b
# d = np.subtract(a, b)

# c = a * b
# d = np.multiply(a, b)

# c = a / b
# d = np.divide(a, b)

# f = a ** 3
# print(a)
# print("==============================================")
# print(b)
# print("==============================================")
# print(c)
# print("==============================================")
# print(d)
# print("==============================================")
# print(f)


# a = np.random.randint(1, 10, (4, 3))
# b = np.random.randint(1, 10, (3, 4))

# c = np.dot(a, b)
# d = np.dot(b, a)

# print(c)
# print("==============================================")
# print(d)

# a = np.random.randint(1, 10, (4, 3))

# b = np.transpose(a)
# c = a.T
# print(a)
# print("==============================================")
# print(b)
# print("==============================================")
# print(c)

# a = np.random.randint(1, 10, (3, 3))

# b = np.linalg.inv(a)

# c = np.dot(a, b)

# print(a)
# print("==============================================")
# print(b)
# print("==============================================")
# print(c)

# a = np.random.randint(1, 10, 10)
# b = np.random.randint(1, 10, (4, 3))
# print(len(a))
# print(a.size)
# print(len(b))
# print(b.size)

