import typer
from user import Customer

app = typer.Typer()

customers = {}


def get_customer(customer_id: str) -> Customer:
    if customer_id not in customers:
        customers[customer_id] = Customer(customer_id)
    return customers[customer_id]


@app.command()
def earn(customer_id: str, points: int):
    customer = get_customer(customer_id)
    customer.add(points)
    print(f"earned {points} balance={customer.points}")


@app.command()
def redeem(customer_id: str, points: int):
    customer = get_customer(customer_id)
    customer.subtract(points)
    print(f"redeemed {points} balance={customer.points}")


@app.command()
def balance(customer_id: str):
    customer = get_customer(customer_id)
    print(f"balance={customer.points}")


if __name__ == "__main__":
    app()
