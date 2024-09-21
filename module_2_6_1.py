# Переменная a может быть только от 3 и не более b. Переменная b только более a.
a = 3
b = 20

for i in range(a, b + 1):
    result = []
    for j in range(1, b // 2):
        for k in range(2, b):
            if i % (j + k) == 0 and j < k:
                result.extend([j, k])
    print(i, ' - ', *result, sep='')
