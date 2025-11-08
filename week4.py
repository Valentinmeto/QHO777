def ladders_taken(jump):
    print("how many steps are remaning?")
    print (jump)
    for i in range(jump):
        print("| |")
        print("***")
print("###")
print("$$$")
def ask_draw():
    values = int(input("How many steps has been taken? "))
    ladders_taken(values)


ask_draw()
