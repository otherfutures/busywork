"""
busywork is simple automation program that pumps up GitHub contribution numbers
by creating pointless edits to itself. 

If
    a) git is installed, &
    b) a cron job or task is scheduled on the user's computer, it'll:

        run once a day & add a comment at the end of the file,
        commit & push itself to the GitHub repository,
        revert itself back to its original state (i.e. remove the comment), &
        commit & push itself again.

A program for slackers who don't want their activities quantified or measured with 
total accuracy.
"""

import os
import datetime


# Git commit messages
EDIT_MESSAGE = "Self-edit: Add current date"
REVERT_MESSAGE = "Revert self-edit"

# The pointless edit that's being added & removed
BUSYWORK_MESSAGE = datetime.datetime.now().strftime("%Y-%m-%d")


def read_script_path():
    """Reads the script path from a secrets text file."""
    with open("secrets.txt", "r") as file:
        return file.readline().strip()


def make_edit(script_path):
    """Makes a small edit to the script, commits, and pushes the changes."""
    # Read the source code file
    with open(script_path, "r") as file:
        lines = file.readlines()

    # Make the edit by appending the pointless edit to this file
    lines.append(f"# Pointless Edit: {BUSYWORK_MESSAGE}\n")

    # Write the modified content back to the file
    with open(script_path, "w") as file:
        file.writelines(lines)

    # Use Git commands to stage, commit, and push the changes
    os.system("git add .")
    os.system(f'git commit -m "{EDIT_MESSAGE}"')
    os.system("git push")


def revert_edit(script_path):
    """Reverts the last edit, commits the revision, and pushes the changes."""
    # Read the source code file
    with open(script_path, "r") as file:
        lines = file.readlines()

    # Remove the last line (the edit)
    lines = lines[:-1]

    # Write the revised content back to the file
    with open(script_path, "w") as file:
        file.writelines(lines)

    # Use Git commands to stage, commit, and push the revision
    os.system("git add .")
    os.system(f'git commit -m "{REVERT_MESSAGE}"')
    os.system("git push")


def main():
    # Read the script path from the secrets text file
    script_path = read_script_path()

    make_edit(script_path)
    revert_edit(script_path)


if __name__ == "__main__":
    main()
