import csv


def read_csv(file_path):
    file = open(file_path, "r")
    csv_reader = csv.reader(file)

    headings = next(csv_reader)
    print("Headings:")
    print(headings)

    print("Values:")
    for values in csv_reader:
        print(values)

    file.close()


def run_task1():
    read_csv("clothing.csv")


if __name__ == "__main__":
    run_task1()


def extract(path_file):
    print("Extracting...", end="")
    file = open(path_file, "r")
    csv_reader = csv.reader(file)

    next(csv_reader)
    names = ""  # empty variable
    for values in csv_reader:
        item_name = values[1]
        names += item_name + "\n"
    file.close()

    print("Done!")
    print("The extracted items are:")
    print(names.strip())


def run_task2():
    extract("clothing.csv")


if __name__ == "__main__":

    run_task2()
