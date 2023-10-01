import os
import jsonlines
import pandas as pd

# Define the path to the dataset folder
dataset_folder = 'C:/Users/davie/Downloads/amazonCAT1/1.1/data'

# List all JSONL files in the dataset folder
jsonl_files = [f for f in os.listdir(dataset_folder) if f.endswith('.jsonl')]

for jsonl_file in jsonl_files:
    # Extract the language code from the filename (e.g., "af-ZA.jsonl" -> "af-ZA")
    lang_code = jsonl_file.split('.')[0]

    # Initialize an empty list to store data
    data = []

    # Read the JSONL file
    with jsonlines.open(os.path.join(dataset_folder, jsonl_file)) as reader:
        for line in reader:
            data.append({'id': line['id'], 'utt': line['utt'], 'annot_utt': line['annot_utt']})

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Create an Excel writer object
    excel_file = f'C:/Users/davie/Downloads/amazonCAT1/1.1/data/new/en-{lang_code}.xlsx'
    writer = pd.ExcelWriter(excel_file, engine='openpyxl')

    # Write the DataFrame to the Excel file
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Save the Excel file
    writer._save()


