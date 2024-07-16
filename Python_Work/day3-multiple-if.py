print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You are able to get on the ride!")
    age = int(input("How old are you? "))
    if age > 18:
        print("You have to pay $12 to get on!")
        bill += 12
    elif age >= 12 and age <=18:
        print("You have to pay $7 to get on!")
        bill += 7
    else:
        print("You have to pay $5 to get on!")
        bill += 5

    wants_photo = input("Do you want a photo taken? Y or N. ")

    if wants_photo == 'Y'or wants_photo == 'y':
        print("Wants a photo")
        bill += 3
    else:
        print("Does not want a photo")

    print(f'This is your bill: ${bill}')
else:
    print("You need to grow more!")