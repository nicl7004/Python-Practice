# Nicholas Clement


def salute(string):
    string = string.replace(" ", "")
    for each in string:
        if each != "<" and each != "-" and each != ">":
            print("Error with input")
            return 0
    count = i = 0
    string = list(string)
    while len(string) > 0:
        if string[i] == ">":
            for b in string:
                if b == "<":
                    count +=2
        del string[i]







    return count






if __name__ == "__main__":
    x = "<--g--><><"
    y = "fdsa"
    z = "--->-><-><-->-"

    print(salute(y), salute(x), salute(z))
