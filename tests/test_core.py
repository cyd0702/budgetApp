"""Tests for budget core logic."""

from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the transaction list length."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        }
    ]
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == 2


def test_add_transaction_saves_negative_amount() -> None:
    """Negative expense amounts should be stored without modification."""
    transactions = []
    transaction = {
        "date": "2026-01-10",
        "type": "지출",
        "category": "교통",
        "description": "지하철",
        "amount": -1500,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["amount"] == -1500


def test_add_transaction_saves_positive_amount() -> None:
    """Positive income amounts should be stored without modification."""
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "중고 판매",
        "amount": 25000,
        "memo": "중고마켓",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["amount"] == 25000


def test_add_transaction_handles_empty_description() -> None:
    """Empty descriptions should be stored as empty strings."""
    transactions = []
    transaction = {
        "date": "2026-01-30",
        "type": "지출",
        "category": "식비",
        "description": "",
        "amount": -5800,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[0]["description"] == ""
