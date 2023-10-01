import os
import pandas as pd

# Path to the directory containing the .jsonl files
data_directory = "amazon_dataset_processor/data/1.1/data"


def process_data(file_path):
    # Read the .json file and extract English text and translation
    # Replace this with the actual logic to extract the required information from your dataset
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        english_text = data.get("english_text", "English text not available")
        translation = data.get("translation", "Translation not available")

    # Create a DataFrame
    df = pd.DataFrame({"English": [english_text], "Translation": [translation]})

    # Extract the language code from the file path
    language_code = os.path.basename(file_path).split('.')[0]

    # Save to Excel
    excel_path = f"output/{language_code}.xlsx"  # Modify the path as needed
    df.to_excel(excel_path, index=False)


# Iterate over each .jsonl file in the directory
for file_name in os.listdir(data_directory):
    if file_name.endswith(".jsonl"):
        file_path = os.path.join(data_directory, file_name)
        process_data(file_path)
