"""
UI Layer: input/output only, no logic 

* Display menus
* Collects user input
* Calls service methods 

"""
from service.user_service import login
from service.expense_service import submit_new_expense, get_expenses_by_user

def login_menu():
    attempts = 0
    while attempts < 3:
        username = input("Username: ")
        password = input("Password: ")
        login_attempt = login(username, password)
        
        if login_attempt is not None:
            print("\nWelcome to the main employee menu")
            employee_menu(login_attempt)
            break
        else:
            print("Invalid credientials") 
            attempts += 1
    else:
        print("Too many failed attempts. Goodbye.")
    
def employee_menu(user):
    while True:
        print("\n--- Employee Menu ---")
        print("1. Submit new expense")
        print("2. View my expenses")
        print("3. Edit expense")
        print("4. Delete expense")
        print("5. View history")
        print("6. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            submit_expense_menu(user)
        elif choice == "2":
            view_expenses_menu(user)
        elif choice == "3":
            edit_expense_menu(user)
        elif choice == "4":
            delete_expense_menu(user)
        elif choice == "5":
            view_history_menu(user)
        elif choice == "6":
            print("\nLogging out...")
            break
        else:
            print("Invalid choice, please try again")
    

def submit_expense_menu(user):
    amount = str(input("Enter Amount: "))
    description = input("Enter Description: ")
    try:
        submit_new_expense(user[0], amount, description)
        print("Successfully submitted an expense!")
    except Exception as e:
        print(f"Error submitting e