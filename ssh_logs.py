import os
import datetime

ssh_file = '/var/log/auth.log'
store_file = '/home/zeeshan/Desktop/file.log'

# Function to check if a log entry is older than 5 minutes
def older_logs(log_entry):
    try:
        # Extract the timestamp from the log entry
        time = ' '.join(log_entry.split()[:3])
        log_time = datetime.datetime.strptime(time, '%b %d %H:%M:%S')


        # Calculate the time difference
        current_time = datetime.datetime.now()
        time_difference = current_time - log_time

        return time_difference.total_seconds() > 300
    except Exception as e:
        print(e)

# Read the SSH log file
with open(ssh_file, 'r') as file:
    ssh_entries = file.readlines()

# Filter log entries older than 5 minutes
filtered_entries = [entry.strip() for entry in ssh_entries if older_logs(entry)]

if filtered_entries:
    with open(store_file, 'w') as desktop_log:
        for entry in filtered_entries:
            desktop_log.write(entry + '\n')
