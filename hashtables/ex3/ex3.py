def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    count = {}
    dups = []
    for array in arrays:
        for item in array:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1

    for item in count:
        if count[item] == len(arrays):
            dups.append(item)

    return dups


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
