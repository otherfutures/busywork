"""
busywork is simple automation program that pumps up GitHub contribution stats
by creating pointless edits to itself. It also emulates the feeling of agile, I guess. 

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
import random
import time
from datetime import datetime


# Git commit messages
EDIT_MESSAGE = "Self-edit: Add current date"
REVERT_MESSAGE = "Revert self-edit"

# The pointless edit that's being added & removed
BUSYWORK_MESSAGE = datetime.now().strftime("%Y-%m-%d")

# Toggle whether the program will randomly update tdy.
    #  True == 50/50 chance of it committing/reverting tdy.
    #  False == Consistent & daily updates
RANDOMLY_UPDATE = False

# Toggle whether to commit/revert a rand. no. of times
RANDOM_NUMBER_OF_UPDATES = True

# Toggle whether to wait b/w commit/revert cycles
WAIT = False


def main():
    counter = 0

    if RANDOMLY_UPDATE:
        update_today = random_updater()
    else:
        update_today = True

    if update_today:
        # Read the script filepath from the secrets text file
        filepath = read_filepath()

        # Get rand. no. if RANDOM var. is toggled True
        if RANDOM_NUMBER_OF_UPDATES:
            num_calls = random_calls()
        else:
            num_calls = 1

        # Pushes the commit, then pushes the reversion 
        for _ in range(num_calls):
            make_edit(filepath)
            revert_edit(filepath)
            counter += 1
            # Wait a rand. amt. of time b/w commit/revert cycles
            if RANDOM_NUMBER_OF_UPDATES and WAIT:
                min_delay = 30  # Seconds
                max_delay = 125  # Seconds
                delay = random.uniform(min_delay, max_delay)
                time.sleep(delay)

        print(f"\n\n-----FINISHED WORKING-----\n\n{counter * 2} Commits")


def read_filepath():
    """Reads the script filepath from a secrets text file."""
    try:
        with open("secrets.txt", "r") as file:
            return file.readline().strip()
    except FileNotFoundError:
        print("Can't find secrets.txt")
        quit()


def random_calls():
    """Generate a rand. no. to run scripts"""
    min_calls = 1
    max_calls = 10
    return random.randint(min_calls, max_calls)


def random_updater():
    """Rand. decides if the program will commit/revert"""
    return random.choice([True, False])


def make_edit(script_path):
    """Makes a small edit to the script, commits, and pushes the changes."""
    with open(script_path, "r") as file:
        lines = file.readlines()  # Read this .py file

    # Make the edit by appending the pointless edit to this file
    lines.append(f"# Pointless Edit: {BUSYWORK_MESSAGE}\n")

    # Write the modified content back to the file
    with open(script_path, "w") as file:
        file.writelines(lines)

    # Use Git commands to stage, commit, and push the changes
    os.system("git add .")
    os.system(f'git commit -m "{EDIT_MESSAGE}"')
    os.system("git pull")
    os.system("git push")


def revert_edit(script_path):
    """Reverts the last edit, commits the revision, and pushes the changes."""

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
    os.system("git pull")
    os.system("git push")


if __name__ == "__main__":
    main()
# Pointless Edit: 2023-07-17
