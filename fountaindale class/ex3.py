a = "You're never too old to learn!"
b = "Cherish your youth"

while True:  # start a loop

    print("How old are you?")  # input() reads whatever data is put in as a str type
    age = int(input())    # Type conversion: str type --> int type
    
    if age >= 60:  # condition 1
        print(a)
        
    else:          # condition 2
        print(b)
        
    print("")
