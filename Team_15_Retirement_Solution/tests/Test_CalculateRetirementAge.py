import CalculateRetirementAge as Age


def test_age():
    test_years = [1937, 1938, 1939, 1940, 1941, 1942, 1943, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 2020]
    test_results = [(65, 0), (65, 2), (65, 4), (65, 6), (65, 8), (65, 10), (66, 0), (66, 0), (66, 2),
                    (66, 4), (66, 6), (66, 8), (66, 10), (67, 0), (67, 0)]

    for i in range(len(test_years)):
        assert Age.calculate_retirement_age(test_years[i]) == test_results[i]
