import view
from model import Preapprovals

#Banks would encourage more members by availing quick Pre-Approvals and sell 
# more credit card products/consumer loans
def bank_main_page():
    """
    Corporate Bank welcomes you to join us.
    Choose below option
    1.Create account
    2.Not interested
    """
    is_joining = view.get_user_choice()

    if is_joining:
        # get customer details
        user_details = view.get_details()
        preapp = Preapprovals()

        # save customer data in DB
        preapp.save_user_details(user_details)

        # run basic rules to check customer's eligibility                     
        is_basic_check_success = run_basic_preapprovals_rules(user_details)

        if(is_basic_check_success):
            #check credit history before calling external service to get credit score          
            credit_history = preapp.getCredit_history(user_details['aadhar_number'])
            is_ch_eligible(credit_history)

            if(is_ch_eligible): 
                #get the credit score from Experian/ Equifax / TransUnion               
                credit_score = get_credit_score(user_details)
                good_score = is_good_score(credit_score)
                if(is_good_score):
                    #get preapproval products based on credit score                  
                    products = execute_preapproval_rules(credit_score)
                    if products:
                        # display preapprovals
                        view.display_products(products)
                else:
                    print("customer credit score is less to get preapprovals")
            else:
                print("Customer credit history is not good") 


def run_basic_preapprovals_rules(user_details):  
    """
    check customer's age and income
    """  
    basic_check = False
    if user_details['age'] > 18:
        if(user_details['occupiation'] == 'soldier'):
            basic_check = True
        elif user_details['monthly_income'] > 30000:
            basic_check = True
    return basic_check

def is_ch_eligible(credit_history):
    """
    verify customer's eligibility based on credit history
    """
    is_ch_eligible = False
    if(credit_history[0][0] not in ["Credit fraud", "Mortgage Fraud"]):
        is_ch_eligible = True
    return is_ch_eligible

def get_credit_score(user_details):
    """
    get the credit score from database
    """   
    preapp = Preapprovals()
    credit_score = preapp.get_credit_score(user_details)
    return credit_score

def is_good_score(credit_score):
    """
    check whether the credit score is enough to get preapprovals
    """
    if(credit_score >= 500):
        return True
    else:
        return False

def execute_preapproval_rules(credit_score):
    """
    get preapproval products from database based on credit score
    """
    preapp = Preapprovals()
    products = preapp.get_products(credit_score)
    return products

print(bank_main_page.__doc__)
if __name__ == "__main__":
    bank_main_page() 
