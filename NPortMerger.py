#!/usr/bin/env python
# Author: Сухас Дхолз
# Link: https://github.com/GTekSD/
import argparse
import pyperclip
import re

def display_gteksd():
    gteksd = """
 _____            _    _____                          
|  _  |NESSUS___ | |_ |     | ___  ___  ___  ___  ___ 
|   __|| . ||  _||  _|| | | || -_||  _|| . || -_||  _|
|__|   |___||_|  |_|  |_|_|_||___||_|  |_  ||___||_|  
             Created by Team GTekSD    |___|             
            https://gteksd.github.io/
------------------------------------------------------
    """
    print(gteksd)

def parse_input_file(file):
    data = {}
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            parts = line.split(':')
            if len(parts) == 2:
                key = parts[0].strip()
                value = int(parts[1].strip())
                if key not in data:
                    data[key] = set()
                data[key].add(value)
            else:
                # If there's a single space or tab, replace it with a colon
                adding_colon = re.sub("\s",":",line,1)
                corrected_line = re.sub("\s","",adding_colon)
                parts = corrected_line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = int(parts[1].strip())
                    if key not in data:
                        data[key] = set()
                    data[key].add(value)
    return data

def merge_and_display_ports(data):
    for key in sorted(data.keys()):
        sorted_ports = sorted(data[key])
        ports_str = ', '.join(str(port) for port in sorted_ports)
        print(f"{key}: {ports_str}")

def copy_to_clipboard(data):
    result = ""
    for key in sorted(data.keys()):
        sorted_ports = sorted(data[key])
        ports_str = ', '.join(str(port) for port in sorted_ports)
        result += f"{key}: {ports_str}\n"
    pyperclip.copy(result)
    print("BOOM!!!\nResult copied to clipboard.")


def main():
    parser = argparse.ArgumentParser(description="""The Nessus Port Merger is designed to merge and sort port listed for domains/IP addresses provided in an input file. The script removes duplicates, sorts the ports in ascending order, and displays the merged ports for each domain/IP.""")
    parser.add_argument("input_file", help="Input file containing domain names or IP addresses with ports, it can be in any format")
    parser.add_argument("-cp", "--copy", action="store_true", help="Copy output result to clipboard")
    parser.add_argument("--silent", action="store_true", help="Suppress gteksd/banner display")

    args = parser.parse_args()

    if not args.silent:
        display_gteksd()

    try:
        data = parse_input_file(args.input_file)

        cleaned_data = {}
        for key, ports in data.items():
            cleaned_data[key] = sorted(ports)

        if not args.copy:
            merge_and_display_ports(cleaned_data)
        else:
            copy_to_clipboard(cleaned_data)

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
