name, surname = "", ""

while name == "":
    name = input("Your First name: ")

while surname == "":
    surname = input("Your Last name: ")

f = lambda gn, gs: gn.strip().title() + " " + gs.strip().title()

print(f(name, surname))
