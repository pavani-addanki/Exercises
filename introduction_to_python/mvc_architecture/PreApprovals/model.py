import sqlite3
from sqlite3 import Error

class Preapprovals:
    def __init__(self):
        self.conn = conn=sqlite3.connect('Preapprovals.db')

    def save_user_details(self,user_dict):
        """
        save customer data in database
        """
        conn = self.conn
        cursorObj = conn.cursor()
        cursorObj.execute("CREATE TABLE if not exists CUSTOMER(name text, age INTEGER, occupiation text, monthly_income real, user_name text, aadhar_no INTEGER )")
        
        cursorObj.execute("INSERT INTO CUSTOMER(name, age, occupiation , monthly_income, user_name, aadhar_no) VALUES(?,?,?,?,?,?)", (user_dict['fullName'], user_dict['age'], user_dict['occupiation'], user_dict['monthly_income'], user_dict['user_name'], user_dict['aadhar_number']))
        conn.commit()

    def getCredit_history(self,aadhar_number):
        """
        get the customer credit history data from database
        """
        conn = self.conn
        cursorObj = conn.cursor()
        cursorObj.execute(f"select credit_status from CREDIT_HISTORY where aadhar_number == {aadhar_number[0]}") 
        rows = cursorObj.fetchall()
        #print(rows)  
        conn.close()
        return rows

    def get_credit_score(self,user_details):
        """
        get the credit score from database based on aadhar no/SSN
        """
        conn = self.conn
        cursorObj = conn.cursor()
        aadhar_no = user_details['aadhar_number'][0]
        cursorObj.execute(f"select credit_score from CREDIT_SCORE_INFO where aadhar_number == {aadhar_no}") 
        rows = cursorObj.fetchall()
        #print(rows)  
        conn.close()
        return rows[0][0]

    def get_products(self,credit_score):
        """
        get credir card and consumer loan proapproval products from database
        """
        conn = self.conn
        cursorObj = conn.cursor()
        cursorObj.execute(f"select product from PREAPP_PRODUCTS where cs_lowest < {credit_score} and cs_highest >= {credit_score}") 
        rows = cursorObj.fetchall()
        #print(rows)  
        conn.close()
        return rows
        


    # def create_db_connection():
    #     try:
    #         conn=sqlite3.connect('Preapprovals.db')
    #         return conn
    #     except Error:
    #         print(Error)

