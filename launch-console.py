print("Welcome!")
user_name = input("Enter your name:")
print("Hello " + user_name + "!")
while True:
    print("1. About me")
    print("2. My goals")
    print("3. Favorite Holiday")
    print("4. Exit")
    choice = input("Choose an option (1-4):")
    if choice == "1":
        print("My name is Hansika and I'm a high school student.")
    elif choice == "2":
        print("My goal is to do well in school.")
    elif choice == "3":
        print("My favorite holiday is Christmas.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
