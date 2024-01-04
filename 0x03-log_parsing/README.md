# Log parser
 **Here's a breakdown of the script's logic without actual code:**

**1. Reading Input:**

- The script will continuously read lines from standard input (stdin), which means it can accept input directly from a user or another program's output.
- It will process each line individually.

**2. Handling Input Format:**

- For each line, it will check if it matches the specified format:
    - `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- If a line doesn't match this format, it will be skipped and not processed further.

**3. Extracting Data:**

- If a line matches the format, the script will extract the following information:
    - Status code
    - File size

**4. Accumulating Metrics:**

- **Total file size:** The script will keep track of the total file size by adding up the file size values from each processed line.
- **Number of status code:** It will create a counter for each possible status code (200, 301, 400, 401, 403, 404, 405, 500) and increment the corresponding counter for each line.

**5. Printing Statistics:**

- After every 10 lines **or** if a keyboard interruption (CTRL+C) is detected, the script will print the following statistics:
    - **Total file size:** `File size: <total size>`, where `<total size>` is the accumulated file size.
    - **Number of lines by status code:** It will print each status code with its count in ascending order, only for status codes that have appeared in the input.

**6. Termination:**

- The script will continue processing lines and printing statistics until it reaches the end of stdin or is interrupted by the user (CTRL+C).
