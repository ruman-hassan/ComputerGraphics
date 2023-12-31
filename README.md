# Assessment Project - Python3 and File Processing

This project includes the implementation and documentation of tasks related to setting up a Python3 development environment, working with files using python, and processing a massive dataset ( which was provided in the CAT instructions).

## File Structure

This repository contains a directory called dataset, which contains the massive dataset that was provided to use as the data source for this CAT. The other files contain the codes that are to be used to execute the activities that have been listed.

## Task 1: Python3 Development Environment (10 Marks)

1. **Setting up Python3 Development Environment:**
   - Installed all necessary [dependencies](#dependencies) for the Python3 development environment taht are indicated.

2. **Python Project Structure:**
   - Each member in the group created a Python project using the PyCharm structure(The name of the project varied depending on the individuals way of creating the directory).
   - The files contained within this repository include:
   
      1. deutsch.py : For generating ,German (de), separate jsonl files with test, train and dev respectively
      2. english.py : For generating ,English (en), separate jsonl files with test, train and dev respectively
      3. swahili.py : For generating ,Swahili (sw), separate jsonl files with test, train and dev respectively
      4. JSON_to_XLSX.py : For converting the .jsonl file structure to .xlsx in the folder output
      5. large_json : For generating one large json file showing all the translations from en to xx with id and utt for all the train sets. 
      6. functions.py : which works hand in hand with main.py to perform conversion of .jsonl to .xlsx
      7. main.py

3. **Importing the Dataset:**
   - Imported the MASSIVE Dataset mentioned in the data file. (The massive dataset can be found in the folder: Dataset/1.1/data).

4. **Data Processing:**
   - Generated en-xx.xlsx files for all languages in the dataset, considering English as the pivot language(The output folder will be made manually or can be created using the code).
   - The group members managed to avoid using recursive algorithms to optimize time complexity while generating the required files..

## Task 2: Working with Files (10 Marks)

1. **Generating JSONL Files:**
   - Generated separate JSONL files for English (en), Swahili (sw), and German (de) translations, containing test, train, and dev data.

2. **Creating Large JSON File:**
   - Created a large JSON file consolidating translations from en to xx with id and utt for all train sets.

3. **E-print Application:**
   - Utilized E-print application to pretty print the JSON file structure.

4. **File Backup and Upload:**
   - Uploaded all the generated files to GithHb for referencing as well as editing.

5. **Version Control:**
   - Uploaded all the changes to GitHub.

## How to Use

The following states the dependencies required to run the project as well as the cloning process and the file structure.

## Dependencies

Ensure you have the following dependencies installed to run the project:

1. **Pandas**:
   - Pandas is an open-source data manipulation and analysis tool. To install, use pip:
     ```bash
     pip install pandas
     ```

2. **Openpyxl**:
   - Openpyxl is a Python library to read/write Excel xlsx files. Install it using pip:
     ```bash
     pip install openpyxl
     ```

3. **NumPy**:
   - NumPy is a powerful numerical computing library. Use pip to install:
     ```bash
     pip install numpy
     ```

4. **TensorFlow**:
   - TensorFlow is an open-source machine learning framework. Refer to the [official TensorFlow installation guide](https://www.tensorflow.org/install) for detailed installation instructions.

5. **Google API Client**:
   - The Google API Client library allows interaction with various Google services. To install, use pip:
     ```bash
     pip install google-api-python-client
     ```

## Cloning the Repository using SSH

To clone this repository using SSH, follow these steps:

1. **Copy the SSH URL**:
   - Go to the GitHub repository and copy the SSH URL. You can find the SSH URL by clicking on the "Code" button and selecting the SSH option.

2. **Open Terminal**:
   - Open your terminal or command prompt on your local machine.

3. **Clone the Repository**:
   - Navigate to the directory where you want to clone the repository using the `cd` command:
     ```bash
     cd /path/to/your/directory
     ```
   - Clone the repository using the `git clone` command and paste the copied SSH URL:
     ```bash
     git clone git@github.com:pomegranating/ComputerGraphics.git
     ```

4. **Verify the Cloning**:
   - After executing the clone command, you should see a message indicating that the repository is being cloned.

5. **Access the Cloned Repository**:
   - Use `cd` to navigate into the cloned repository's directory:
     ```bash
     cd ComputerGraphics
     ```


Now you have successfully cloned the repository using SSH. Remember to have SSH keys set up on your machine and added to your GitHub account for this method to work. Once installed you can run the codes on your end.

## Contributors

The contributors of this repository include the members of group two:
1. Manasseh Maina 
2. Ruman Hassan
3. Lancelot Githinji
4. Charles Davies
5. Joyline Karanja
