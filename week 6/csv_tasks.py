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
