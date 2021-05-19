
def get_details():
    """
    Request customer to enter below required details
    """
    user_dict = dict()
    fullName = input("Enter your full name- ")
    
    try:
        age = int(input("Enter your age- "))
    except:
        print("please enter numeric value for age")
        age = int(input("Enter your age- "))


    occupiation = input("Enter your occupiation- ")

    try:
        monthly_income = int(input("Enter your monthly income- "))
    except:
        print("please enter numeric value for monthly income")
        monthly_income = int(input("Enter your monthly income- "))

    aadhar_number = input("Enter your Aadhar number- ")
    try:
        ad_no = int(aadhar_number)
    except:
        print("*******invalid Adhaar card number**********")
        aadhar_number = input("Enter your Aadhar number- ")

    user_name = input("Enter user name- ")
    password = input("Enter password- ")
    print("upload your Aadhar card and PAN card softcopy for account verification")
    print("Account has been created successfully")

    user_dict['fullName'] = fullName
    user_dict['age'] = age
    user_dict['occupiation'] = occupiation
    user_dict['monthly_income'] = monthly_income
    user_dict['user_name'] = user_name
    user_dict['password'] = password
    user_dict['aadhar_number'] = aadhar_number

    return user_dict

def get_user_choice():
    choice = input("Please choose one option: ")
    is_joining = False
    if (int(choice) == 1):
        print("****************Thanks for joining us :)*************")
        is_joining = True
    return is_joining

def display_products(products):
    """
    Display preapproval card products/consumer loan products to the customer
    """    
    for i in products:
        prod = i[0] 
        if(prod == 'HOME LOAN'):
            print("*******you are eligible for home loan upto 80 Lac.*********")
            print("       Buy ur dream home (with minimal process charges)   ")

        if(prod == 'PERSONAL LOAN'):
            print("*********you are eligible for peronal loan upto 5 Lac.(low interates compared to market)********")

        if(prod == 'VISA'):
            print("****You are eligible for Visa Credit card*****")
        elif(prod == 'MASTER'):
            print("********You are eligible for Master Credit card******")
        elif(prod == 'AMEX'):
            print("******You are eligible for AMEX Credit card********")  