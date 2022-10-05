marks = list(map(int, input().split()))

print(f'{round(marks.count(5) / len(marks) * 100, 2)}%')
