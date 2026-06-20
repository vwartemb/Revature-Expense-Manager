"""
dao layer: only talks to the database (no logic)

Insert, Select, update, and delete expenses

"""
from db.connection import get_connection
import datetime


def submit_new_expense_dao(user_id, amount, description):
    conn = get_connection()
    try:
        cur = conn.cursor()
        date = str(datetime.date.today())
        # everytime you submit a new expense you also have to need it to get approved
        cur.execute(" INSERT INTO expenses (user_id, amount, description, date) values (?,?,?,?)",
                    (user_id, amount, description, date))
        cur.execute(" INSERT INTO approvals (expense_id, status) values (?,?)",
                    (cur.lastrowid, 'pending'))
        conn.commit()
    except Exception as e:
        print(f"Error submitting expense: {e}")
        return None
    finally:
        conn.close()

# view the status of ALL of my expenses given a user_id
def get_expenses_dao(user_id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT expenses.id, 
                   expenses.amount, 
                   expenses.description, 
                   expenses.date, 
                   approvals.status
            FROM expenses
            JOIN approvals ON approvals.expense_id = expenses.id
            WHERE expenses.user_id = ?
        """, (user_id,))
        
        result = cur.fetchall()
        return result
    except Exception as e:
        print(f"Error retrieving expenses: {e}")
        return None
    finally:
        conn.close()


def edit_expense_dao(expense_id, user_id, new_amount, new_description):
    conn = get_connection()
    try:
        cur = conn.cursor()
        
        # Check if expense exists and is still pending
        cur.execute("""
            SELECT approvals.status
            FROM approvals
            JOIN expenses ON approvals.expense_id = expenses.id
            WHERE expenses.id = ?
            AND expenses.user_id = ?
        """, (expense_id, user_id))
        
        result = cur.fetchone()
        
        # If no expense found or not pending, return false
        if result is None:
            print("Expense not found")
            return False
        if result[0] != 'pending':
            print("Can only edit pending expenses")
            return False
        
        
        # Run the update
        cur.execute("""
            UPDATE expenses
            SET amount = ?, description = ?
            WHERE id = ?
            AND user_id = ?
        """, (new_amount, new_description, expense_id, user_id))
        
        conn.commit()
        return True
    
    except Exception as e:
        print(f"Error editing expense: {e}")
        return None
    finally:
        conn.close()
    