def task1(parameter1='ok', parameter2=1, parameter3=[1]):
    if parameter1 and parameter2 and parameter3:
        print(parameter1, parameter2, parameter3)


task1('lol', 12, ['kek', 0])
task1('', 0, [])