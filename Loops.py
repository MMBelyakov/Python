# while_example1
response = ""
while response != "exit":
    response = input("Type 'exit' to exit: ")

# while_example2

n = 1
while n <= 3:
    print("n = ", n)
    n += 1

# while_example3

number = 0
while number <= 0:
    number = int(input("Enter a positive integer: "))

print("You have entered", number)

# while_example4

print("All natural numbers :")

n = 2
# while True:
#   print(n)
# n **=2

# break_example1

while True:
    print("Enter 'exit' to exit loop")
    response = input(">")
    if response == "exit":
        break

print("Loop has stopped.")

# break_example2

name = None

while True:
    print("Menu:")
    print("1. Enter a name")
    print("2. Print greeting")
    print("3. Quit")

    response = input("Please choose a action: ")

    print()

    if response == "1":
        name = input("Enter your name: ")
    elif response == "2":
        if name:
            print("Hello,", name, "!", sep='')
        else:
            print("I don't know your name")
    elif response == "3":
        break
    else:
        print("Incorrect input")

    print()

# continue_example1

number = 0
while number < 10:
    number += 1
    if number == 5:
        continue
    print("Current number is: ", number)

# while_else

counter = 5
while counter != 0:
    print(counter)
    counter -= 1
print("Loop is complete")
print("counter = ", counter)

# while_else_break

attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    password = input("Enter your password"
                     "(you have {} left)".format(attempts_left + 1))
    if password == "98eaxc":
        print("Access granted")
        break
else:
    print("Access denied")

# for_example1
for i in range(10):
    print("i =", i)

# for_break
for i in range(10):
    if i == 8:
        break
    print(i)

for i in range(10):
    if i == 8:
        continue
    print(i)

# for_else

for attempts_left in range(3, 0, -1):
    password = input("Enter a password: "
                     "(you have {} attempts left)".format(attempts_left))
    if password == "98eaxc":
        print("Access granted")
        break
    else:
        print("Access denied")

# nested loops

for row in range(5):
    for column in range(30):
        print("*" , end="")
    print()
