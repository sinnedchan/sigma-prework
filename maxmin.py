def find_min_max(numbers):
    lowest = numbers[0]
    highest = numbers[0]
#assume that the first number in list is the lowest and highest, then proceed to loop through
#comparing each integer, and replacing lowest and highest when it occurs
    for number in numbers:
        if number < lowest:
            lowest = number
        if number > highest:
            highest = number
#when loop finishes, return both values in a list, lowest first
    return [lowest, highest]

print(find_min_max([2, 4, 1, 0, 2, -1]))
print(find_min_max([20, 50, 12, 6, 14, 8]))
print(find_min_max([100, -100]))