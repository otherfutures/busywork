import os
import datetime

EDIT_MESSAGE = "UNIT TEST"

with open("secrets.txt", "r") as file:
    script_path = file.readline().strip()

print(f"script_path: {script_path}")

"""Makes a small edit to the script, commits, and pushes the changes."""
# Read the source code file
with open(script_path, "r") as file:
    lines = file.readlines()

# print(f"lines: {lines}")

# Make the edit by appending the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
lines.append(f"# Edit: {current_date}\n")

print(f"current_date: {current_date}")

# Write the modified content back to the file
with open(script_path, "w") as file:
    file.writelines(lines)

# # Use Git commands to stage, commit, and push the changes
# os.system("git add .")
# os.system(f'git commit -m "{EDIT_MESSAGE}"')
# os.system("git push")
