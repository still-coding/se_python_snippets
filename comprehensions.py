# Включения

# l = []
# for i in range(10):
#     l.append(i)
#
#
# l = list(range(10))

def sqr(x):
    return x * x

# списковые
l = [sqr(i) for i in range(10) if i % 2]
print(l)


# l = []
# for i in range(10):
#     for j in range(100, 100, 100):
#         if i % 2:
#             l.append(i + j)

l = [i + j for i in range(10) if i % 2
    for j in range(100, 1000, 100)]

print(l)


# О.ф
#
# [выражение for цель1 in итерируемый_объект1 if условие1
#             for цель2 in итерируемый_объект2 if условие2
#             ...]

# включения множеств
s = {sqr(i) for i in range(10) if i % 2}
print(s)


# словарные
d = {i: sqr(i) for i in range(10) if i % 2}
print(d)


# no tuple comprehension!
t = (sqr(i) for i in range(10) if i % 2)
print(t)
