# this folder houses all functions that are required
# to run different modules of the project

# make necessary imports
import os
import pandas as pd


def convert_jsonl_to_xlsx():
    # Set the path to /data where the jsonl files are located
    jsonl_folder = 'Dataset/1.1/data'

    # Set the path to /output_xlsx where the xlsx files will be located
    output_folder = 'output_xlsx'

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through JSONL files and convert each to an Excel file
    for filename in os.listdir(jsonl_folder):
        if filename.endswith('.jsonl'):
            # Construct file paths
            jsonl_file_path = os.path.join(jsonl_folder, filename)
            xlsx_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.xlsx')

            # Read JSONL into a DataFrame
            data = pd.read_json(jsonl_file_path, lines=True)

            # Write the DataFrame to an Excel file
            data.to_excel(xlsx_file_path, index=False)
