import pytest
from domain.entities.customer import Customer


def test_earn_positive_points_increases_balance(
    fresh_customer: Customer,
) -> None:
    customer: Customer = fresh_customer
    customer.earn(10)
    assert customer.get_balance() == 10


def test_earn_non_positive_raises(fresh_customer: Customer) -> None:
    customer = fresh_customer
    with pytest.raises(ValueError):
        customer.earn(0)
    with pytest.raises(ValueError):
        customer.earn(-5)


def test_redeem_decreases_balance(customer_with_points: Customer) -> None:
    customer: Customer = customer_with_points
    customer.redeem(7)
    assert customer.get_balance() == 13


def test_redeem_more_than_balance_raises(
    small_balance_customer: Customer,
) -> None:
    customer: Customer = small_balance_customer
    with pytest.raises(ValueError):
        customer.redeem(6)


def test_redeem_non_positive_raises(small_balance_customer: Customer) -> None:
    customer: Customer = small_balance_customer
    with pytest.raises(ValueError):
        customer.redeem(0)
    with pytest.raises(ValueError):
        customer.redeem(-1)
