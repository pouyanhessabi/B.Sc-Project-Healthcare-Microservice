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
