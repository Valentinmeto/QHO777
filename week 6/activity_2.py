import csv


def extract(path_file):
    print("Extracting...", end="")
    file = open(path_file, "r")
    csv_reader = csv.reader(file)
