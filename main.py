from functions import convert_jsonl_to_xlsx

if __name__ == '__main__':
    # Set the path to /data where the jsonl files are located
    jsonl_folder = 'Your path to /data'

    # Set the path to /output_xlsx where the xlsx files will be located
    output_folder = 'specify location for /output_xlsx'

    # call the function for converting each jsonl files to xlsx files
    convert_jsonl_to_xlsx(jsonl_folder, output_folder)
