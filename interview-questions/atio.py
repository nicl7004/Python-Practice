class atoi:

    def convert(word):
        x = word.split()

        for letter in x:
            if x is in ["1","2","3","4","5","6","7","8","9","0"]:
                continue:
            else:
                print("failure")
                return None

        return(int(word))

def main():
    print(atoi.convert("12345"))
    print(type(atoi.convert("12345")))

    print(atoi.convert("hello"))
    print(type(atoi.convert("hello")))

if __name__ == '__main__':
    main()
