"""Reads the script path from a secrets text file."""
with open("secrets.txt", "r") as file:
    print(file.readline().strip())
