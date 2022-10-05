print("введите трёхзначное число:")
num = int(input())
a = num // 100
b = num % 100
c = num % 10
print(a + (b // 10) + c)



