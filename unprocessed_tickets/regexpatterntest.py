#import re
import re

# search for ERROR|DEBUG|INFO [any id]
test_pattern = r"^(ERROR|DEBUG|INFO)\s+\[pid:(\d+)\]\s+(.*?)\s+-\s+User:(EMP\d{4})$"

print("search for ERROR|DEBUG|INFO or [any id]")

with open("incoming_tickets.log", "r") as file:
    match_count = 0
    total_lines = 0

    # searching through every single line
    for line_num, line in enumerate(file, 1):
        total_lines += 1
        clean_line = line.strip()

        # searching for targets anywhere
        match = re.match(test_pattern, clean_line)

        if match:
            match_count +=1
            # successful line
            print(f" [Line {line_num} MATCH] Found Prefix: {match.group(1)}")
            print(f"    ↳ Raw Line: '{clean_line}'\n")
        else:
            # Optional: You can uncomment the line below if you want to see what failed
            #print(f"🔴 [Line {line_num} NO MATCH] '{clean_line}'\n")
            pass

print("=" * 60)
print(f"SEARCH COMPLETE: Found {match_count} matching lines out of {total_lines} total lines.")