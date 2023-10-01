import os
import jsonlines
import pandas as pd

# Define the path to the dataset folder
dataset_folder = 'Dataset/1.1/data'

# Process only en-US.jsonl
jsonl_file = 'sw-KE.jsonl'

# Initialize empty dictionaries for each partition
train_data = []
dev_data = []
test_data = []

# Read the JSONL file
with jsonlines.open(os.path.join(dataset_folder, jsonl_file)) as reader:
    for line in reader:
        # Depending on the 'partition' field, add the data to the respective dictionary
        partition = line['partition']
        if partition == 'train':
            train_data.append(line)
        elif partition == 'dev':
            dev_data.append(line)
        elif partition == 'test':
            test_data.append(line)

# Create separate JSONL files for each partition
train_file = os.path.join(dataset_folder, 'sw-KE-train.jsonl')
dev_file = os.path.join(dataset_folder, 'sw-KE-dev.jsonl')
test_file = os.path.join(dataset_folder, 'sw-KE-test.jsonl')

with jsonlines.open(train_file, 'w') as writer:
    writer.write_all(train_data)

with jsonlines.open(dev_file, 'w') as writer:
    writer.write_all(dev_data)

with jsonlines.open(test_file, 'w') as writer:
    writer.write_all(test_data)
