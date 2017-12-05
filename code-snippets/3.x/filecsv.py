# 28 Mar 2017 | Read / Write delimited files

import csv
'''
# Header Record: Without
with open('sample_input.csv', 'r', newline='') as file_read:
    reader = csv.reader(file_read, delimiter=',', quoting=csv.QUOTE_ALL)

    with open('sample_output.csv', 'w', newline='') as file_write:
        writer = csv.writer(file_write, delimiter='|', quoting=csv.QUOTE_NONE)

        for row_read in reader:
            row_write = row_read
            row_write[0] = str(row_write[0]).upper()
            if row_write[2] == '':
                row_write[2] = '1900'

            writer.writerow(row_write)
'''
# Header Record: With
with open('sample_input.csv', 'r', newline='') as file_read:

    # Check if file has header record
    snf = csv.Sniffer().has_header(file_read.read(100))
    print('Has Header?', snf)
    file_read.seek(0)

    reader = csv.DictReader(file_read, delimiter=',', quoting=csv.QUOTE_ALL)
    fieldnames = reader.fieldnames

    with open('sample_output.csv', 'w', newline='') as file_write:
        writer = csv.DictWriter(file_write, fieldnames=fieldnames, delimiter='|', quoting=csv.QUOTE_NONE)
        writer.writeheader()

        for row_read in reader:
            row_write = row_read
            row_write['TITLE'] = str(row_write['TITLE']).upper()
            if row_write['YEAR'] == '':
                row_write['YEAR'] = '1900'

            writer.writerow(row_write)