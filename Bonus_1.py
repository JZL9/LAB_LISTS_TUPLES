numbers = [8, 7, -2, 0, 34, 10, 0]
numbers.sort(reverse=True)
first = [0,0]
numbers = first + [n for n in numbers if n not in first]
print(numbers)