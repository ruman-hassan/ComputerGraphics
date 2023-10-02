import tarfile

tar_file = 'amazon-massive-dataset-1.1_CAT1.tar'

with tarfile.open(tar_file, 'r') as tar:
    tar.extractall()

import pandas as pd

df = pd.read_xlsx('extracted_file.xlsx')



