def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    output = []
    for i in range(length):
        if (weights[i]) in cache:
            otherWeight = cache[weights[i]]
            output.append(i)
            output.append(weights.index(otherWeight))
            return output
        else:
            cache[limit - weights[i]] = weights[i]

    return None


print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
