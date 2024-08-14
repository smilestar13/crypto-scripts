import csv


def determine_delimiter(line):
    if ';' in line:
        return ';'
    elif ':' in line:
        return ':'
    return None


def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        for line in infile:
            line = line.strip()
            delimiter = determine_delimiter(line)

            if delimiter:
                columns = line.split(delimiter)
                writer.writerow(columns)
            else:
                print(f"No known delimiter found in line: {line}")


input_file = 'input.txt'
output_file = 'output.csv'

process_file(input_file, output_file)
