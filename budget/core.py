"""Core business logic for the budget CLI app."""


def add_transaction(
    transactions: list[dict[str, object]],
    transaction: dict[str, object],
) -> list[dict[str, object]]:
    """Add a transaction to the transaction list and return the updated list."""
    transactions.append(
        {
            "date": transaction["date"],
            "type": transaction["type"],
            "category": transaction["category"],
            "description": transaction["description"],
            "amount": transaction["amount"],
            "memo": transaction["memo"],
        }
    )
    return transactions


def get_balance(transactions: list[dict]) -> int:
    """Return the current balance calculated from the transaction list."""
    pass


def filter_by_category(transactions: list[dict], category: str) -> list[dict]:
    """Return transactions that match the given category."""
    pass


def load_transactions_from_csv(file_path: str) -> list[dict]:
    """Load transactions from a CSV file and return them as a list."""
    pass


def monthly_summary(transactions: list[dict]) -> dict[str, dict[str, int]]:
    """Return a month-by-month summary of income, expense, and net balance."""
    pass
