# Python File I/O and JSON Handling: Comprehensive Guide

"""
Efter Jahan Ema
ID: C193229
Email: c193229@ugrad.iiuc.ac.bd
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
import csv
import json

def csv_to_json(csv_file, json_file):
    products = []
    with open('product.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product_Name", "Price", "Condition"])
        writer.writerow(["TV", 52000, "Fresh"])
        writer.writerow(["Laptop", 50000, "New"])
        writer.writerow(["AC", 83000, "Fresh"])
    
    with open('product.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            products.append(row)
            
    with open('products.json', 'w') as file:
        json.dump(products, file, indent=4)

csv_to_json('products.csv', 'products.json')

# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.
import datetime

def w_log(message, log_file):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_time = f"[{timestamp}] {message}\n"
    
    with open(log_file, 'a') as file:
        file.write(log_time)

w_log("Here is your messages.", "log_msg.log")

# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.
