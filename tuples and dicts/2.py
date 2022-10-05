numbers = "0139412831055230677798"

result = {}
for i in range(0, 10):
    result[i] = numbers.count(str(i))

print(result)


