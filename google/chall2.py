# Nicholas Clement


def salute(string):

    count = i = 0
    string = list(string)
    while len(string) > 0:
        if string[i] != "<" and string[i] != "-" and string[i] != ">":
            return 0
        elif string[i] == ">":
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
