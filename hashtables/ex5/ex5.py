# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    file_names = {}
    paths = []
    for file in files:
        split_file = file.split("/")
        file_name = split_file[-1]
        if file_name not in file_names:
            file_names.setdefault(file_name, [file])
        else:
            file_names[file_name].append(file)
        
    for query in queries:
        if query in file_names:
            for file in file_names[query]:
                paths.append(file)    
    return paths

    


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
