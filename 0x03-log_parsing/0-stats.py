#!/usr/bin/python3
"""Log parsing"""
import sys


def parse_line(line):
    """parse line for correct format"""
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except Exception as err:
        return None, None, None


def print_metrics(total_file_size, status_code_counts):
    """Print the metrics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")


total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

line_count = 0

try:
    for line in sys.stdin:
        ip_address, status_code, file_size = parse_line(line)
        if ip_address is not None:
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            print_metrics(total_file_size, status_code_counts)
finally:
    print_metrics(total_file_size, status_code_counts)
