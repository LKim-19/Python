print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You are able to get on the ride!")
    age = int(input("How old are you? "))
    if age > 18:
        print("You have to pay $12 to get on!")
    elif age >= 12 and age <=18:
        print("You have to pay $7 to get on!")
    else:
        print("You have to pay $5 to get on!")
else:
    print("You need to grow more!")