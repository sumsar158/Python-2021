"""Hobbies."""


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    sorted_dict = {}

    for k, v in dic.items():
        v = sorted(v)
        sorted_dict[k] = v

    return sorted_dict


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    dict_hobbies = {}
    data = data.replace("\n", " ").split(" ")

    for i in data:
        i = i.split(":")
        if i[0] not in dict_hobbies:
            dict_hobbies[i[0]] = []
        if i[1] not in dict_hobbies[i[0]]:
            dict_hobbies[i[0]].append(i[1])

    return dict_hobbies


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    dict_hobbies = {}
    data = data.replace("\n", " ").split(" ")

    for i in data:
        i = i.split(":")
        if i[1] not in dict_hobbies:
            dict_hobbies[i[1]] = []
        if i[0] not in dict_hobbies[i[1]]:
            dict_hobbies[i[1]].append(i[0])

    dict_hobbies = sort_dictionary(dict_hobbies)

    return dict_hobbies


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    data = create_dictionary(data)
    pupils_hobbies_count = {}
    list_of_people_with_most_hobbies = []
    max_value = 0

    for k, v in data.items():
        v = len(v)
        pupils_hobbies_count[k] = v
        if v > max_value:
            max_value = v

    for k, v in pupils_hobbies_count.items():
        if v == max_value:
            list_of_people_with_most_hobbies.append(k)

    return sorted(list_of_people_with_most_hobbies)


def find_people_with_least_hobbies(data: str) -> list:
    """
    Find the people who have least hobbies.

    :param data: given string from database
    :return: list of people with least hobbies. Sorted alphabetically.
    """
    data = create_dictionary(data)
    pupils_hobbies_count = {}
    list_of_people_with_most_hobbies = []
    max_value = 999

    for k, v in data.items():
        v = len(v)
        pupils_hobbies_count[k] = v
        if v < max_value:
            max_value = v

    for k, v in pupils_hobbies_count.items():
        if v == max_value:
            list_of_people_with_most_hobbies.append(k)

    return sorted(list_of_people_with_most_hobbies)


def find_most_popular_hobbies(data: str) -> list:
    """
    Find the most popular hobbies.

    :param data: given string from database
    :return: list of most popular hobbies. Sorted alphabetically.
    """
    data = create_dictionary_with_hobbies(data)
    hobbies_popularity = {}
    most_popular_hobbies = []
    max_value = 0

    for k, v in data.items():
        v = len(v)
        hobbies_popularity[k] = v
        if v > max_value:
            max_value = v

    for k, v in hobbies_popularity.items():
        if v == max_value:
            most_popular_hobbies.append(k)

    return sorted(most_popular_hobbies)


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    data = create_dictionary_with_hobbies(data)
    hobbies_popularity = {}
    most_popular_hobbies = []
    max_value = 99999

    for k, v in data.items():
        v = len(v)
        hobbies_popularity[k] = v
        if v < max_value:
            max_value = v

    for k, v in hobbies_popularity.items():
        if v == max_value:
            most_popular_hobbies.append(k)

    return sorted(most_popular_hobbies)


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    pass


if __name__ == '__main__':
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    dic = create_dictionary(sample_data)
    print(sort_dictionary(dic))
    print(create_dictionary_with_hobbies(sample_data))
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print(find_people_with_most_hobbies(sample_data))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print(find_people_with_least_hobbies(sample_data))  # -> ['Molly']
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print(find_most_popular_hobbies(sample_data))  # -> ['football', 'gaming', 'sport']
    print(find_least_popular_hobbies(sample_data))  # -> ['dance', 'flowers', 'puzzles', 'tennis']

    sort_result = sort_names_and_hobbies(sample_data)
    # if the condition after assert is False, error will be thrown
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == 'Alfred'
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == ('Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # if you see this line below, then everything seems to be ok!
    print("sorting works!")

    # print(sort_names_and_hobbies(sample_data))