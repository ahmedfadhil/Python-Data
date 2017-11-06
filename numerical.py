import numpy as np

# Creating array with numpy

my_list = [1, 2, 3, 4, 5]
x = np.array(my_list)

y = np.array([1, 2, 3, 4, 5])
m = np.array([[1, 2, 3], [1, 2, 3]])
print(m.shape)

# Arrange function
n = np.arange(0, 30, 2)

n = n.reshape(3, 5)
print(n)

line = np.linspace(0, 4, 9)
print(line.resize(3, 3))

pones = np.ones((3, 2))
zones = np.zeros((3, 2))

print(pones)
print()
print(zones)

eyes = np.eye(8)
diag = np.diag([[1, 2, 3, 4], [3, 4, 5, 6]])
print(diag)

repeating = np.repeat([1, 2, 3], 3)
print(repeating)

p = np.ones([2, 3], float)

vp = np.vstack([p, 2 * p])
hp = np.hstack([p, 2 * p])

# print(p)
# print(vp)
# print(hp)
z = np.array([y, y ** 2])
#
# z.shape
# # z.T
# print(z.shape)
# print(z.T)
# print(z.dtype)

# Operations
amount = np.array([-2, 3, 4, 5, 6, 76, 7, 9])

print('---------------')
print(amount.sum())
print(amount.max())
print(amount.min())
print(amount.mean())
print(amount.std())
print(amount.argmax())
print(amount.argmin())
print('================')

# Indexing and slicing

s = np.arange(13) ** 2

print(s)
print(s[-5::-2])

r = np.arange(30)
r.resize((6, 6))

print(r[2, 3])
print(r[3, 3:6])
print(r[r > 4])

xy = r[r > 30] = 20
print(xy)

r2 = r[:3, :3]
print('===================')
print(r2)

r2[:] = 0

print(r)

r_copy = r.copy()

r_copy[:] = 10
print(r)

# Iterating through arrays

test = np.random.randint(0, 10, (4, 3))
print(test)

for row in test:
    print('{}'.format(row))
    print('-')
print('--------------')
for i in range(len(test)):
    print(test[i])

for i, row in enumerate(test):
    print('row', i, 'is', row)

test2 = test ** 2
print(test2)

for i, j in zip(test, test2):
    print(i, '+', j, '=', i + j)
