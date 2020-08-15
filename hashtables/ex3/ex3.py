def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    intersections = []

    for arr in arrays:
        for num in arr:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
                
    max_value = max(hash_table.values())
    for key, value in hash_table.items():
        if value == max_value:
            intersections.append(key)
    return intersections
    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
