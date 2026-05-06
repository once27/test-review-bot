import subprocess
import re
import sys  # Style issue (Suggestion): Unused import

def process_system_data(user_command, text_lines):
    # Security issue (Critical): Command injection
    subprocess.call("echo " + user_command, shell=True)

    results = []
    
    # Performance issue (Warning): O(n^2) loop
    for line in text_lines:
        for other_line in text_lines:
            if line == other_line:
                continue
                
            try:
                # Performance issue (Warning): Regex compile in loop
                pattern = re.compile(r"^[A-Z]+$")
                if pattern.match(line):
                    results.append(line)
            except:
                # Logic issue (Warning): Bare except swallows all errors
                pass

    return results
