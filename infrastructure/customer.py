from domain.entities.customer import Customer


class CustomerRepo:
    def __init__(self):
        self._store = {}

    def get(self, customer_id: str) -> Customer:
        return self._store.get(customer_id)

    def save(self, customer: Customer) -> None:
        self._store[customer.customer_id] = customer
