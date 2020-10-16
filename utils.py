def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


numbers = [12, 8, 9, 7]
print(find_max(numbers))