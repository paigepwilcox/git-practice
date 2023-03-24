def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max
    
=======
    largest_number = max(numbers)
    return largest_number
>>>>>>> 4865d1390e66b59e48ff1c748de42662c24ce436


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
