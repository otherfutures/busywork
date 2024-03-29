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
import subprocess
import random
import time
import requests
from datetime import datetime, timedelta
import sys


# Git commit messages
EDIT_MESSAGE = "Self-edit: Add current date"
REVERT_MESSAGE = "Revert self-edit"

# The pointless edit that's being added & removed
BUSYWORK_MESSAGE = datetime.now().strftime("%Y-%m-%d")

# Toggle whether the program will randomly update tdy.
#  True == 50/50 chance of it committing/reverting tdy.
#  False == Consistent & daily updates
RANDOMLY_UPDATE = True

# Range of commits; exact no. chosen by random_calls()
MIN_CALLS = 1
MAX_CALLS = 30

# Toggle whether to commit/revert a rand. no. of times
RANDOM_NUMBER_OF_UPDATES = True

# Toggle whether to wait b/w commit/revert cycles
WAIT = False

# Wait intervals
MIN_WAIT = 30  # Seconds
MAX_WAIT = 125  # Seconds

# Checking for internet
RETRY_INTERVAL = 6  # minutes
MAX_RETRIES = 60 // RETRY_INTERVAL  # Retry for an hr.


def main():
    counter = 0

    if RANDOMLY_UPDATE:
        update_today = random_updater()
    else:
        update_today = True

    if update_today:
        # Check internet conn.
        open_github(counter)

        # Read the script filepath from the secrets text file
        filepath = read_filepath()

        # Get rand. no. if RANDOM var. is toggled True
        if RANDOM_NUMBER_OF_UPDATES:
            num_calls = random_calls()
        else:
            num_calls = 1

        # Pushes the commit, then pushes the reversion
        for _ in range(num_calls):
            try:
                # The actual edits & pushing
                make_edit(counter, filepath)
                revert_edit(counter, filepath)
                counter += 1

                # Wait a rand. amt. of time b/w commit/revert cycles
                if RANDOM_NUMBER_OF_UPDATES and WAIT:
                    delay = random.uniform(MIN_WAIT, MAX_WAIT)
                    time.sleep(delay)
            except Exception as e:
                open_github(counter)

    finish(counter)


def read_filepath():
    """Reads the script filepath from a secrets text file."""
    try:
        with open("secrets.txt", "r") as file:
            return file.readline().strip()
    except FileNotFoundError:
        print("Can't find secrets.txt")
        sys.exit(1)


def random_calls():
    """Generate a rand. no. of how many times script is run"""
    return random.randint(MIN_CALLS, MAX_CALLS)


def random_updater():
    """Rand. decides if the program will commit/revert"""
    return random.choice([True, False])


def open_github(counter):
    """Checks to see if there's internet & can push to GitHub"""

    URL = "https://github.com"
    HEADERINFO = {"User-Agent": "Mozilla/5.0"}

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(URL, headers=HEADERINFO)
            if response.status_code == 200:
                return
        except Exception as e:
            # Get the current date and time
            current_datetime = datetime.now()
            new_datetime = (
                current_datetime + timedelta(minutes=RETRY_INTERVAL)
            ).strftime("%H:%M")

            print(
                f"\n\nError! Failed to open GitHub - Attempt {attempt + 1}/{MAX_RETRIES}"
                f"\nStatus Code: {response.status_code}"
                f"\nWill try again in {RETRY_INTERVAL} minutes (i.e. at {new_datetime})"
            )
            time.sleep(RETRY_INTERVAL * 60)  # Wait 6 min. before retrying

    print(
        f"\n\nUnable to open GitHub after one hour. Program stopped."
        f"\nLast response status code: {response.status_code} ({response.text})"
    )
    finish(counter)
    sys.exit(1)  # Terminate w/ err.


def make_edit(counter, script_path):
    """Makes a small edit to the script, commits, and pushes the changes."""

    while True:
        try:
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
            break
        except Exception as e:
            open_github(counter)


def revert_edit(counter, script_path):
    """Reverts the last edit, commits the revision, and pushes the changes."""

    while True:
        try:
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
            break

        except Exception as e:
            open_github(counter)


def finish(counter):
    print(f"\n-----FINISHED WORKING-----\n\n{counter * 2} Commits")


if __name__ == "__main__":
    main()
# Pointless Edit: 2024-03-30
