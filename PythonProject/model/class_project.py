from parisa_module import *


while True:
    option=show_menu()

    if option == "1":
        get_data()

    elif option == "2":
        person_mobile = input("Enter your Mobile Number to search: ")
        find_person(person_mobile)

    elif option == "3":
        print("People List: ")
        show_list()

    elif option == "0":
        break
    else:
        print("Error: Invalid Option!!")
        print("-"*30)



