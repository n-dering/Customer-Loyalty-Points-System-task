class Customer:
    def __init__(self, customer_id, points=0):
        self.customer_id = customer_id
        self.points = points

    def add(self, amount: int) -> None:
        if amount <= 0:
            print("Amount must be positive")
            return
        self.points += amount

    def subtract(self, amount: int) -> None:
        if amount <= 0:
            print("Amount must be positive")
            return
        
        if amount > self.points:
            print("You don't have enough points")
            return
        
        new_balance = self.points - amount
        
        if new_balance < 10:
            print(
                f"Warning: Customer {self.customer_id} has a low balance: "
                f"{new_balance} points."
            )
        self.points = new_balance

    def get_balance(self) -> int:
        return self.points

    def __str__(self):
        return f"Customer(id={self.customer_id}, points={self.points})"
