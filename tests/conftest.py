import pytest

from domain.entities.customer import Customer


@pytest.fixture
def fresh_customer():
    return Customer("customer_1")


@pytest.fixture
def customer_with_points():
    return Customer("customer_1", points=20)


@pytest.fixture
def small_balance_customer():
    return Customer("customer_1", points=5)
