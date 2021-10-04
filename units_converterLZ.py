# startuem

while True:
    x = input("soo what do you wanna know? outside temp?? \n please put your data to convert (like this 12F or 99C) : ")
    i_convention = x[-1]
    result = ""
    edin_izmer = ""
    if i_convention.upper() == "C":
        degree = int(x[:-1])
        result = int(round((9 * degree) / 5 + 32))
        edin_izmer = "Fahrenheit"
        print("\n The temperature in", edin_izmer, "is", result, "degrees.")
        print("please note that you can leave this app by 'exit' command at the next input\n")
    elif i_convention.upper() == "F":
        degree = int(x[:-1])
        result = int(round((degree - 32) * 5 / 9))
        edin_izmer = "Celsius"
        print("\n The temperature in", edin_izmer, "is", result, "degrees.")
        print("please note that you can leave this app by 123 123 command at the next input\n")
    else:
        print("\n please point your edinici izmereniya properly \n")
print("gg")
