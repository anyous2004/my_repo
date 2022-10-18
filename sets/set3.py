_newspaper = range(1, 76)
_magazine = range(77, 104)
_both = range(21, 34)


def task_3(newspaper, magazine, both):
    only_newspaper = (set(newspaper)).difference(set(both))
    only_magazines = (set(magazine)).difference(set(both))
    print(len(only_magazines) + len(only_newspaper) + len(both))


task_3(_newspaper, _magazine, _both)