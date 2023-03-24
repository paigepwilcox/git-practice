def most_common_value(number_list):
    """ returns the most common element of the list
    """
    number_count = {}
    for number in number_list:
        if number not in number_count:
            number_count[number] = 1
        else:
            number_count[number] += 1
        


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
