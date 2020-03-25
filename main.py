def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac



run = True
while run:
    number = (input(">>> Enter a number or any command\n"))
    try:
        print(factorial(int(number)))
        user_input = input(">>> Want to try again [y / n]\n")
        if user_input == "y":
            run = True
            print(">>> Setting up Factorial Calculator ...")
            print(">>> Done ✓✓✓")
        elif user_input == "n":
            run = False
            print(">>> Quitting Factorial Calculator ...")
            print(">>> GOODBYE 👋👋👋")
        else:
            print("INVALID SYNTAX type exit() to quit")
    except Exception as e:
        if number == "exit()":

            print(">>> Quitting Factorial Calculator ...")
            print(">>> GOODBYE 👋👋👋")
            run = False
        elif number == "help()":
            print(">>> This is a factorial calculator created by Kartikaye"
                  " Rishi of India", "Rate us on Play Store and App Store")

        else:
            print("Invalid Syntax")



