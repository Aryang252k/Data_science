import sys
from dbhelper import DBhelper
class App:
    def __init__(self):
        self.db=DBhelper()
        self.menu()

    def menu(self):
        user_info=input("""
                        1) For registeration enter 1
                        2) For login enter 2
                        3) For exit or anything else enter 3 
                        """)
    
        if user_info =='1':
            self.register()
        elif user_info == '2':
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name=input('Enter the name: ')
        email=input("Enter the email: ")
        password=input("Enter the password")




obj=App()
