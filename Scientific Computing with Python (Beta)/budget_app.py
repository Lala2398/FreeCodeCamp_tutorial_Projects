class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Add a deposit to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Add a withdrawal to the ledger if funds are sufficient."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Calculate current balance."""
        balance = sum(item["amount"] for item in self.ledger)
        return balance

    def transfer(self, amount, category):
        """Transfer funds between categories if sufficient."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Check if there are sufficient funds for an operation."""
        return amount <= self.get_balance()

    def __str__(self):
        """Custom string representation of the category."""
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:23}"
            amt = f"{item['amount']:.2f}"
            items += f"{desc}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    """Generate a bar chart of spending percentages by category."""
    total_spent = 0
    spending = {}

    # Calculate total and category-wise spending
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spending[category.name] = spent
        total_spent += spent

    # Calculate spending percentages
    percentages = {name: int((spent / total_spent) * 100) // 10 * 10 for name, spent in spending.items()}

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for name in categories:
            chart += "o  " if percentages[name.name] >= i else "   "
        chart += "\n"

    # Add horizontal line
    chart += "    -" + "---" * len(categories) + "\n"

    # Add vertical labels
    max_len = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_len) for category in categories]
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip("\n")


# Example use
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
clothing.deposit(500, "initial deposit")
clothing.withdraw(25.55)
clothing.withdraw(100)

entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(15)

food.transfer(50, clothing)

print(food)
print(clothing)
print(entertainment)
print(create_spend_chart([food, clothing, entertainment]))
