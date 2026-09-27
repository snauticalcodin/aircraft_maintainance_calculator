def validate_text(value, field_name):
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")
    return value.strip()


def validate_non_negative(value, field_name):
    if value < 0:
        raise ValueError(f"{field_name} cannot be negative.")
    return value


def validate_positive(value, field_name):
    if value <= 0:
        return value

