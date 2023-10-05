def get_the_five_highest_value_dictionary(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:5])


def normalized_dictionary_values(dictionary: dict):
    """ THis method divide all values by sum, that means sum(dict.values) = 1.
    after that it multiply 100 so that it shows percentage"""
    total_sum = sum(dictionary.values())
    return {key: round(value * 100 / total_sum, 2) for key, value in dictionary.items()}


def create_dictionary_from_formatted_ui_list(formatted_list):
    reverted_dict = {}
    for item in formatted_list:
        key, value_str = item.split(':')
        key = key.strip()  # Remove leading/trailing spaces
        value = float(value_str.strip())  # Convert the value to an integer (or float if needed)
        reverted_dict[key] = value
    return reverted_dict


def create_formatted_list_from_dictionary_to_ui(dictionary):
    return [f'{key}: {value}' for key, value in dictionary.items()]


def separate_value_before_colon(string):
    colon_index = string.find(":")
    if colon_index != -1:
        result = string[:colon_index].strip()
    else:
        result = string  # Handle the case where no colon is found
    return result
