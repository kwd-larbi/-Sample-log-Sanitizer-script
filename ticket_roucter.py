# check if folders are in the directory
# 1.scan the directory regardless of linux or MacOs
import os
# 2.regx pattern
import re
# 3. CSV
import csv


# The Gatekeeper Pattern with 4 explicit capturing groups
TICKET_PATTERN = r"^(ERROR|WARNING|INFO)\s+\[pid:(\d+)\]\s+(.*?)\s+-\s+User:(EMP\d{4})$"
def sanitize_and_route_tickets(input_dir, output_csv_path):
    """Crawls a directory, streams text files, applies regular expressions, and creates a CSV grid."""
    parsed_tickets = []
    # if directory exist
    if not os.path.exists(input_dir):
        print(f" Error: The director '{input_dir}' was not found.")
        return

    # Directory Traversal
    for filename in os.listdir(input_dir):
        if filename.endswith(".log") or filename.endswith(".txt"):# this reads the directory for any log or txt
            file_path = os.path.join(input_dir, filename) # ready to open folder and file

            #opening file line by line
            with open(file_path, "r") as file:
                for line_num, line in enumerate(file, 1):
                    clean_line = line.strip()

                    # Run the regex scanner
                    match = re.match(TICKET_PATTERN, clean_line)

                    if match:
                        # ROUTE A: The Clean Path (Extract groups 1, 2, 3, 4)
                        parsed_tickets.append({
                            "Ticket ID": f"TICK-{match.group(2)}",
                            "Priority": match.group(1),
                            "System Message": match.group(3),
                            "Assigned Employee": match.group(4)
                        })
                    else:
                        # ROUTE B: The Audit Path (Catches all dirty or noise rows!)
                        parsed_tickets.append({
                            "Ticket ID": "MALFORMED-LOG",
                            "Priority": "AUDIT_REQUIRED",
                            "System Message": f"[Line {line_num}] Raw Data: {clean_line}",
                            "Assigned Employee": "SYSTEM_ADMIN"
                        })

                        # Output layer Mapping
                        fields = ["Ticket ID", "Priority", "System Message", "Assigned Employee"]

                        with open(output_csv_path,"w", newline="") as csv_file:
                            writer = csv.DictWriter(csv_file, fieldnames=fields)
                            writer.writeheader()
                            writer.writerows(parsed_tickets)

                print(f"📊 Process Complete! 100% of data audited. Dashboard built at: '{output_csv_path}'")


if __name__ == "__main__":
    # Define our functional runtime paths
    intake_directory = "unprocessed_tickets"
    final_dashboard_report = "structured_it_dashboard.csv"

    # Fire up the automation pipeline engine
    sanitize_and_route_tickets(intake_directory, final_dashboard_report)