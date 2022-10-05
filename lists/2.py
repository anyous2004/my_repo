marks = ['5', '5', '2', '3', '3', '2', '5', '4', '2', '4']


print(sorted(marks, reverse=True))
print(len(marks))
print((marks.count('5') + marks.count('4') + marks.count('3')) / len(marks) * 100)
