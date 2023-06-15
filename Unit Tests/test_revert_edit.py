import os

REVERT_MESSAGE = "UNIT TEST"

with open("secrets.txt", "r") as file:
    script_path = file.readline().strip()

print(f"script_path: {script_path}")

"""Reverts the last edit, commits the revision, and pushes the changes."""
# Read the source code file
with open(script_path, "r") as file:
    lines = file.readlines()

print(f"lines: {lines}")

# Remove the last line (the edit)
lines = lines[:-1]

print(f"lines: {lines}")

# Write the revised content back to the file
with open(script_path, "w") as file:
    file.writelines(lines)

# # Use Git commands to stage, commit, and push the revision
# os.system("git add .")
# os.system(f'git commit -m "{REVERT_MESSAGE}"')
# os.system("git push")
