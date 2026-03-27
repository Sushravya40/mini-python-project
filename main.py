from pyscript import window, document

# 1. VARIABLES (Memory allocation for values)
budget = 200.0
total_spent = 0.0

# 3. DATA STRUCTURES (Using a generic List to hold Dictionary elements)
expense_ledger = []

# Ensure UI updates securely
def update_ui(text):
    document.getElementById("output").innerText = text

# Entry point of app runtime
update_ui("Ready! Enter an expense and hit 'Add to Ledger'.\nBudget limit is $200.")

def add_item(event):
    global total_spent
    
    # 2. DATATYPES (We grab Strings from the DOM)
    name_element = document.getElementById("itemName")
    amount_element = document.getElementById("itemAmount")
    
    name_str = name_element.value
    amount_str = amount_element.value
    
    # 4. FLOW CONTROLS (If/Else Condition block to ensure valid data presence)
    if not name_str or not amount_str:
        update_ui("⚠️ Error: Please enter both Name and Amount.")
        return # early return
        
    # 4. FLOW CONTROLS (Try/Except for error handling validation)
    try:
        # DATATYPES: Transforming String to Float
        amount_float = float(amount_str)
        
        # DATA STRUCTURES: Creating a Dictionary with Key/Value pairs
        new_expense_entry = {
            "name": name_str,
            "cost": amount_float
        }
        
        # DATA STRUCTURES: Adding to the List
        expense_ledger.append(new_expense_entry)
        total_spent += amount_float
        
        # Reset input fields in the UI
        name_element.value = ""
        amount_element.value = ""
        
        # Build status UI using FLOW CONTROLS (For Loop over List of Dicts)
        status_text = "----- LEDGER -----\n"
        for item in expense_ledger:
            status_text += f"• {item['name']}: ${item['cost']:.2f}\n"
            
        status_text += "------------------\n"
        status_text += f"Total Spent: ${total_spent:.2f}\n"
        
        # 4. FLOW CONTROLS (Checking logical limits with If/Else statements)
        if total_spent > budget:
            status_text += "❗ WARNING: You have exceeded budget!"
        else:
            status_text += f"✔️ You are within budget (${budget - total_spent:.2f} left)."
            
        update_ui(status_text)
        
    except ValueError:
        update_ui("⚠️ Error: Amount must be a valid number!")
