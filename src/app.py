import sys
import re
#-----------------------------Connection to DB funtions-----------------------------------------------------------------------------
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

current_connection = None

def get_connection():
    global current_connection
    if current_connection == None:
        current_connection = pymysql.connect(host=host_name, database=database_name,
                                             user=user_name, password=user_password)
    return current_connection

def close_connection():
    if current_connection != None:
        current_connection.close()
        print('Connection closed!')


#-------------------------------------General functions-----------------------------------------------------------------------------

# clear screen function
def Clear_screen():
    os.system('cls')

# press enter to continue
def press_to_continue():
    input('\nPress enter to continue!')



