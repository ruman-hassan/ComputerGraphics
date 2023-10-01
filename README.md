# Assessment Project - Python3 and File Processing

This project includes the implementation and documentation of tasks related to setting up a Python3 development environment, working with files, and processing a a massive dataset ( which was provided in the CAT instructions).

## Task 1: Python3 Development Environment (10 Marks)

1. **Setting up Python3 Development Environment:**
   - Installed [all necessary dependencies](#dependencies) for the Python3 development environment taht are indicated.


2. **Python Project Structure:**
   - Each member in the group created a Python project using the PyCharm structure. (The name of the project varied depending on the individuals way of creating the directory.)

3. **Importing the Dataset:**
   - Imported the MASSIVE Dataset mentioned in the data file. (The massive dataset can be found in the folderas well)

4. **Data Processing:**
   - Generated en-xx.xlsx files for all languages in the dataset, considering English as the pivot language.
   - This was done using the file named .py 
   - The group members managed to avoid using recursive algorithms to optimize time complexity while generating the required files..

5. **Flags and bash scripting:**
   - Utilized flags and bash scripting to facilitate running the solution on generator.sh files.

## Task 2: Working with Files (10 Marks)

1. **Generating JSONL Files:**
   - Generated separate JSONL files for English (en), Swahili (sw), and German (de) translations, containing test, train, and dev data.

2. **Creating Large JSON File:**
   - Created a large JSON file consolidating translations from en to xx with id and utt for all train sets.

3. **E-print Application:**
   - Utilized E-print application to pretty print the JSON file structure.

4. **File Backup and Upload:**
   - Uploaded all the generated files to the Google Drive Backup Folder.

5. **Version Control:**
   - Uploaded all the changes to GitHub using Google Cloud API.

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

Ensure you have the necessary permissions and API credentials for using Google APIs.

For TensorFlow, please follow the [official TensorFlow installation guide](https://www.tensorflow.org/install) to ensure you're installing the version compatible with your system and requirements.

Make sure to install these dependencies in your Python environment to successfully run the project.

## File Structure

Still coming up with that structure... Maybe we can just use how the cat_trial looks like...?

## Contributors

The contributors of this repository include the members of group two:
1. Manasseh Maina
2. Ruman Hassan
3. Lancelot Githinji
4. Charles Davies
5. Joyline Karanja

