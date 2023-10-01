import json
import os

def split_data_and_write(language, data):
    # Split the data into train, test, and dev sets
    train_data = data[:8000]
    test_data = data[8000:9000]
    dev_data = data[9000:]

    # Write the data to separate JSONL files
    with open(f'data/{language}_train.jsonl', 'w') as f:
        for item in train_data:
            f.write(json.dumps(item) + '\n')

    with open(f'data/{language}_test.jsonl', 'w') as f:
        for item in test_data:
            f.write(json.dumps(item) + '\n')

    with open(f'data/{language}_dev.jsonl', 'w') as f:
        for item in dev_data:
            f.write(json.dumps(item) + '\n')

# Sample data for each language
en_data = [{'text': 'English sentence 1'}, {'text': 'English sentence 2'}, ]  # Replace ellipsis with actual data
sw_data = [{'text': 'Swahili sentence 1'}, {'text': 'Swahili sentence 2'}, ...]  # Replace ellipsis with actual data
de_data = [{'text': 'German sentence 1'}, {'text': 'German sentence 2'}, ...]  # Replace ellipsis with actual data

# Call the function for each language
split_data_and_write('en-US', en_data)
split_data_and_write('sw-KE', sw_data)
split_data_and_write('de-DE', de_data)
