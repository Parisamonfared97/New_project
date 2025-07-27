import re

person_list = []
#-------------------------------------------------------------------------------
#menu
def show_menu():
    print("1)Add New Person")
    print("2)Search Person by Mobile Number")
    print("3)Show Person List")
    print("0)Exit")
    print("-"*30)
    option = input("Enter your choice: ")
    return option
#-------------------------------------------------------------------------------
#name
def name_checker(name):
    if re.match(r"^[a-z\s\w]{3,10}$", name,re.I):
        return True
    else:
        print("Invalid Name!")
        return False

#-------------------------------------------------------------------------------
#family
def family_checker(family):
    if re.match(r"^[a-z\s\w]{3,20}$", family,re.I):
        return True
    else:
        print("Invalid Family!")
        return False

#-------------------------------------------------------------------------------
#mobile
def mobile_checker(mobile):
    #چرا warning میده؟ todo
    if re.match(r"[09|+98][^\d$]{11}", mobile):
        return True
    else:
        print("Invalid Mobile Number!")
        return False

#-------------------------------------------------------------------------------
#data
def get_data():
    name = input("Enter your Name: ")
    family = input("Enter your Family Name: ")
    mobile = input("Enter your Mobile Number: ")

    if name_checker(name) and family_checker(family) and mobile_checker(mobile):
        person = {"name": name, "family": family, "mobile": mobile}
        person_list.append(person)
        print("Info: Person Saved successfully!")
    else:
        print("Error: Invalid Information!")

#-------------------------------------------------------------------------------
#list
def show_list():
    for person in person_list:
        print(person["name"], person["family"], person["mobile"])

#-------------------------------------------------------------------------------
#find person by mobile number
def find_person(mobile):
    for person in person_list:
        if mobile == person["mobile"]:
            print("Info: Person Found!", person["name"], person["family"])
            break
    else:
        print("Error: Person not found!")

#--------------------------------------------------------------------------------
#age

def age_checker(age):
    if 20 <= age <= 30:
        return True
    else:
        print("Error : Age is not ok !!!")
        return False

#--------------------------------------------------------------------------------

def email_checker(email):
    if re.match(r"^[a-z](gmail|yahoo)$",email,re.I):
        print("Info: Email Verified!")
    else:
        print("Error: Invalid Email!")