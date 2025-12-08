import pytest
from domain.entities.customer import Customer


def test_earn_positive_points_increases_balance(
    fresh_customer: Customer,
) -> None:
    points_before_add = fresh_customer.get_balance()
    fresh_customer.earn(10)
    assert fresh_customer.get_balance() == points_before_add + 10


def test_earn_non_positive_raises(fresh_customer: Customer) -> None:
    customer = fresh_customer
    with pytest.raises(ValueError):
        customer.earn(0)
    with pytest.raises(ValueError):
        customer.earn(-5)


def test_redeem_decreases_balance(customer_with_points: Customer) -> None:
    customer: Customer = customer_with_points
    points_before_substract = customer_with_points.get_balance()
    customer.redeem(7)
    assert customer.get_balance() == points_before_substract - 7


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


def test_low_balance_warning_printed(
    small_balance_customer: Customer,
    capsys,
) -> None:
    customer: Customer = small_balance_customer
    customer.redeem(1)
    captured = capsys.readouterr()
    assert f"Warning: Customer {customer.customer_id} low balance: "
    assert f"{customer.get_balance()} points." in captured.out


def test_low_balance_warning_when_crossing_threshold(
    customer_with_points: Customer,
    capsys,
) -> None:
    customer: Customer = customer_with_points
    customer.redeem(11)
    captured = capsys.readouterr()
    assert (
        f"Warning: Customer {customer.customer_id} low balance: "
        f"{customer.get_balance()} points." in captured.out
    )


def test_no_warning_at_exact_threshold(
    customer_with_points: Customer,
    capsys,
) -> None:
    points_before_substract = customer_with_points.get_balance()
    customer: Customer = customer_with_points
    customer.redeem(10)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""
    assert customer.get_balance() == points_before_substract - 10


def test_warning_on_zero_balance(
    small_balance_customer: Customer,
    capsys,
) -> None:
    customer: Customer = small_balance_customer
    customer.redeem(5)
    captured = capsys.readouterr()
    assert (
        f"Warning: Customer {customer.customer_id} low balance: "
        f"{customer.get_balance()} points." in captured.out
    )
    assert customer.get_balance() == 0


def test_no_warning_on_earn(
    small_balance_customer: Customer,
) -> None:
    customer: Customer = small_balance_customer
    customer.earn(10)
    assert customer.get_balance() == 15
