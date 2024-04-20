#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def is_curl_installed():
    try:
        subprocess.run(['curl', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def run_curl_command(url, save_output=False, file_format="txt"):
    try:
        # Validate URL format before running the command
        if not url.startswith("http://") and not url.startswith("https://"):
            raise ValueError("Invalid URL format. Please include 'http://' or 'https://'.")

        # Construct the curl command
        curl_command = ['curl', url]

        # Run the curl command
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)

        # Print or save the result based on user preference
        if save_output:
            save_to_file(result.stdout, file_format)
        else:
            print_result(result.stdout)

    except ValueError as ve:
        # Handle invalid URL format
        logging.error(f"Error: {ve}")

    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        logging.error(f"Error executing curl command: {e}")
        logging.error("Error Output:")
        logging.error(e.stderr)

def print_result(output):
    print("Curl Command Output:")
    print(output)

def save_to_file(output, file_format):
    filename = input("Enter the filename (including extension): ").strip()
    
    try:
        with open(filename, 'w') as file:
            file.write(output)
        logging.info(f"Output saved to {filename}")
    except Exception as ex:
        logging.error(f"Error saving to file: {ex}")

if __name__ == "__main__":
    try:
        # Check if curl is installed
        if not is_curl_installed():
            logging.error("Error: curl is not installed. Please install curl and try again.")
            exit(1)

        # Prompt the user to enter the URL
        url_to_fetch = input("Enter the URL to fetch: ").strip()

        # Check if the entered URL is not empty
        if not url_to_fetch:
            raise ValueError("URL cannot be empty.")

        # Prompt user for saving to file
        save_to_file_option = input("Do you want to save the output to a file? (y/n): ").lower() == 'y'

        if save_to_file_option:
            print("Available output formats: txt, json, xml, csv, etc.")
            print("The recommended format is json.")
            file_format = input("Enter the desired file format: ").strip()
            run_curl_command(url_to_fetch, save_output=True, file_format=file_format)
        else:
            run_curl_command(url_to_fetch)

    except ValueError as ve:
        # Handle invalid user input
        logging.error(f"Error: {ve}")

    except KeyboardInterrupt:
        logging.info("\nScript interrupted by user.")
    except EOFError:
        logging.error("\nError: Unexpected end of input.")
