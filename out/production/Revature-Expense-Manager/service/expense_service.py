"""
Service layer: business logic only, no DB calls

* is this expense still pending before allowing an edit?
* Does this expense belong to this employer?

"""

from dao.expense_dao import submit_new_expense_dao, get_expenses_dao

# Validate the info given from the UI
def submit_new_expense(user_id, amount, description):
    try:
        if float(amount) <= 0:
            return False
        # if description is none or if its "  "
        if not description or not description.strip(): 
            return False
        submit_new_expense_dao(user_id, amount, description)
        return True
    except ValueError as e:
        print(f"Error couldn't convert {amount} to float: {e}")
        return None

# Just retrieving info so no validation required
def get_my_expenses(user_id):
    return get_expenses_dao(user_id)

