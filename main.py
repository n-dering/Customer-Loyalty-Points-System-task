import typer
from application.customer_service import CustomerLoyalityService
from infrastructure.customer import CustomerRepo

app: typer.Typer = typer.Typer()
service: CustomerLoyalityService = CustomerLoyalityService(CustomerRepo())


@app.command()
def earn(customer_id: str, points: int) -> None:
    try:
        balance: int = service.earn(customer_id, points)
        print(f"earned {points} balance={balance}")
    except Exception as e:
        print(str(e))


@app.command()
def redeem(customer_id: str, points: int) -> None:
    try:
        balance: int = service.redeem(customer_id, points)
        print(f"redeemed {points} balance={balance}")
    except Exception as e:
        print(str(e))


@app.command()
def balance(customer_id: str) -> None:
    try:
        current: int = service.balance(customer_id)
        print(f"balance={current}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    app()
