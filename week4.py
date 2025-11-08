def sum_weight():
    person = float(input("What is persons's weight?"))
    inventory = float(input("What is the wight of the inventory?"))
    total = person + inventory
    return total


def cal_average(w1, w2):
    return (w1 + w2) / 2


def run():
    choice = input("What would you like to do?")
    if choice == "sum":
        result = sum_weight()
        print("The sum is: ", result)
    elif choice == "cal average":
        person = float(input("What is persons's weight?"))
        inventory = float(input("What is wight of the inventory?"))
        result = cal_average(person, inventory)
        print("The average is: ", result)


run()
