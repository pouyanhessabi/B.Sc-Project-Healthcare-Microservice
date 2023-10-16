import numpy as np
import openpyxl
import pandas as pd

filename = "output Alireza.xlsx"
sheet_name = "Sheet"
workbook = openpyxl.load_workbook(filename)


def export_to_excel(array):
    sheet = workbook.active

    # Write the elements of the array to column A (column index 1)
    for index, element in enumerate(array, start=1):
        sheet.cell(row=index, column=1).value = element

    # Save the workbook to the specified filename
    workbook.save(filename)
    # Example usage
    # my_array = ['(vertigo) Paroymsal  Positional Vertigo', 'AIDS', 'Acne', 'Alcoholic hepatitis', 'Allergy', 'Arthritis',
    #             'Bronchial Asthma', 'Cervical spondylosis', 'Chicken pox', 'Chronic cholestasis', 'Common Cold', 'Dengue',
    #             'Diabetes ', 'Dimorphic hemmorhoids(piles)', 'Drug Reaction', 'Fungal infection', 'GERD', 'Gastroenteritis',
    #             'Heart attack', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Hypertension ',
    #             'Hyperthyroidism', 'Hypoglycemia', 'Hypothyroidism', 'Impetigo', 'Jaundice', 'Malaria', 'Migraine',
    #             'Osteoarthristis', 'Paralysis (brain hemorrhage)', 'Peptic ulcer diseae', 'Pneumonia', 'Psoriasis',
    #             'Tuberculosis', 'Typhoid', 'Urinary tract infection', 'Varicose veins', 'hepatitis A']
    # export_to_excel(my_array)


def insert_zeros(range_str):
    sheet = workbook[sheet_name]

    for row in sheet[range_str]:
        for cell in row:
            if cell.value is None:
                cell.value = 0

    workbook.save(filename)
    # Example usage
    # insert_zeros("A1:Q42")


def normalize_row(row_index):
    sheet = workbook[sheet_name]
    row_values = sheet[row_index]
    values = [cell.value for cell in row_values if (cell.value is not None) and (type(cell.value) is not str)]
    total = sum(values)
    normalized_values = [value / total for value in values]

    for i, cell in enumerate(row_values):
        if (cell.value is not None) and (type(cell.value) is not str):
            cell.value = normalized_values.pop(0)


def average_result():
    file_paths = ['output Alireza.xlsx', 'output leila.xlsx', 'output Reyhan.xlsx']

    # Create an empty DataFrame to store the integrated data
    integrated_df = pd.DataFrame()

    # Loop through the file paths
    for file_path in file_paths:
        # Read each Excel file into a DataFrame, skipping the first row and first column
        df = pd.read_excel(file_path, skiprows=0, index_col=0)

        # Append the data to the integrated DataFrame
        integrated_df = integrated_df.add(df, fill_value=0)

    # Calculate the average by dividing the integrated DataFrame by the number of files
    average_df = integrated_df / len(file_paths)

    # Save the average DataFrame to a new Excel file
    average_df.to_excel('average_result.xlsx', engine='openpyxl')


def calculate_standard_deviation():
    # data1 = {
    #     'A': [1.0, 2.0, 3.0],
    #     'B': [4.0, 5.0, 6.0],
    #     'C': [7.0, 8.0, 9.0]
    # }
    # data2 = {
    #     'A': [2.0, 3.0, 4.0],
    #     'B': [5.0, 6.0, 7.0],
    #     'C': [8.0, 9.0, 10.0]
    # }
    # data3 = {
    #     'A': [6.0, 4.0, 5.0],
    #     'B': [6.0, 7.0, 8.0],
    #     'C': [9.0, 10.0, 11.0]
    # }
    # df1 = pd.DataFrame(data1)
    # df2 = pd.DataFrame(data2)
    # df3 = pd.DataFrame(data3)

    file_paths = ['output Alireza.xlsx', 'output leila.xlsx', 'output Reyhan.xlsx']
    df1 = pd.read_excel(file_paths[0], skiprows=0, index_col=0)
    df2 = pd.read_excel(file_paths[1], skiprows=0, index_col=0)
    df3 = pd.read_excel(file_paths[2], skiprows=0, index_col=0)

    # Calculate the mean of the three DataFrames
    mean_df = (df1 + df2 + df3) / 3

    # Calculate the squared differences for each DataFrame
    squared_diff1 = (df1 - mean_df) ** 2
    squared_diff2 = (df2 - mean_df) ** 2
    squared_diff3 = (df3 - mean_df) ** 2

    # Sum the squared differences
    sum_squared_diff = squared_diff1 + squared_diff2 + squared_diff3

    # Calculate the standard deviation
    std_dev_df = np.sqrt(sum_squared_diff / 3)
    std_dev_df.to_excel('std_dev.xlsx', engine='openpyxl')
    # Output DataFrame (std_dev_df) will have the same dimensions as df1, df2, and df3
    print(std_dev_df)


if __name__ == "__main__":
    """ 
    normalized each file
    insert_zeros("A1:Q42")
    for index_row in range(2, 43):
        normalize_row(index_row)
    workbook.save(filename)"
    """

    """
    average_result()
    """

    """
    calculate_standard_deviation()
    """
