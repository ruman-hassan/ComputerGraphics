# this folder houses all functions that are required
# to run different modules of the project

# make necessary imports
import os
import pandas as pd


# This function takes in the folder location for the .jsonl files
# and the output folder location as arguments

def convert_jsonl_to_xlsx(jsonl_folder: str, output_folder: str):
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
