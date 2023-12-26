import time


def swearWord(name):
    print("Yes or no: are you learning anything?")
    answer = input()

    if answer == "yes" or answer == "Yes":
        print("")
        print("Your teacher must be old and wise.")

    elif answer == "no" or answer == "No":
        while True:
            print(name, "I am so sorry")
            time.sleep(0.4)

    else:
        print("")
        print("Uhhhh.....")
        print("That wasn't an option but ok!")
    

def congrats():
    print("you have called a function!")
    print("")
    
def main():
    print("who are you?")
    name = input()
    print("Well done, " + name + "....")
    congrats()
    swearWord(name)

if __name__ == '__main__':
    main()
