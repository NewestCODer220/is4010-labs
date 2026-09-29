def calculate_average_age(users: list[dict]) -> float:
    """Return the average numeric age, or 0.0 when none are valid.

    Parameters
    ----------
    users : list[dict]
        A list of user records, where each record is a dictionary.

    Returns
    -------
    float
        The average age of valid numeric entries, or 0.0 if none exist.
    """
    valid_ages = []

    for user in users:
        # Validate that the item is a dictionary containing the 'age' key
        if isinstance(user, dict) and "age" in user:
            age = user["age"]

            # Exclude boolean values (bool is a subclass of int in Python)
            if isinstance(age, bool):
                continue

            # Safely attempt to parse age as a numeric float (EAFP pattern)
            try:
                numeric_age = float(age)
                if numeric_age >= 0:
                    valid_ages.append(numeric_age)
            except (ValueError, TypeError):
                continue

    if not valid_ages:
        return 0.0

    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users: list[dict]) -> list[str]:
    """Return email addresses belonging to active users.

    Parameters
    ----------
    users : list[dict]
        A list of user records, where each record is a dictionary.

    Returns
    -------
    list[str]
        A list of email addresses for active users, retaining original order.
    """
    active_emails = []

    for user in users:
        # Validate item is a dictionary
        if isinstance(user, dict):
            # Check truthiness of 'is_active' and valid presence of string email
            is_active = bool(user.get("is_active"))
            email = user.get("email")

            if is_active and isinstance(email, str) and email.strip():
                active_emails.append(email)

    return active_emails