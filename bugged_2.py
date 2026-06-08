def find_largest(numbers):
    largest = 0

    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]

    return largest


# Program starts here
temperatures = [-3, -7, -1, -12, -5]

print("Temperatures:", temperatures)

highest = find_largest(temperatures)

print("Highest temperature:", highest)