import CalculateRetirementDate as Rd


def test_1937_lower_boundary():
    retirement_date = Rd.calculate_retirement_date(1900, 1, 65, 0)
    assert retirement_date.year == 1965
    assert retirement_date.month == 1


def test_1937_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1937, 12, 65, 0)
    assert retirement_date.year == 2002
    assert retirement_date.month == 12


def test_1938_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1938, 12, 65, 2)
    assert retirement_date.year == 2004
    assert retirement_date.month == 2


def test_1939_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1939, 12, 65, 4)
    assert retirement_date.year == 2005
    assert retirement_date.month == 4


def test_1940_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1940, 12, 65, 6)
    assert retirement_date.year == 2006
    assert retirement_date.month == 6


def test_1941_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1941, 12, 65, 8)
    assert retirement_date.year == 2007
    assert retirement_date.month == 8


def test_1942_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1942, 12, 65, 10)
    assert retirement_date.year == 2008
    assert retirement_date.month == 10


def test_1943_54_lower_boundary():
    retirement_date = Rd.calculate_retirement_date(1943, 1, 66, 0)
    assert retirement_date.year == 2009
    assert retirement_date.month == 1


def test_1943_54_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1954, 1, 66, 0)
    assert retirement_date.year == 2020
    assert retirement_date.month == 1


def test_1955_lower_boundary():
    retirement_date = Rd.calculate_retirement_date(1955, 1, 66, 2)
    assert retirement_date.year == 2022
    assert retirement_date.month == 2


def test_1956_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1956, 12, 66, 4)
    assert retirement_date.year == 2023
    assert retirement_date.month == 4


def test_1957_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1957, 12, 66, 6)
    assert retirement_date.year == 2024
    assert retirement_date.month == 6


def test_1958_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1958, 12, 66, 8)
    assert retirement_date.year == 2025
    assert retirement_date.month == 8


def test_1959_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1959, 12, 66, 10)
    assert retirement_date.year == 2026
    assert retirement_date.month == 10


def test_1960_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(1960, 12, 67, 0)
    assert retirement_date.year == 2027
    assert retirement_date.month == 12


def test_2020_upper_boundary():
    retirement_date = Rd.calculate_retirement_date(2020, 12, 67, 0)
    assert retirement_date.year == 2028
    assert retirement_date.month == 12
