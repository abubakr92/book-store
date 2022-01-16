import time

users = {'abubakr046': '1122',
         'aliabbas039': '1234',
         'huzaifa030': '7218',
         'saad035': '4690',
         'rafay003': '1111'}

names = {'abubakr046': "Abubakr",
         'aliabbas039': "Ali Abbas",
         'huzaifa030': 'Huzaifa Yaseen',
         'saad035': 'Saad Gondal',
         "rafay003": 'Abdul Rafay'}


def signup():
    print("Please Enter following credentials: ")
    while True:
        global name
        name = input("Name: ")
        name = name.title()
        if name == '' or name == ' ':
            print("Name can't be empty, enter the name again.")
            continue
        elif name.isnumeric():
            print("Name can't be a numeric value")
            continue
        else:
            break
    while True:
        mobile_number = input("Mobile No: ")
        if len(mobile_number) == 11:
            pass
        elif len(mobile_number) > 11 or len(mobile_number) < 11:
            print("Please enter 11 digit mobile number.")
            continue
        if mobile_number[0] == "0" and mobile_number[1] == "3":
            break
        else:
            print("Please enter a phone number starting from 03")
    while True:
        username = input("Select a username: ")
        print("Please wait while we check the validity of your username", end='')
        for k in range(4):
            print(".", end='')
            time.sleep(0.4)
        for i in users:
            if username == i:
                print()
                print(f'The username "{username}" is not available. Please try another one.')
                break
        if username == i:
            continue
        else:
            break
    print()
    password = input("Type a password: ")
    print("Dear user! You have successfully signed up.")
    users[username] = password
    names[username] = name
    print()
    print("---")
    print()
    login_menu()


def login():
    a = 0
    while True:
        user_name = input("Enter your username: ")
        for i in users:
            if user_name == i:
                a += 1
                break
        global name
        name = names[i]

        if a == 0:
            print('New user? Press enter to signup instantly! or Enter "No" to re-type your username')
            new = input("")
            if new == '' or new == ' ':
                signup()
            elif new.lower() == 'no':
                print(f'Please enter a username that is already registered.')
                continue

            continue
        else:
            print(f'Hello {name.title()}! Please enter your password.')
            while True:
                p = 0
                pass_word = input(f"Password: ")
                for j in users:
                    if pass_word == users[user_name]:
                        p += 1
                        break
                if p == 1:
                    break
                else:
                    print("Wrong password, Please enter the password again.")
        if p == 1:
            break


def login_menu():

    while True:
        print("1. Login \n2. Signup")
        user_choice = input("Enter your choice: ")
        if user_choice == "1" or user_choice.lower() == 'login':
            login()
        elif user_choice == "2" or user_choice.lower() == "signup":
            signup()
        else:
            print("Invalid choice, please enter the choice again..")
            continue
        break

    print("Please wait while we log you in", end='')
    for k in range(4):
        print('.', end='')
        time.sleep(0.4)
    print()
    print("---")
    print()


    print(f'Hello {name}! Welcome to Kitabistan Book Centre!')

books = ["1984" , "Lord of the Rings" , "Animal Farm" , "Hundred Years of Solitude" , "Harry Potter" ,
         "Dune" , "The Great Gatsby" , "To kill  of Mockingbird" , "War and Peace" , "Don Quixote" ,
         "Moby Dick" , "Crime and Punishment" , "A Song of Ice and Fire "]
price={"1984":'500','Lord of the Rings':'1000', "Animal Farm":'1000' , "Hundred Years of Solitude":'1000' , "Harry Potter":'1000' ,
         "Dune":'1000' , "The Great Gatsby":'1000' , "To kill  of Mockingbird":'1000' , "War and Peace":'1000' , "Don Quixote" :'1000',
         "Moby Dick" :'1000', "Crime and Punishment":'1000' , "A Song of Ice and Fire":'1000'}


def book_buy():

    while True:

        for items in books:
            print(books)
            book = input("Enter the name: ")
            if book in books:
                print("You have to pay Rupees:",price[book],"for Book", book)
                break
            else:
                print("Sorry we don't have that book")
                break
            break

        again = input("Do you want to buy any other? ")
        if again == "Yes":
            print()
        if again=='No':
            print("Thank you for visiting us")
            break




login_menu()
book_buy()
