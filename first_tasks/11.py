print("Введите массу в киллограмах:")
m = int(input())
print("Введите рост в сантиметрах:")
santi = int(input())
h2 = float((santi / 100) ** 2)
i = m / h2
print(round(i, 2))

