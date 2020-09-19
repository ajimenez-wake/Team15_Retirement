import BirthYearValidation as Year


def test_handle_string():
    assert Year.birth_year_validation("Nineteen-Sixty Two") is False


def test_handle_float():
    assert Year.birth_year_validation(float(1955)) is True


def test_invalid_years():
    invalid_months = [0, 1899]
    for month in invalid_months:
        assert Year.birth_year_validation(month) is False


def test_valid_years():
    # Test every month since the test is quick to write and to run.
    valid_months = range(1900, 2020)
    for month in valid_months:
        assert Year.birth_year_validation(month) is True
