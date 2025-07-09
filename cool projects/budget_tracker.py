#******************************************
# 03. Personal Budget Assistant          #
# Concepts: Functions, If/Else, Loops    #
# Lists, Strings, Numbers, Booleans      #
#******************************************

def categorize_expense(amount, category):
    """Categorize and validate expenses"""
    if category.lower() in ["food", "groceries", "restaurant"]:
        return "Food & Dining"
    elif category.lower() in ["gas", "uber", "bus", "train"]:
        return "Transportation"
    elif category.lower() in ["netflix", "spotify", "games"]:
        return "Entertainment"
    else:
        return "Other"

def check_budget_status(spent, budget):
    """Check if you're within budget"""
    percentage = (spent / budget) * 100
    
    if percentage <= 70:
        return f"✅ Safe zone ({percentage:.1f}% used)"
    elif percentage <= 90:
        return f"⚠️ Caution ({percentage:.1f}% used)"
    else:
        return f"🚨 Over budget! ({percentage:.1f}% used)"

def monthly_budget_tracker():
    """Track monthly expenses"""
    monthly_budget = float(input("Enter your monthly budget: $"))  # Casting
    expenses = []  # List of dictionaries
    total_spent = 0
    
    # Add expenses throughout the month
    while True:  # Loop until user says done
        expense = input("Press Enter (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
            
        amount = float(input("Amount: $"))
        category = input("Category: ")
        
        categorized = categorize_expense(amount, category)
        expenses.append({"amount": amount, "category": categorized})
        total_spent += amount
        
        # Real-time budget check
        status = check_budget_status(total_spent, monthly_budget)
        print(f"Current status: {status}")
    
    return expenses, total_spent, monthly_budget

# Run the budget tracker
expenses, total, budget = monthly_budget_tracker()
remaining = budget - total
print(f"\nMonthly Summary:")
print(f"Budget: ${budget:.2f}")
print(f"Spent: ${total:.2f}")
print(f"Remaining: ${remaining:.2f}")