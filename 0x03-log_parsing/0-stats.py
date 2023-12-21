#!/usr/bin/python3
import sys

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
        line_count += 1
        try:
            ip, _, date, _, status_code, file_size = line.split(maxsplit=5)
            file_size = int(file_size)
        except ValueError:
            continue

        total_file_size += file_size
        status_code_counts[int(status_code)] += 1

        if line_count % 10 == 0 or line_count == 1:
            print("File size:", total_file_size)
            for code in sorted(status_code_counts):
                count = status_code_counts[code]
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    pass
