class Customer:
    def __init__(self, customer_id: str, points: int = 100):
        self.customer_id = customer_id
        self.points = points

    def earn(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.points += amount

    def redeem(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.points:
            raise ValueError("Not enough points to redeem")
        new_balance = self.points - amount
        self.points = new_balance
        if self.points < 10:
            print(f"Warning: Customer {self.customer_id} low balance: {self.points} points.")

    def get_balance(self) -> int:
        return self.points

    def __str__(self) -> str:
        return f"Customer(id={self.customer_id}, points={self.points})"
