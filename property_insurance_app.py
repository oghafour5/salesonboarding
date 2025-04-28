# property insurance app - bad code example

import time

def doall():
    a = input("What is your name: ")
    b = input("how old r u: ")
    c = input("whats ur property worth: ")
    d = input("where is ur property?: ")
    e = input("Do you want fire coverage (y/n)? ")
    f = input("Do you want theft too? ")

    print("Ok... we r making your policy")
    time.sleep(1.5)

    pr = 100
    if e=="y":
        pr = pr + 50
    if f=="yes" or f=="y":
        pr+=35

    if c == "":
        c = "0"

    try:
        val = int(c)
        pr = pr + (val / 1000)
    except:
        print("couldnt read property worth lol")

    print("----POLICY THING----")
    print("name:", a)
    print("age: ", b)
    print("property location: ", d)
    print("fire covr: ", e)
    print("theft?: ", f)
    print("total = $" + str(pr))

doall()

