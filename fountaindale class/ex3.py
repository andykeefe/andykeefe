a = "You're never too old to learn!"
b = "Cherish your youth"

while True:  # start a loop

    print("How old are you?")
    age = int(input())    # str type --> int type
    
    if age >= 60:  # condition 1
        print(a)
        
    else:          # condition 2
        print(b)
        
    print("")
