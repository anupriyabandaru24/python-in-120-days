def count_error_lines(filename):
    """Counts how many lines in a file contain the word 'ERROR'. Returns 0 if the file doesn't exist."""
    try:
        with open(filename) as f:
            c = 0
            for line in f:
                if "ERROR" in line:
                    c += 1
            return c
    except FileNotFoundError:
        return 0


def read_first_n_lines(filename, n):
    """Returns the first n lines of a file as a list, with newlines stripped."""
    with open(filename) as f:
        c = 0
        list_n = []
        for line in f:
            if c != n:
                list_n.append(line.strip())
                c += 1
            else:
                break
        return list_n


def extract_errors(filename):
    """Returns a list of all lines containing 'ERROR', stripped of whitespace."""
    with open(filename) as f:
        list_err = []
        for line in f:
            if "ERROR" in line:
                list_err.append(line.strip())
        return list_err


def write_errors_to_file(input_file, output_file):
    """Reads input_file and writes only the lines containing 'ERROR' to output_file."""
    with open(input_file) as f_in:
        with open(output_file, "w") as f_out:
            for line in f_in:
                if "ERROR" in line:
                    f_out.write(line)


def safe_read(filename):
    """Safely reads a file's content, handling missing files and unexpected errors."""
    try:
        with open(filename, "r") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return f"File not found: {filename}"
    except Exception as e:
        return f"Unexpected error: {e}"


def count_log_levels(filename):
    """Counts how many lines contain ERROR, WARNING, and INFO respectively."""
    with open(filename) as f:
        dictionary = {}
        for line in f:
            if "ERROR" in line:
                dictionary["ERROR"] = dictionary.get("ERROR", 0) + 1
            elif "WARNING" in line:
                dictionary["WARNING"] = dictionary.get("WARNING", 0) + 1
            elif "INFO" in line:
                dictionary["INFO"] = dictionary.get("INFO", 0) + 1
        return dictionary


def average_line_length(filename):
    """Returns the average number of characters per line in a file."""
    with open(filename) as f:
        count = 0
        total = 0
        for line in f:
            a = line.strip()
            total += len(a)
            count += 1
        if count == 0:
            return 0
        else:
            return total / count


def find_longest_line(filename):
    """Returns the longest line in a file and its length, as a (line, length) tuple."""
    with open(filename) as f:
        max_len = 0
        lon_line = ""
        for line in f:
            a = line.strip()
            curr_len = len(a)
            max_len = max(max_len, curr_len)
            if len(lon_line) < curr_len:
                lon_line = a
        return (lon_line, max_len)


def merge_log_files(file1, file2, output_file):
    """Merges lines from two files, sorts them alphabetically, and writes them to output_file."""
    with open(file1) as f1, open(file2) as f2, open(output_file, "w") as out:
        merge_list = []
        for line in f1:
            merge_list.append(line.strip())
        for line in f2:
            merge_list.append(line.strip())
        sorted_list = sorted(merge_list)
        for line in sorted_list:
            out.write(line + "\n")


def parse_log_summary(filename):
    """Reads a log file and returns total lines, error count, and unique word count."""
    with open(filename) as f:
        linecount = 0
        errorcount = 0
        combinedtext = ""
        for line in f:
            linecount += 1
            combinedtext += line.strip().lower() + " "
            if "ERROR" in line:
                errorcount += 1
        combinedtext = combinedtext.replace('.', '')
        combinedtext = combinedtext.replace(',', '')
        clean_text = combinedtext.split()
        unique_words = set(clean_text)
        dictionary = {"total_lines": linecount, "error_count": errorcount, "unique_words": len(unique_words)}
        return dictionary