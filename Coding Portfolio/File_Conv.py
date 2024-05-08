#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
from docx2pdf import convert  # Import the docx2pdf library

# Constants
WORKING_DIRECTORY = r'C:\Users\Ryan\WorkingScripts\Coding Portfolio\Finance Python Scripts\Finished'
DOC_TO_PDF = '1'
JSON_TO_CSV = '2'

def set_working_directory():
    """Set the working directory."""
    os.chdir(WORKING_DIRECTORY)
    print("Note: Ensure that the File to be converted is in the same folder as this script.")

def json_to_csv_conversion():
    """Convert JSON to CSV."""
    input_file = input("Enter the name of the input JSON file (including extension): ")
    output_file = input("Enter the name for the output CSV file (including extension): ")

    with open(input_file, 'r') as file:
        json_data = pd.read_json(file)

    json_data.to_csv(output_file, index=False)
    print(f"Conversion successful. JSON data from {input_file} has been saved to {output_file} as a CSV file.")

def doc_to_pdf_conversion():
    """Convert DOC to PDF."""
    doc_file_path = input("Enter the name of the DOC file to convert (including extension): ")
    pdf_file_path = os.path.splitext(doc_file_path)[0] + '.pdf'

    convert(doc_file_path, pdf_file_path)
    print(f"DOC to PDF conversion successful. {doc_file_path} has been converted to {pdf_file_path}.")

def main():
    try:
        set_working_directory()

        # Prompt user to choose the conversion option
        conversion_option = input("Choose the conversion option:\n"
                                  "1. Convert DOC to PDF\n"
                                  "2. Convert JSON to CSV\n"
                                  "Enter the option number: ")

        if conversion_option == JSON_TO_CSV:
            json_to_csv_conversion()
        elif conversion_option == DOC_TO_PDF:
            doc_to_pdf_conversion()
        else:
            # Handle invalid conversion option
            print("Error: Invalid conversion option. Please choose either '1' for DOC to PDF conversion or '2' for JSON to CSV conversion.")

    except FileNotFoundError as e:
        # Handle file not found error
        print(f"Error: {e}. Please make sure the files exist in the specified directory.")

    except pd.errors.EmptyDataError:
        # Handle empty JSON file error
        print(f"Error: The JSON file is empty. Please provide a valid JSON file with data.")

    except pd.errors.JSONDecodeError:
        # Handle JSON decode error
        print(f"Error: Unable to decode JSON data. Please check the file format and ensure it is valid JSON.")

    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}. Please review the script and file paths, and try again.")

if __name__ == "__main__":
    main()
