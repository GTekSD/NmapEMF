"""
Nmap Parser (nparser)

Description:
This script is designed to parse Nmap scan results and filter the ports based on their states (open, closed, filtered). It takes an Nmap output file and organizes the information, allowing users to quickly identify active services on the scanned hosts.

Usage:
To use the script, provide the path to an Nmap output file as a positional argument. You can optionally specify an output file to save the results, or filter the results by only showing open, closed, or filtered ports.

Example:
1. To parse an Nmap output file and display results on the console:
   python nparser.py nmap-output.txt

2. To save the filtered output to a file:
   python nparser.py nmap-output.txt -o converted-output.txt

3. To show only open ports:
   python nparser.py nmap-output.txt -op

4. To show only closed ports:
   python nparser.py nmap-output.txt -cp

5. To show only filtered ports:
   python nparser.py nmap-output.txt -fp
"""


import argparse

# Banner
BANNER = """
    _   ______                           
   / | / / __ \____ ______________  _____
  /  |/ / /_/ / __ `/ ___/ ___/ _ \/ ___/
 / /|  / ____/ /_/ / /  (__  )  __/ /    
/_/ |_/_/    \__,_/_/  /____/\___/_/     
                          
 Parse and filter Nmap scan results 
---------Created by GTekSD----------
"""

# Function to parse the Nmap output file
def parse_nmap_output(file_content, filter_ports=None):
    parsed_data = {}
    current_host = None

    for line in file_content:
        line = line.strip()
        if line.startswith("Nmap scan report for"):
            current_host = line.split(" ")[-1]
            parsed_data[current_host] = []
        elif line and current_host:
            if "/tcp" in line or "/udp" in line:
                port, state, service = line.split()[:3]
                port_number = port.split("/")[0]
                if filter_ports:
                    if (filter_ports == 'open' and state == 'open') or \
                       (filter_ports == 'closed' and state == 'closed') or \
                       (filter_ports == 'filtered' and state == 'filtered'):
                        parsed_data[current_host].append(port_number)
                else:
                    parsed_data[current_host].append(port_number)
    
    return parsed_data

# Function to display or write output
def display_output(parsed_data, output_file=None):
    output = ""
    for host, ports in parsed_data.items():
        if ports:
            output += f"{host} -p {','.join(ports)}\n"

    if output_file:
        with open(output_file, 'w') as f:
            f.write(output)
    else:
        print(output)

# Main function to handle arguments and run the script
def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description=
        " [i]  Nmap Output Parser (NParser): A tool to parse Nmap results and filter ports by their states.\n\n"
	"[Tip] Automate your scanning process with the Batch is Better (bisb) tool.\n"
	"  +   Example: bisb \"nmap -Pn -sV\" nparser-output.txt\n"
	"  |_  This runs Nmap for each target in your output file, saving you time and effort.\n\n"
	" [!]  Why do it manually when you can do it automatically?\n"
	" [i]  Download bisb here: https://github.com/GTeKSD/batch-is-better",

                    
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument('nmap_output', help="Path to the Nmap output text file")
    parser.add_argument('-o', '--output', help="Path to save the converted output (optional)")
    parser.add_argument('-op', '--open_ports', action='store_true', help="Show only open ports")
    parser.add_argument('-cp', '--closed_ports', action='store_true', help="Show only closed ports")
    parser.add_argument('-fp', '--filtered_ports', action='store_true', help="Show only filtered ports")
    
    args = parser.parse_args()
    
    # Read the input file
    with open(args.nmap_output, 'r') as file:
        file_content = file.readlines()
    
    # Determine the filtering based on user arguments
    filter_ports = None
    if args.open_ports:
        filter_ports = 'open'
    elif args.closed_ports:
        filter_ports = 'closed'
    elif args.filtered_ports:
        filter_ports = 'filtered'
    
    # Parse the Nmap output
    parsed_data = parse_nmap_output(file_content, filter_ports=filter_ports)
    
    # Display or save the output
    display_output(parsed_data, output_file=args.output)

if __name__ == "__main__":
    main()
