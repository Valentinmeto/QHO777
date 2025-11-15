# activity 1
def directions():
    steps = ["Move forward", "Move backword", " Turn Right", "Turn Left"]
    return steps


def run_task1():
    movements = directions()
    print(movements)


if __name__ == "__main__":
    run_task1()

    # ACTIVITY 2


def movements():
    path = ["Move forward", 10, "Move backword", 5, " Turn Right", 3, "Turn Left", 1]
    return path


def run_task2():
    print("Moving...")
    path = movements()

    for i in range(0, len(path), 2):
        direction = path[i]
        steps = path[i + 1]
        print(f"{direction} for {steps} steps")


if __name__ == "__main__":
    run_task2()


# ACTIVITY 3
def directions():
    return ["Move forward", "Move backword", " Turn Right", "Turn Left"]


def menu():
    print("Please select a direction:")
    steps = directions()

    for index in range(len(steps)):
        print(f"{index}. {steps[index]}")


def run_task3():
    menu()


if __name__ == "__main__":
    run_task3()
