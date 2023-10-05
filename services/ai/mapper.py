import os

import pandas as pd

from shared_method import get_the_five_highest_value_dictionary, normalized_dictionary_values


def read_create_dataframe():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data\\average_result.xlsx')
    dataframe = pd.read_excel(file_path, index_col=0)
    return dataframe


def calculate_expertise_disease_value(df, given_diseases):
    expertise_disease_value = dict.fromkeys(df.columns.values, 0)
    for expertise in expertise_disease_value:
        for disease in given_diseases:
            expertise_disease_value[expertise] += given_diseases[disease] * (df.loc[disease]).get(expertise)
    expertise_disease_value = dict(sorted(expertise_disease_value.items(), key=lambda item: item[1], reverse=True))
    normalized = normalized_dictionary_values(expertise_disease_value)
    return get_the_five_highest_value_dictionary(normalized)


def mapper_method(given_diseases: dict):
    df = read_create_dataframe()
    expertises = calculate_expertise_disease_value(df, given_diseases)
    print("Expertises: ", expertises)
    return expertises

# Example Usage:
# given_diseases = {'Paralysis (brain hemorrhage)': 0.79882693, 'Hyperthyroidism': 0.047980916, 'GERD': 0.019209143,
#                   'Cervical spondylosis': 0.015426416, 'Migraine': 0.012158146}
# mapper_method(given_diseases)
