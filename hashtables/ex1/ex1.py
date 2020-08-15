def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}
    one = None
    two = None
    if length < 2:
        return None
    for i in range(length):
        weight_dict[weights[i]] = i

    for i in range(length):
        answer = limit - weights[i]
        if answer in weight_dict:
            one = weight_dict[answer]
            two = i
            result = [one, two]
            result.sort(reverse=True)
            return result[0], result[1]
            

