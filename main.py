import emoji

def main_menu():
    while True:
        print(emoji.emojize("Hi:red_heart: Welcome to mini instagram :rocket:"))
        print("\t1)Home\n\t2)Profile\n\t3)Explore\n\t4)Requests\n\t5)NewPost\n\t6)Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            print(emoji.emojize("Invalid choice:frowning_face:"))
            break



if __name__ == '__main__':
    main_menu()