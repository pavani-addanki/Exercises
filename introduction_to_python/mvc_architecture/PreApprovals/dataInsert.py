import sqlite3
from sqlite3 import Error

def create_db_connection():
    try:
        conn=sqlite3.connect('Preapprovals.db')
        return conn
    except Error:
        print(Error)

con = create_db_connection()
cursorObj = con.cursor()

# def create_credit_table(cursorObj):
#     cursorObj.execute("CREATE TABLE if not exists CREDIT_HISTORY(credit_status text, aadhar_number text)")
    
# def insert_credit_data(cursorObj,con, aadhar_number):
#     cursorObj.execute("INSERT INTO CREDIT_HISTORY(credit_status, aadhar_number) VALUES(?,?)", ('Mortgage Fraud', aadhar_number))
#     con.commit()

# def create_credit_table(cursorObj):
#     cursorObj.execute("CREATE TABLE if not exists PREAPP_PRODUCTS(cs_lowest INTEGER, cs_highest INTEGER, product TEXT)")

    #select products from PREAPP_PRODUCTS where cs_lowest < {credit_score} and cs_highest >= {credit_score}"
    
# def insert_credit_data(cursorObj,con, cs_lowest,cs_highest,product):
#     cursorObj.execute("INSERT INTO PREAPP_PRODUCTS(cs_lowest,cs_highest,product) VALUES(?,?,?)", (cs_lowest,cs_highest, product))
#     con.commit()


# def create_credit_table(cursorObj):
#     cursorObj.execute("CREATE TABLE if not exists CREDIT_SCORE_INFO(credit_score INTEGER, aadhar_number TEXT)")
# def insert_credit_data(cursorObj,con, a,b):
#     cursorObj.execute("INSERT INTO CREDIT_SCORE_INFO(aadhar_number,credit_score) VALUES(?,?)", (a,b))
#     con.commit()

def create_credit_table(cursorObj):
    cursorObj.execute("delete from CREDIT_HISTORY where aadhar_number = '1111'")


create_credit_table(cursorObj)
#insert_credit_data(cursorObj,con,'0')
# insert_credit_data(cursorObj,con, 1,'750')
# insert_credit_data(cursorObj,con, 2,'750')
# insert_credit_data(cursorObj,con, 3,'750')
# insert_credit_data(cursorObj,con, 4,'555')
# insert_credit_data(cursorObj,con, 5,'650')
# insert_credit_data(cursorObj,con, 6,'750')
# insert_credit_data(cursorObj,con, 7,'400')
# insert_credit_data(cursorObj,con, 8,'775')
# insert_credit_data(cursorObj,con, 9,'775')
# insert_credit_data(cursorObj,con, 0,'610')

