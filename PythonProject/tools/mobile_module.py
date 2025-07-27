#product_checkers
product_list=[]


def show_menu(option):
    print("1)Add New Phone")
    print("2)Search Phone by code")
    print("3)Search Phone by Price")
    print("4)Show Phones List")
    print("0)Exit")
    print("-"*30)
    option = input("Enter your choice: ")
    return option


def product_add(product):
    name=input("Enter your phone name: ")
    code=input("Enter phone code: ")
    brand=input("Enter brand name: ")
    price=int(input("Enter price: "))
    product={"name":name, "code":code, "brand":brand, "price":price}
    product_list.append(product)
    return product

def code_search(code):
    if code in product_list:
        return code
        
def brand_checker(brand):
    pass

def code_checker(code):
    pass

def price_checker(price):
    pass

