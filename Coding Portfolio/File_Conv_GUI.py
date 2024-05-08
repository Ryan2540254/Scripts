#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas          as pd
from   docx2pdf    import convert  # Import the docx2pdf library
import tkinter         as tk
from   tkinter     import filedialog

# Constants
WORKING_DIRECTORY = r'C:\Users'
DOC_TO_PDF        = '1'
JSON_TO_CSV       = '2'

class ConversionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Conversion App")
        self.root.geometry("400x200")

        self.set_working_directory()

        tk.Label(root, text="Choose the conversion option:").pack(pady=10)

        tk.Button(root, text="Convert DOC to PDF", command=self.doc_to_pdf_conversion).pack(pady=5)
        tk.Button(root, text="Convert JSON to CSV", command=self.json_to_csv_conversion).pack(pady=5)

    def set_working_directory(self):
        os.chdir(WORKING_DIRECTORY)
        print("Note: Ensure that the File to be converted is in the same folder as this script.")

    def json_to_csv_conversion(self):
        input_file = filedialog.askopenfilename(title="Select JSON file", filetypes=[("JSON files", "*.json")])
        output_file = filedialog.asksaveasfilename(title="Save CSV file", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        try:
            json_data = pd.read_json(input_file)
            json_data.to_csv(output_file, index=False)
            tk.messagebox.showinfo("Conversion Successful", f"JSON data from {input_file} has been saved to {output_file} as a CSV file.")
        except pd.errors.EmptyDataError:
            tk.messagebox.showerror("Error", f"The JSON file {input_file} is empty. Please provide a valid JSON file with data.")
        except pd.errors.JSONDecodeError:
            tk.messagebox.showerror("Error", f"Unable to decode JSON data from {input_file}. Please check the file format and ensure it is valid JSON.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An unexpected error occurred: {e}. Please review the script and file paths, and try again.")

    def doc_to_pdf_conversion(self):
        doc_file_path = filedialog.askopenfilename(title="Select DOC file", filetypes=[("DOC files", "*.docx")])
        pdf_file_path = filedialog.asksaveasfilename(title="Save PDF file", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        try:
            convert(doc_file_path, pdf_file_path)
            tk.messagebox.showinfo("Conversion Successful", f"DOC to PDF conversion successful. {doc_file_path} has been converted to {pdf_file_path}.")
        except FileNotFoundError as e:
            tk.messagebox.showerror("Error", f"{e}. Please make sure the files exist in the specified directory.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An unexpected error occurred: {e}. Please review the script and file paths, and try again.")

def main():
    root = tk.Tk()
    app = ConversionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
