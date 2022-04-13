# Итерируемый объект - объект, поддерживающий протокол итерации

# Итерируемый объект - объект, на основе которого можно создать итератор (у которого есть метод __iter__)
#
# Итерируемый объект, для которого запрашиваются итерации - __iter__
#
# Объект итератора, возвращаемый __iter__
# 1) Следующий эл-т __next__
# 2) Индикация конца последовательности


# for цель in итерируемый_объект:
#     код


l = [1, 2, 3, 4]

for i in l:
    print(i)

try:
    items = iter(l)
    while True:
        item = next(items)
        print(item)
except StopIteration:
    pass
