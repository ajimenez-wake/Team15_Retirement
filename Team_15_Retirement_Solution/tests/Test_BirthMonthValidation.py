import BirthMonthValidation as Month


def test_handle_string():
    assert Month.birth_month_validation("January") is False


def test_handle_float():
    assert Month.birth_month_validation(float(12)) is True


def test_invalid_months():
    invalid_months = [-1, 0, 13]
    for month in invalid_months:
        assert Month.birth_month_validation(month) is False


def test_valid_months():
    # Test every month since the test is quick to write and to run.
    valid_months = range(1, 13)
    for month in valid_months:
        assert Month.birth_month_validation(month) is True
