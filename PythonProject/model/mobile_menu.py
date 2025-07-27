from product_module import *

while True:
    option=show_menu()

    if option=='1':
        product=product_add()

    elif option=='2':
        pass

    elif option=='3':
        pass

    elif option=='4':
        pass

    elif option=='0':
        break

    else:
        print("Error: Invalid option")