#Kiril Krushkov
#Git_verkefni
#In english

main = "Yup"
while main == "Yup":
    print("Number *1*")
    print("Name *2*")
    print("Text *3*")
    print("Exit *4*")
    line = int(input("1-4 your choice: "))

    if line == 1:

        ex1 = int(input("First number: "))
        ex2 = int(input("Second number: "))
        x = ex1 + ex2
        y = ex1 * ex2
        print("This is the result of #+#:", x)
        print("This is the result of #*#:", y)

    if line == 2:

        FName = input("Write your first name: ")
        LName = input("Write your second name: ")
        print("This is your full name: ", FName, LName)

    if line == 3:

        text = input("Write a text: ")
        a = 0
        b = 0
        c = 0
        for x in range(len(text)):
            if text[x].isupper():
                a += 1
            elif text[x].islower():
                b += 1
                if x > 0 and text[x - 1].isupper():
                    c += 1
        print("They are:", a, "sentence/s.", "Small letters:", b, "and big letters:", c, "- Cutters come immediately after uppercase.")

    if line == 4:
        print("Thank you! By Kiril")
        break







