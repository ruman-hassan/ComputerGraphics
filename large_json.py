import os
import jsonlines
import json

# Define the path to the dataset folder
dataset_folder = 'Dataset/1.1/data/'

# Initialize an empty dictionary to store translations
translations = {}

# List all JSONL files in the dataset folder as shown
jsonl_files = [f for f in os.listdir(dataset_folder) if f.endswith('.jsonl')]

# Iterate through each JSONL file
for jsonl_file in jsonl_files:
    # Read the JSONL file
    with jsonlines.open(os.path.join(dataset_folder, jsonl_file)) as reader:
        for line in reader:
            # Check if it's a 'train' partition
            if line['partition'] == 'train':
                # Extract relevant information
                lang_code = jsonl_file.split('.')[0]  # Language code
                translation = {
                    'id': line['id'],
                    'utt': line['utt']
                }

                # Add the translation to the dictionary
                if lang_code not in translations:
                    translations[lang_code] = []
                translations[lang_code].append(translation)

# Save the translations as a JSON file
with open('C:/Users/davie/Downloads/amazonCAT1/1.1/output/all_translations.json', 'w', encoding='utf-8') as json_file:
    json.dump(translations, json_file, indent=4, ensure_ascii=False)

print("JSON file 'all_translations.json' has been created.")
