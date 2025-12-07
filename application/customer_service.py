from typing import Optional
from domain.entities.customer import Customer
from infrastructure.customer import CustomerRepo


class CustomerService:
    def __init__(self, repository: CustomerRepo) -> None:
        self._repo: CustomerRepo = repository

    def _get_or_create(self, customer_id: str) -> Customer:
        existing: Optional[Customer] = self._repo.get(customer_id)
        if existing is not None:
            return existing
        customer = Customer(customer_id)
        self._repo.save(customer)
        return customer

    def earn(self, customer_id: str, points: int) -> int:
        customer: Customer = self._get_or_create(customer_id)
        customer.earn(points)
        self._repo.save(customer)
        return customer.get_balance()

    def redeem(self, customer_id: str, points: int) -> int:
        customer: Customer = self._get_or_create(customer_id)
        customer.redeem(points)
        self._repo.save(customer)
        return customer.get_balance()

    def balance(self, customer_id: str) -> int:
        customer: Customer = self._get_or_create(customer_id)
        return customer.get_balance()
