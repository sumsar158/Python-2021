
def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    data_types = {"int": 0, "float": 0.1, "string": "0", "list": [], "tuple": (), "dict": {}, "set": set()}
    result = []
    for i in range(amount):
        result.append(data_types[data_type])
    return result


def generate_combined_list(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs',
    it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    """
    data_types = {"int": 0, "float": 0.1, "string": "a", "list": [], "tuple": (), "dict": {}, "set": set()}
    data = {}
    result = []

    for i in inputs:
        if i[1] not in data.keys():
            data[i[1]] = i[0]
        if i[1] in data.keys() and data[i[1]] < i[0]:
            data[i[1]] = i[0]

    for k, v in data.items():
        if k in data_types.keys():
            for i in range(v):
                result.append(data_types[k])

    return result


if __name__ == '__main__':
    print(generate_list(5, 'int'))


def generate_combined_list_unique(input_amount):
    return []