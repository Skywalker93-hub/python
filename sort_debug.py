# Variables
old_filename="log.txt"
new_filename="new_log.txt"

import re
   
def read_log_data(old_filename):
    with open(old_filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line
    
def write_processed_log(new_filename, processed_data):
    with open(new_filename, 'w+', encoding='utf-8') as f:
       f.writelines(processed_data)

def process_log(old_filename):
    processed_data = []
    for line in read_log_data(old_filename):
        if re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} DEBUG:', line):
            processed_data.append(line)

    write_processed_log(new_filename, processed_data)

process_log(old_filename)  
print ("Processing complete. Check the new log file for DEBUG entries.")
