def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    output = []
    # save (limit - weight) : weight, and check for weight,
    # because if you find (limit - weight) in weight,
    # it means weight is in list.
    for i in range(length):
        # check if weight is in cache and append its index
        # and the partner weight index to output array.
        # return array
        if (weights[i]) in cache:
            otherWeight = cache[weights[i]]
            output.append(i)
            output.append(weights.index(otherWeight))
            print(cache)
            return output
        else:
            # if weight is not in cache, add partner weight as key
            # and current weight index as value
            cache[limit - weights[i]] = weights[i]

    return None


print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
